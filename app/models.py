from app import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
# -----------------------------------------------------------------------------------------
#     'users' table
# -----------------------------------------------------------------------------------------


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    _password = db.Column(db.String(128))
    email = db.Column(db.String(255), unique=True)
    cell = db.Column(db.String(255))
    gender = db.Column(db.String(6))
    college = db.Column(db.String(255))
    batch = db.Column(db.Integer)
    branch = db.Column(db.String(255))
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.name


class PasswordReset(db.Model):
    __tablename__ = 'password_resets'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    token = db.Column(db.String(128))

    def __init__(self, email, token):
        self.email = email
        self.token = token


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

    def __init__(self, user_id, workshop_id):
        self.user_id = user_id
        self.workshop_id = workshop_id
