from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

# Create an Instance of Flask
app = Flask(__name__)

# Include config from config.py
app.config.from_object('config')

# Flask Debug Toolbar
toolbar = DebugToolbarExtension(app)

# Create an instance of SQLAlchemy
db = SQLAlchemy(app)
from app import views, models, api
