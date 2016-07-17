from flask import Blueprint, render_template, flash, request, url_for, redirect, abort
from app import app, db
from app.models import User
from flask_login import LoginManager, login_user, logout_user
from htmlmin.minify import html_minify
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

authentication = Blueprint('authentication', __name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '.login'
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])


@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.id == userid).first()


@authentication.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(password=request.form['password'],
                    name=request.form['name'],
                    email=request.form['email'],
                    cell=request.form['cell'],
                    gender=request.form['gender'],
                    college=request.form['college'],
                    batch=request.form['batch'],
                    branch=request.form['branch'])
        user.email_confirmed = False
        db.session.add(user)
        db.session.commit()

        subject = "Confirm your email"

        token = ts.dumps(request.form['email'], salt='email-confirm-key')

        confirm_url = url_for(
            '.confirm_email',
            token=token,
            _external=True)

        html = render_template(
            '_snippets/_activate.html',
            confirm_url=confirm_url)

        msg = Message(subject=subject,
                      sender='techvaganza2k16@gmail.com',
                      recipients=[request.form['email']],
                      html=html
                      )

        Mail(app).send(msg)

        flash('Registration Successful! Please confirm your email within 24 hours.')

        return redirect(url_for('.login'))
    return html_minify(render_template('register.html'))


@authentication.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token, salt="email-confirm-key", max_age=86400)
    except:
        abort(404)

    user = User.query.filter_by(email=email).first_or_404()
    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()
    flash('Congratulations! Your email has been confirmed!')
    return redirect(url_for('.login'))


@authentication.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return html_minify(render_template('login.html'))
    email = request.form['email']
    password = request.form['password']
    registered_user = User.query.filter_by(email=email).first()
    if registered_user is None:
        flash('Username or Password is invalid')
        return redirect(url_for('.login'))

    if not registered_user.is_correct_password(password):
        flash('Username or Password is invalid')
        return redirect(url_for('.login'))

    if not registered_user.email_confirmed:
        flash('Please confirm your email first.')
        return redirect(url_for('.login'))

    remember_me = True if 'remember-me' in request.form else False
    login_user(registered_user, remember=remember_me)
    return redirect(url_for('general.user'))


@authentication.route('/reset-password/', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            subject = "Techvaganza 2k16 : Password Reset"

            token = ts.dumps(request.form['email'], salt='reset-key')

            reset_url = url_for(
                '.reset_with_token',
                token=token,
                _external=True)

            html = render_template(
                '_snippets/_reset.html',
                reset_url=reset_url)

            msg = Message(subject=subject,
                          sender='techvaganza2k16@gmail.com',
                          recipients=[request.form['email']],
                          html=html
                          )

            Mail(app).send(msg)
            flash("Password reset email sent, check your mail!")
        else:
            flash("User doesn't exist!")
    return html_minify(render_template('forgot-password.html'))


@authentication.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_with_token(token):
    try:
        email = ts.loads(token, salt="reset-key", max_age=86400)
    except:
        abort(404)
    if request.method == 'POST':
        user = User.query.filter_by(email=email).first_or_404()
        if request.form['password'] == request.form['confirm_password']:
            user.password = request.form['password']
            flash("Password changed successfully!")
            db.session.commit()
            return redirect(url_for('.login'))
        else:
            flash("Passwords don't match!")

    return render_template('reset-password.html')


@authentication.route('/logout/', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('general.index'))
