from flask import Blueprint, render_template, request, session, jsonify, flash
from app import app, db
from app.models import User, Event, Workshop, EventRegistration, \
    WorkshopRegistration
from flask_login import LoginManager, login_required
from htmlmin.minify import html_minify
from sqlalchemy.exc import IntegrityError
from app.utils import nocache

general = Blueprint('general', __name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'authentication.login'


@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id == userid).first()


@general.route('/', methods=['GET'])
def index():
    rendered_html = render_template('index.html')
    return html_minify(rendered_html)


@general.route('/events/', methods=['GET'])
@general.route('/events/<int:page>', methods=['GET'])
def events(page=1):
    pagination = Event.query.paginate(page,
                                      app.config['RESULTS_PER_PAGE'],
                                      False)
    return html_minify(render_template('events/events.html',
                                       pagination=pagination,
                                       entities="general.events"))


@general.route('/events/<slug>', methods=['GET', 'POST'])
@nocache
def event(slug):
    if request.method == 'POST':
        if 'user_id' in session:
            try:
                user = User.query.filter_by(id=session['user_id']).first()
                slug = request.path.split('/')[2]
                event = Event.query.filter_by(slug=slug).first()
                event_registration = EventRegistration(user_id=user.id,
                                                       event_id=event.id)
                try:
                    db.session.add(event_registration)
                    db.session.commit()
                    return jsonify(success=True, registered=True)
                except IntegrityError:
                    db.session.rollback()
                    EventRegistration.query.filter_by(user_id=user.id,
                                                      event_id=event.id).delete()
                    db.session.commit()
                    return jsonify(success=True, registered=False)
            except Exception as e:
                return jsonify(success=False, message=e)
        else:
            flash('You must log in first!')
            return jsonify(success=False, login_required=True)

    event = Event.query.filter_by(slug=slug).first_or_404()
    registered = False
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        if EventRegistration.query.filter_by(user_id=user.id,
                                             event_id=event.id).first():
            registered = True

    return html_minify(render_template('events/event.html', event=event,
                                       registered=registered))


@general.route('/workshops/', methods=['GET'])
@general.route('/workshops/<int:page>', methods=['GET'])
def workshops(page=1):
    pagination = Workshop.query.paginate(page,
                                         app.config['RESULTS_PER_PAGE'],
                                         False)
    return html_minify(render_template('workshops/workshops.html',
                                       pagination=pagination,
                                       entities="general.workshops"))


@general.route('/workshops/<slug>', methods=['GET', 'POST'])
@nocache
def workshop(slug):
    if request.method == 'POST':
        if 'user_id' in session:
            try:
                user = User.query.filter_by(id=session['user_id']).first()
                slug = request.path.split('/')[2]
                workshop = Workshop.query.filter_by(slug=slug).first()
                workshop_registration = WorkshopRegistration(user_id=user.id,
                                                             workshop_id=workshop.id)
                try:
                    db.session.add(workshop_registration)
                    db.session.commit()
                    return jsonify(success=True, registered=True)
                except IntegrityError:
                    db.session.rollback()
                    WorkshopRegistration.query.filter_by(user_id=user.id,
                                                         workshop_id=workshop.id).delete()
                    db.session.commit()
                    return jsonify(success=True, registered=False)
            except Exception as e:
                return jsonify(success=False, message=e)
        else:
            flash('You must log in first!')
            return jsonify(success=False, login_required=True)

    workshop = Workshop.query.filter_by(slug=slug).first_or_404()
    registered = False
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        if WorkshopRegistration.query.filter_by(user_id=user.id,
                                                workshop_id=workshop.id).first():
            registered = True

    return html_minify(
        render_template('workshops/workshop.html', workshop=workshop,
                        registered=registered))


@general.route('/user/', methods=['GET'])
@login_required
def user():
    user = User.query.filter_by(id=session['user_id']).first()
    event_registrations = EventRegistration.query.filter_by(
        user_id=user.id).all()
    workshop_registrations = WorkshopRegistration.query.filter_by(
        user_id=user.id).all()
    events = []
    workshops = []
    for event_registration in event_registrations:
        events.append(
            Event.query.filter_by(id=event_registration.event_id).first())

    for workshop_registration in workshop_registrations:
        workshops.append(
            Workshop.query.filter_by(
                id=workshop_registration.workshop_id).first())

    return html_minify(
        render_template('users/user.html', events=events,
                        workshops=workshops))
