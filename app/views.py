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
def admin_dashboard():
    return html_minify(render_template('admin/admin-dashboard.html'))


@app.route('/admin/events/', methods = ['GET', 'POST'])
def admin_dashboard_events():
    if request.method == 'POST':
        event = Event(request.form['title'],
                    request.form['slug'],
                    request.form['description'],
                    request.form['body'])
        db.session.add(event)
        db.session.commit()
        flash('Event Upload Successful!')
    return html_minify(render_template('admin/events.html'))


@app.route('/admin/notifications/', methods = ['GET', 'POST'])
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
    return html_minify(render_template('register.html'))

@app.route('/events/', methods = ['GET'])
@app.route('/events/<int:page>', methods = ['GET'])
def events(page = 1):
    pagination = Event.query.paginate(page, app.config['RESULTS_PER_PAGE'], False)
    return html_minify(render_template('events/events.html', pagination = pagination))


@app.route('/events/<slug>', methods = ['GET'])
def event(slug):
    event = Event.query.filter_by(slug = slug).first()
    return html_minify(render_template('events/event.html', event = event))


# -----------------------------------------------------------------------------------------
#     Housekeeping Routes
# -----------------------------------------------------------------------------------------

@app.route('/<page>/')
def housekeeping(page):  # For handling pages: about, contact, sponsors, our team.
    try:
        return html_minify(render_template('housekeeping/' + page + '.html'))
    except Exception:
        return "404"


# -----------------------------------------------------------------------------------------
#     Error Handlers
# -----------------------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    pass
