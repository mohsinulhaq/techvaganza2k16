import os
from flask import render_template, flash, request, redirect, abort
from app import app, db
from app.models import User, Event, Workshop
from app.forms import RegistrationForm
from htmlmin.minify import html_minify
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.login import LoginManager


login_manager = LoginManager()
login_manager.init_app(app)


# -----------------------------------------------------------------------------------------
#     Admin Routes
# -----------------------------------------------------------------------------------------

@app.route('/admin/')
def admin_dashboard():
    return html_minify(render_template('admin/base.html'))


@app.route('/admin/events/', methods=['GET', 'POST'])
def admin_dashboard_events():
    if request.method == 'POST':
        event = Event(request.form['title'], request.form['slug'],
                      request.form['description'], request.form['body'])
        db.session.add(event)
        db.session.commit()
        flash('Event Upload Successful!')
    return html_minify(render_template('admin/events.html'))


@app.route('/admin/notifications/', methods=['GET', 'POST'])
def admin_dashboard_notifications():
    if request.method == 'POST':
        file = False
        if 'file' not in request.files:
            flash('Sleepy much? Select a proper file first.')
        file = request.files['file']
        if file.filename == '':
            flash('Sleepy much? Select a proper file first.')
            return redirect(request.url)
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            flash('Notification uploaded successfully')
    return html_minify(render_template('admin/notifications.html'))


@app.route('/admin/registrations/')
def admin_dashboard_registrations():
    users = User.query.all()
    return html_minify(render_template('admin/registrations.html', users=users))


@app.route('/admin/registrations/<int:id>')
def admin_dashboard_view_registration(id):
    user = User.query.get(id)
    return html_minify(render_template('admin/viewregistration.html', user=user))

# -----------------------------------------------------------------------------------------
#     General Routes
# -----------------------------------------------------------------------------------------


@app.route('/', methods=['GET'])
def index():
    rendered_html = render_template('index.html')
    return html_minify(rendered_html)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
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


@app.route('/login', methods=['GET', 'POST'])
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


@app.route('/logout')
def logout():
    logout_user()
    return html_minify(render_template('index.html'))


@app.route('/events/', methods=['GET'])
@app.route('/events/<int:page>', methods=['GET'])
def events(page=1):
    pagination = Event.query.paginate(page, app.config['RESULTS_PER_PAGE'],
                                      False)
    return html_minify(render_template('events/events.html',
                                       pagination=pagination))


@app.route('/events/<slug>', methods=['GET', 'POST'])
def event(slug):
    if request.method == 'POST':
        pass
    event = Event.query.filter_by(slug=slug).first()
    return html_minify(render_template('events/event.html', event=event))


@app.route('/workshops/', methods=['GET'])
@app.route('/workshops/<int:page>', methods=['GET'])
def workshops(page=1):
    pagination = Workshop.query.paginate(page, app.config['RESULTS_PER_PAGE'],
                                         False)
    return html_minify(render_template('workshops/workshops.html',
                                       pagination=pagination))


@app.route('/workshops/<slug>', methods=['GET', 'POST'])
def workshop(slug):
    if request.method == 'POST':
        pass
    workshop = Workshop.query.filter_by(slug=slug).first()
    return html_minify(render_template('workshops/workshop.html', workshop=workshop))

# -----------------------------------------------------------------------------------------
#     Contact
# -----------------------------------------------------------------------------------------

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # TODO SEND MAIL
        flash('Message Sent!')
    return html_minify(render_template('contact.html'))


# -----------------------------------------------------------------------------------------
#     User Routes
# -----------------------------------------------------------------------------------------

@app.route('/user/', methods=['GET'])
def user():
    return html_minify(render_template('users/user.html'))


# -----------------------------------------------------------------------------------------
#     Housekeeping Routes
# -----------------------------------------------------------------------------------------

@app.route('/<page>/')
def housekeeping(page):
    """
    For handling pages: about, contact, sponsors, our team.
    """
    try:
        return html_minify(render_template('housekeeping/' + page + '.html'))
    except Exception:
        abort(404)


# -----------------------------------------------------------------------------------------
#     Error Handlers
# -----------------------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    pass
