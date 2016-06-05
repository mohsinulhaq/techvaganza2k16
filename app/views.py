from flask import render_template, flash, request
from app import app


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
    if request.method == 'GET':
        return render_template('register.html')
    else:
        return 'Laaenchaa'
