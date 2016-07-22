from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Create an Instance of Flask
app = Flask(__name__)

# Include config from config.py
app.config.from_object('config')

# bcrypt encryption module
bcrypt = Bcrypt(app)

# Create an instance of SQLAlchemy
db = SQLAlchemy(app)

from views import admin, general, housekeeping, authentication, api

# register blueprints
app.register_blueprint(admin.admin, url_prefix='/admin')
app.register_blueprint(api.api, url_prefix='/api')
app.register_blueprint(general.general)
app.register_blueprint(housekeeping.housekeeping)
app.register_blueprint(authentication.authentication)
