from flask import Blueprint, render_template, flash, request, url_for, redirect
from app import app, db
from app.models import User, Event, Workshop, PasswordReset
from flask.ext.login import LoginManager
from flask.ext.login import login_user, logout_user
from htmlmin.minify import html_minify
from flask.ext.mail import Mail, Message
import random
import string

general = Blueprint('general', __name__)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


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
        return redirect(url_for('.index'))
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
        return redirect(url_for('.login'))
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    login_user(registered_user, remember=remember_me)
    flash('Logged in successfully')
    return html_minify(render_template('users/user.html'))


@general.route('/login/forgot-password/', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            token = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(64)])
            old_password_reset = PasswordReset.query.filter_by(email=request.form['email']).first()
            if old_password_reset:
                db.session.delete(old_password_reset)
                db.session.commit()
            password_reset = PasswordReset(request.form['email'], token)
            db.session.add(password_reset)
            db.session.commit()
            msg = Message(subject='Techvaganza 2k16 : Password Reset',
                          sender='techvaganza2k16@gmail.com',
                          recipients=[request.form['email']]
                          )
            msg.body = "Reset your password : http://localhost:5000" + \
                       url_for('general.reset_password', token=token, user_id=user.id)
            Mail(app).send(msg)
            flash("Password reset email sent, check your mail!")
        else:
            flash("Email doesn't exist!")
    return html_minify(render_template('forgot-password.html'))


@general.route('/login/reset-password/<token>/<int:user_id>', methods=['GET', 'POST'])
def reset_password(token, user_id):
    if request.method == 'POST':
        user = User.query.filter_by(id=user_id).first()
        password_reset = PasswordReset.query.filter_by(email=user.email).first()
        if token == password_reset.token:
            if request.form['password'] == request.form['confirm_password']:
                # Just noticed, we haven't hashed passwords -_-
                user.password = request.form['password']
                db.session.delete(password_reset)
                db.session.commit()
                flash("Password changed successfully.")
            else:
                flash("Passwords don't match!")
        else:
            flash("Failure: Illegal token found.")
    return html_minify(render_template('reset-password.html'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@general.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('.index'))


@general.route('/events/', methods=['GET'])
@general.route('/events/<int:page>/', methods=['GET'])
def events(page=1):
    pagination = Event.query.paginate(page, app.config['RESULTS_PER_PAGE'],
                                      False)
    return html_minify(render_template('events/events.html',
                                       pagination=pagination))


@general.route('/events/<slug>/', methods=['GET', 'POST'])
def event(slug):
    if request.method == 'POST':
        pass
    event = Event.query.filter_by(slug=slug).first()
    return html_minify(render_template('events/event.html', event=event))


@general.route('/workshops/', methods=['GET'])
@general.route('/workshops/<int:page>/', methods=['GET'])
def workshops(page=1):
    pagination = Workshop.query.paginate(page, app.config['RESULTS_PER_PAGE'],
                                         False)
    return html_minify(render_template('workshops/workshops.html',
                                       pagination=pagination))


@general.route('/workshops/<slug>/', methods=['GET', 'POST'])
def workshop(slug):
    if request.method == 'POST':
        pass
    workshop = Workshop.query.filter_by(slug=slug).first()
    return html_minify(
        render_template('workshops/workshop.html', workshop=workshop))


@general.route('/user/', methods=['GET'])
def user():
    return html_minify(render_template('users/user.html'))
