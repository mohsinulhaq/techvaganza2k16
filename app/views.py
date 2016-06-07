from flask import render_template, flash, request
from app import app, db
from app.models import User
from app.forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy(app)

# -----------------------------------------------------------------------------------------
#     Admin Routes
# -----------------------------------------------------------------------------------------

@app.route('/')
@app.route('/admin/')
def adminDashboard():
    flash('laenchaaaaa')
    flash('gupnaaa')
    return render_template('admin/admin-dashboard.html')


@app.route('/admin/events/')
def adminDashboardEvents():
    return render_template('admin/events.html')


@app.route('/admin/notifications/')
def adminDashboardNotifications():
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
                    request.form['first_name'],
                    request.form['last_name'],
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
