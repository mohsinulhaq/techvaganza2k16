# for creating json responses
import json
from flask import jsonify, abort, make_response, request
from app import app, db, views, models
from app.models import Event, EventRegistration, User


# converts a SQLAlchemy result row into a standard python dictionary
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d


# Returns the error as a json response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    res = Event.query.filter_by(id=user_id).all()
    users = []
    if len(res) == 0:
        return jsonify(users)
    else:
        for user in res:
            events.append(row2dict(user))
        return jsonify(users)


@app.route("/api/users", methods=["POST"])
def insert_user():
    if not request.json or not 'enroll' in request.json or not 'password' in request.json\
    or not 'college' in request.json or not 'email' in request.json:
        abort(400)

    password = request.json.get('password', '')
    name = request.json.get('name','')
    email = request.json.get('email', '')
    cell = request.json.get('cell', '')
    gender = request.json.get('gender', '')
    college = request.json['college']
    batch = request.json.get('batch', '')
    branch = request.json.get('branch', '')

    try:
        user = User(password, name, email, cell, gender, college, batch, branch)
        db.session.add(user)
        db.session.commit()
        return jsonify({"status": "success"}), 200
    except:
        return jsonify({"status": "failure"})


# PUT method to modify the details of a User
@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
        if 'password' in request.json:
            item = User.query.filter_by(id=user_id).first()

            if item is None:
                abort(404)

            item.password = request.json['password']
            db.session.commit()

        if 'name' in request.json:
            item = User.query.filter_by(id=user_id).first()
            item.name = request.json['name']
            db.session.commit()

        if 'email' in request.json:
            item = User.query.filter_by(id=user_id).first()
            item.email = request.json['email']
            db.session.commit()

        if 'cell' in request.json:
            item = User.query.filter_by(id=user_id).first()
            item.cell = request.json['cell']
            db.session.commit()

        if 'gender' in request.json:
            item = User.query.filter_by(id=user_id).first()
            item.gender = request.json['gender']
            db.session.commit()

        if 'college' in request.json:
            item = User.query.filter_by(id=user_id).first()
            item.college = request.json['college']
            db.session.commit()

        if 'batch' in request.json:
            item = User.query.filter_by(id=user_id).first()
            item.batch = request.json['batch']
            db.session.commit()

        if 'branch' in request.json:
            item = User.query.filter_by(id=user_id).first()
            item.branch = request.json['branch']
            db.session.commit()

        return jsonify({"status": "success"}), 200


# GET method to retrieve all the events registered
@app.route("/api/events", methods=["GET"])
def get_events():
    res = Event.query.all()
    events = []
    if len(res) == 0:
        return jsonify(events)
    else:
        for event in res:
            events.append(row2dict(event))
        return jsonify(events)


# GET method to retrieve a particular event given its id
@app.route("/api/events/<int:event_id>")
def get_event(event_id):
    res = Event.query.filter_by(id=event_id).all()
    events = []
    if len(res) == 0:
        return jsonify(events)
    else:
        for event in res:
            events.append(row2dict(event))
        return jsonify(events)


# add an event using the POST method
@app.route("/api/events", methods=["POST"])
def create_event():
    if not request.json or not 'title' in request.json or not 'slug' in request.json:
        abort(400)
    event = Event(request.json['title'],
                  request.json['slug'],
                  request.json.get('description', ''),
                  request.json.get('body', ''))
    db.session.add(event)
    db.session.commit()
    return jsonify({'status': 'success'}), 201


# update an event using the PUT method
@app.route("/api/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    if 'title' in request.json:
        item = Event.query.filter_by(id=event_id).first()

        if item is None:
            abort(404)

        item.title = request.json['title']
        db.session.commit()

    if 'description' in request.json:
        item = Event.query.filter_by(id=event_id).first()
        item.description = request.json['description']
        db.session.commit()

    if 'slug' in request.json:
        item = Event.query.filter_by(id=event_id).first()
        item.slug = request.json['slug']
        db.session.commit()

    if 'body' in request.json:
        item = Event.query.filter_by(id=event_id).first()
        item.body = request.json['body']
        db.session.commit()

    return jsonify({"status": "success"}), 200


# DELETE method to delete a particular event
@app.route("/api/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    try:
        Event.query.filter_by(id=event_id).delete()
        db.session.commit()
        return jsonify({"status": "success"}), 200
    except:
        return jsonify({"status": "failed"})


# GET method to retrieve all the registrations being done for events by users
@app.route("/api/event_registrations", methods=["GET"])
def get_event_registrations():
    res = EventRegistration.query.all()
    registrations = []

    if len(res) == 0:
        abort(404)
    else:
        for registration in res:
            registrations.append(row2dict(registration))
        return jsonify(registrations)


# GET method to retrieve a event_registration details, given its id
@app.route("/api/event_registrations/<int:event_registration_id>", methods=["GET"])
def get_event_registration(event_registration_id):
    res = EventRegistration.query.filter_by(id=event_registration_id).all()
    registrations = []
    if len(res) == 0:
        return jsonify(registrations)
    else:
        for registration in res:
            registrations.append(row2dict(registration))
        return jsonify(registrations)


# POST method to insert an event registration
@app.route("/api/event_registrations", methods=["POST"])
def insert_event_registration():
    if not request.json or not 'user_id' in request.json or not 'event_id' in request.json:
        abort(400)
    registration = EventRegistration(request.json['user_id'],
                                     request.json['event_id'])
    db.session.add(registration)
    db.session.commit()
    return jsonify({"status": "Event Registration Added"}), 200


# DELETE method to delete and event registration
@app.route("/api/event_registrations/<int:event_registration_id>", methods=["DELETE"])
def remove_event_registration(event_registration_id):
    try:
        EventRegistration.query.filter_by(id=event_registration_id).delete()
        db.session.commit()
        return jsonify({"status": "success"}), 200
    except:
        return jsonify({"status": "failed"})
