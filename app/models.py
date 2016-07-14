from app import db


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
    batch = db.Column(db.Integer)
    branch = db.Column(db.String(255))
    email_confirmed = db.Column(db.Boolean, default=False, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())

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


# -----------------------------------------------------------------------------------------
#     'password_resets' table
# -----------------------------------------------------------------------------------------

class PasswordReset(db.Model):
    __tablename__ = 'password_resets'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    token = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(),
                           onupdate=db.func.now())

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

    def __init__(self, user_id, workshop_id):
        self.user_id = user_id
        self.workshop_id = workshop_id
