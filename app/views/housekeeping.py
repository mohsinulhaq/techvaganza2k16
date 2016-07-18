from flask import Blueprint, render_template, abort, request, flash
from app import app
from htmlmin.minify import html_minify
from flask_mail import Mail, Message
from app.requests import ContactRequest

housekeeping = Blueprint('housekeeping', __name__)


@housekeeping.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if "fuck" in request.form['msg']:
            flash("Sorry, we don't accept feedback from trolls")
        else:
            validate, errors = ContactRequest().validate(request.form)
            if validate:
                html = render_template('_snippets/_feedback.html',
                                       msg=request.form['msg'],
                                       sender=request.form['email']
                                       )
                msg = Message(subject="FEEDBACK | Techvaganza 2k16",
                              sender=request.form['email'],
                              recipients=['techvaganza2k16@gmail.com'],
                              html=html
                              )
                Mail(app).send(msg)
                flash("Mail sent, thanks for feedback!")
            else:
                # TODO: Implements these in bootstrap/paperkit as individual form inputs field errors.
                for error in errors:
                    flash(errors[error])
    return html_minify(render_template('housekeeping/contact.html'))


@housekeeping.route('/<page>/')
def index(page):
    """
    For handling pages: about, sponsors, our team etc.
    """
    try:
        return html_minify(render_template('housekeeping/' + page + '.html'))
    except Exception:
        abort(404)
