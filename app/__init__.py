from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Create an Instance of Flask
app = Flask(__name__)

#Include config from config.py
app.config.from_object('config')
app.secret_key = "FsdfswsskfhAOCABSKJFNAKdfbgfgaJCNWOACNQWIKXNxbcqcnskjcnIUH287R2YRHI2132FVJBKVBJSVB"

#Create an instance of SQLAclhemy
db = SQLAlchemy(app)
from app import views, models
