from app import db
from wtforms import Form, BooleanField, TextField, PasswordField, validators

# -----------------------------------------------------------------------------------------
#     'users' table
# -----------------------------------------------------------------------------------------


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    cell = db.Column(db.String(255))
    gender = db.Column(db.String(6))
    college = db.Column(db.String(255))
    batch = db.Column(db.Integer())
    branch = db.Column(db.String(255))

    def __init__(self, password, name, email, cell, gender, college, batch,
                 branch):
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

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))

    def __init__(self, filename):
        self.filename = filename


# -----------------------------------------------------------------------------------------
#     'events' table
# -----------------------------------------------------------------------------------------

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(512))
    slug = db.Column(db.String(255), unique=True)
    body = db.Column(db.String(20480))

    def __init__(self, title, slug, description, body):
        self.title = title
        self.description = description
        self.slug = slug
        self.body = body

# -----------------------------------------------------------------------------------------
#     'Event Registrations' table
# -----------------------------------------------------------------------------------------

class Event_registration(db.Model):
    __tablename__ = "event_registrations"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))

    def __init__(self, user_id,event_id):
        self.user_id = user_id
        self.event_id = event_id
