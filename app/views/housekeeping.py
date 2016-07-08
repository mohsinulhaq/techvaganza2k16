from flask import Blueprint, render_template, abort
from htmlmin.minify import html_minify

housekeeping = Blueprint('housekeeping', __name__)


@housekeeping.route('/<page>/')
def index(page):
    """
    For handling pages: about, contact, sponsors, our team.
    """
    try:
        return html_minify(render_template('housekeeping/' + page + '.html'))
    except Exception:
        abort(404)
