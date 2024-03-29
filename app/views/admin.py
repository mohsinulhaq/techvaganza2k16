import os
from flask import Blueprint, render_template, flash, request, redirect, url_for
from app import app, db
from app.models import User, Event, Workshop
from htmlmin.minify import html_minify

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return html_minify(render_template('admin/registrations.html'))


@admin.route('/activities/', methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        if request.form['activity_type'] == "Event":
            event = Event(request.form['title'],
                          request.form['slug'],
                          request.form['description'],
                          request.form['body'])
            db.session.add(event)
            db.session.commit()
            flash('Event Upload Successful!')
            return redirect(url_for('general.events'))
        elif request.form['activity_type'] == "Workshop":
            workshop = Workshop(request.form['title'],
                                request.form['slug'],
                                request.form['description'],
                                request.form['body'])
            db.session.add(workshop)
            db.session.commit()
            flash('Workshop Upload Successful!')
            return redirect(url_for('general.workshops'))
        else:
            flash("Activity type unknown!")
    return html_minify(render_template('admin/activities.html'))


@admin.route('/notifications/', methods=['GET', 'POST'])
def notifications():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Sleepy much? Select a proper file first.')
        file = request.files['file']
        if not file.filename:
            flash('Sleepy much? Select a proper file first.')
            return redirect(request.url)
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            flash('Notification uploaded successfully')
            return redirect(url_for('.notifications'))
    return html_minify(render_template('admin/notifications.html'))


@admin.route('/registrations/')
def registrations():
    users = User.query.all()
    return html_minify(
        render_template('admin/registrations.html', users=users))


@admin.route('/registrations/<int:id>/')
def view_registration(id):
    user = User.query.get(id)
    return html_minify(
        render_template('admin/view-registration.html', user=user))
