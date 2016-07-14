from flask import Blueprint, render_template, request
from app import app
from app.models import User, Event, Workshop
from flask_login import LoginManager, login_required
from htmlmin.minify import html_minify

general = Blueprint('general', __name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '.login'


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
    pagination = Event.query.paginate(page, app.config['RESULTS_PER_PAGE'],
                                      False)
    return html_minify(render_template('events/events.html',
                                       pagination=pagination,
                                       entities="general.events"))


@general.route('/events/<slug>', methods=['GET', 'POST'])
def event(slug):
    if request.method == 'POST':
        pass
    event = Event.query.filter_by(slug=slug).first()
    return html_minify(render_template('events/event.html', event=event))


@general.route('/workshops/', methods=['GET'])
@general.route('/workshops/<int:page>', methods=['GET'])
def workshops(page=1):
    pagination = Workshop.query.paginate(page, app.config['RESULTS_PER_PAGE'],
                                         False)
    return html_minify(render_template('workshops/workshops.html',
                                       pagination=pagination,
                                       entities="general.workshops"))


@general.route('/workshops/<slug>', methods=['GET', 'POST'])
def workshop(slug):
    if request.method == 'POST':
        pass
    workshop = Workshop.query.filter_by(slug=slug).first()
    return html_minify(
        render_template('workshops/workshop.html', workshop=workshop))


@general.route('/user/', methods=['GET'])
@login_required
def user():
    return html_minify(render_template('users/user.html'))
