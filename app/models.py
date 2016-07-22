from app import db, bcrypt
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin


# -----------------------------------------------------------------------------------------
#     'users' table
# -----------------------------------------------------------------------------------------
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=False, unique=True)
    username = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(128))
    _password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)
    cell = db.Column(db.String(64))
    gender = db.Column(db.String(6))
    college = db.Column(db.String(128))
    batch = db.Column(db.Integer)
    branch = db.Column(db.String(64))
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    def __repr__(self):
        return '<User %r>' % self.name


# -----------------------------------------------------------------------------------------
#     'notifications' table
# -----------------------------------------------------------------------------------------

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())

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
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())

    def __init__(self, title, slug, description, body):
        self.title = title
        self.slug = slug
        self.description = description
        self.body = body


# -----------------------------------------------------------------------------------------
#     'Event Registrations' table
# -----------------------------------------------------------------------------------------

class EventRegistration(db.Model):
    __tablename__ = "event_registrations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())
    __table_args__ = (
        UniqueConstraint('user_id', 'event_id'),
    )

    def __init__(self, user_id, event_id):
        self.user_id = user_id
        self.event_id = event_id


# -------------------------------------------------------------------------------------------
#      'Workshops' table
# -------------------------------------------------------------------------------------------

class Workshop(db.Model):
    __tablename__ = 'workshops'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(512))
    slug = db.Column(db.String(255), unique=True)
    body = db.Column(db.String(20480))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())

    def __init__(self, title, slug, description, body):
        self.title = title
        self.description = description
        self.slug = slug
        self.body = body


# --------------------------------------------------------------------------------------------
#       'Workshop' Registrations table
# --------------------------------------------------------------------------------------------

class WorkshopRegistration(db.Model):
    __tablename__ = "workshop_registrations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    workshop_id = db.Column(db.Integer, db.ForeignKey("workshops.id"))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())
    __table_args__ = (
        UniqueConstraint('user_id', 'workshop_id'),
    )

    def __init__(self, user_id, workshop_id):
        self.user_id = user_id
        self.workshop_id = workshop_id
