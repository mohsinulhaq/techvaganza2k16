from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
from flask_assets import Bundle, Environment
from app import app

assets = Environment(app)

bundles = {
    'landing_css': Bundle(
        'css/index.css',
        'css/font-awesome.min.css',
        'css/comfortaa.css',
        'css/lato.css',
        filters='cssmin',
        output='gen/landing_styles.css'),

    'landing_js': Bundle(
        'js/jquery.min.js',
        'js/index.js',
        'js/skrollr.min.js',
        'js/skrollr.menu.min.js',
        filters='jsmin',
        output='gen/landing_scripts.js'),

    'css': Bundle(
        'css/bootstrap.min.css',
        'css/component.css',
        'css/animate.min.css',
        'css/ct-paper.css',
        'css/lato.css',
        'css/examples.css',
        'css/font-awesome.min.css',
        'css/montserrat.css',
        filters='cssmin',
        output='gen/styles.css'),

    'js': Bundle(
        'js/jquery.min.js',
        'js/index.js',
        'js/jquery-ui-1.10.4.custom.min.js',
        'js/bootstrap.min.js',
        'js/classie.js',
        'js/ct-paper.js',
        filters='jsmin',
        output='gen/scripts.js'),

}

assets.register(bundles)


def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers[
            'Cache-Control'] = 'no-store, no-cache, must-revalidate,' \
                               ' post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return update_wrapper(no_cache, view)
