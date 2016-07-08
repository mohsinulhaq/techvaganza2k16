from flask import Blueprint, render_template
from htmlmin.minify import html_minify

user = Blueprint('user', __name__)


@user.route('/user/', methods=['GET'])
def index():
    return html_minify(render_template('users/user.html'))