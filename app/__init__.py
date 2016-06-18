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

# Flask Debug Toolbar
toolbar = DebugToolbarExtension(app)

<<<<<<< HEAD
# Create an instance of SQLAlchemy
db = SQLAlchemy(app)
from app import views, models, api
=======
from app import views, models
>>>>>>> e4cd32b7a318439a7aef31654a3cd6765d293c86
