import os
from flask import render_template, flash, request, redirect, session
from app import app, db
from app.models import User, Event
from app.forms import RegistrationForm
from htmlmin.minify import html_minify

# -----------------------------------------------------------------------------------------
#     Admin Routes
# -----------------------------------------------------------------------------------------

@app.route('/admin/')
def adminDashboard():
    return render_template('admin/admin-dashboard.html')


@app.route('/admin/events/', methods = ['GET', 'POST'])
def adminDashboardEvents():
    if request.method == 'POST':
        event = Event(request.form['title'],
                    request.form['slug'],
                    request.form['description'],
                    request.form['body'])
        db.session.add(event)
        db.session.commit()
        flash('Event Upload Successful!')
    return render_template('admin/events.html')


@app.route('/admin/notifications/', methods = ['GET', 'POST'])
def adminDashboardNotifications():
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
    return render_template('admin/notifications.html')


@app.route('/admin/registrations/')
def adminDashboardRegistrations():
    users = User.query.all()
    return render_template('admin/registrations.html', users=users)


@app.route('/admin/registrations/<int:id>')
def adminDashboardViewRegistration(id):
    user = User.query.get(id)
    return render_template('admin/viewregistration.html', user=user)

# -----------------------------------------------------------------------------------------
#     General Routes
# -----------------------------------------------------------------------------------------

@app.route('/', methods = ['GET'])
def index():
    rendered_html = render_template('index.html')
    return html_minify(rendered_html)


@app.route('/register/', methods = ['GET', 'POST'])
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
    return render_template('register.html')


@app.route('/events/', methods = ['GET'])
def events():
    events = Event.query.all()
    return render_template('events/events.html', events = events)


@app.route('/events/<slug>', methods = ['GET'])
def event(slug):
    event = Event.query.filter_by(slug = slug).first()
    return render_template('events/event.html', event = event)


# -----------------------------------------------------------------------------------------
#     Housekeeping Routes
# -----------------------------------------------------------------------------------------

@app.route('/<page>/')
def housekeeping(page):  # For handling pages: about, contact, sponsors, our team.
    try:
        return render_template('housekeeping/' + page + '.html')
    except Exception:
        return "404"


# -----------------------------------------------------------------------------------------
#     Error Handlers
# -----------------------------------------------------------------------------------------

@app.errorhandler(404)
def pageNotFound(e):
    pass
