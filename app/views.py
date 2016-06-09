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


@app.route('/admin/notifications/', methods = ['GET', 'POST'])
def adminDashboardNotifications():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('Upload a proper format you twat!')
        file = request.files['file']
        # if user does not select file, browser also submits a empty part without filename
        if file.filename == '':
            flash('Sleepy much? Select a file first.')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
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
