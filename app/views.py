import os
from flask import render_template, flash, request, redirect
from app import app, db
from app.models import User
from app.forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename


# -----------------------------------------------------------------------------------------
#     Admin Routes
# -----------------------------------------------------------------------------------------

@app.route('/')
@app.route('/admin/')
def adminDashboard():
    return render_template('admin/admin-dashboard.html')


@app.route('/admin/events/')
def adminDashboardEvents():
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
    return render_template('admin/registrations.html')


# -----------------------------------------------------------------------------------------
#     General Routes
# -----------------------------------------------------------------------------------------

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
