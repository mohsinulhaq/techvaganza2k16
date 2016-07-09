from flask import Blueprint, render_template, flash, request, redirect, url_for
from app import app, db
from app.models import User, Event, Workshop
from flask.ext.login import LoginManager
from flask.ext.login import login_user, logout_user
from htmlmin.minify import html_minify

general = Blueprint('general', __name__)
login_manager = LoginManager()
login_manager.init_app(app)


@general.route('/', methods=['GET'])
def index():
    rendered_html = render_template('index.html')
    return html_minify(rendered_html)


@general.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(request.form['password'],
                    request.form['name'],
                    request.form['email'],
                    request.form['cell'],
                    request.form['gender'],
                    request.form['college'],
                    request.form['batch'],
                    request.form['branch'])
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful!')
    return html_minify(render_template('register.html'))


@general.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return html_minify(render_template('login.html'))
    email = request.form['email']
    password = request.form['password']
    registered_user = User.query.filter_by(email=email,
                                           password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid')
        return html_minify(render_template('login.html'))
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    login_user(registered_user, remember=remember_me)
    flash('Logged in successfully')
    return html_minify(render_template('users/user.html'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@general.route('/logout/')
def logout():
    logout_user()
    return html_minify(render_template('index.html'))


@general.route('/events/', methods=['GET'])
@general.route('/events/<int:page>', methods=['GET'])
def events(page=1):
    pagination = Event.query.paginate(page, app.config['RESULTS_PER_PAGE'],
                                      False)
    return html_minify(render_template('events/events.html',
                                       pagination=pagination))


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
                                       pagination=pagination))


@general.route('/workshops/<slug>', methods=['GET', 'POST'])
def workshop(slug):
    if request.method == 'POST':
        pass
    workshop = Workshop.query.filter_by(slug=slug).first()
    return html_minify(
        render_template('workshops/workshop.html', workshop=workshop))


@general.route('/user/', methods=['GET'])
def user():
    return html_minify(render_template('users/user.html'))
