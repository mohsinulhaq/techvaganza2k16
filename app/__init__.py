from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_assets import Environment, Bundle

# Create an Instance of Flask
app = Flask(__name__)

# Include config from config.py
app.config.from_object('config')

# Create an instance of SQLAlchemy
db = SQLAlchemy(app)

# Flask Debug Toolbar
toolbar = DebugToolbarExtension(app)

# Bundle css and js into minified forms
assets = Environment(app)
bundles = {
    'css': Bundle(
        'css/index.css',
        'css/font-awesome.min.css',
        'css/comfortaa.css',
        'css/lato.css',
        filters='cssmin',
        output='gen/styles.css'),

    'js': Bundle(
        'js/jquery.min.js',
        'js/index.js',
        'js/skrollr.min.js',
        'js/skrollr.menu.min.js',
        filters='jsmin',
        output='gen/scripts.js'),
}
assets.register(bundles)

from views import admin, general, housekeeping

# register blueprints
app.register_blueprint(admin.admin, url_prefix="/admin")
app.register_blueprint(general.general, url_prefix="")
app.register_blueprint(housekeeping.housekeeping, url_prefix="")
