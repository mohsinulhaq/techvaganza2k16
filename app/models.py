from app import db
from wtforms import Form, BooleanField, TextField, PasswordField, validators

# -----------------------------------------------------------------------------------------
#     'users' table
# -----------------------------------------------------------------------------------------

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username=db.Column(db.String(255), unique = True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)
    cell = db.Column(db.String(255))
    gender= db.Column(db.String(6))
    college = db.Column(db.String(255))
    batch = db.Column(db.Integer())
    branch = db.Column(db.String(255))

    def __init__(self, username, password, first_name, last_name, email, cell, gender, college, batch, branch):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cell = cell
        self.gender = gender
        self.college = college
        self.batch = batch
        self.branch = branch
