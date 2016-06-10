from app import db
from wtforms import Form, BooleanField, TextField, PasswordField, validators

# -----------------------------------------------------------------------------------------
#     'users' table
# -----------------------------------------------------------------------------------------

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)
    cell = db.Column(db.String(255))
    gender= db.Column(db.String(6))
    college = db.Column(db.String(255))
    batch = db.Column(db.Integer())
    branch = db.Column(db.String(255))

    def __init__(self, password, name, email, cell, gender, college, batch, branch):
        self.password = password
        self.name = name
        self.email = email
        self.cell = cell
        self.gender = gender
        self.college = college
        self.batch = batch
        self.branch = branch


# -----------------------------------------------------------------------------------------
#     'notifications' table
# -----------------------------------------------------------------------------------------

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(255))

    def __init__(self, filename):
        self.filename = filename
