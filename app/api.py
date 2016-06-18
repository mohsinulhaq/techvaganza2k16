#for creating json responses
from flask import jsonify, abort, make_response, request
from app import app, db, views, models
from models import Event, Event_registration
#converts a SQLAlchemy result row into a standard python dictionary
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

#Returns the error as a json response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


#GET method to retrieve all the events registered
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


# add an event using the POST method
@app.route("/api/events",methods=["POST"])
def create_event():
    if not request.json or not 'title' in request.json or not 'slug' in request.json:
        abort(400)
    event = Event(request.json['title'],request.json['slug'],request.json.get('description',''),request.json.get('body',''))
    db.session.add(event)
    db.session.commit();
    return jsonify({'status':'success'}), 201



#udate an event using the PUT method


#GET method to retrieve a particular event given its id
@app.route("/api/events/<int:event_id>")
def get_event(event_id):
    res = Event.query.filter_by(id = event_id).all();
    events = []
    if len(res) == 0:
        return jsonify(events)
    else:
        for event in res:
            events.append(row2dict(event))
        return jsonify(events)

#GET method to retrieve all the registrations that are being done for events by
#users
@app.route("/api/event_registrations")
def get_event_registrations():
    res = Event_registration.query.all()
    registrations = []

    if len(res) == 0:
        abort(404)
    else:
        for registration in res:
            registrations.append(row2dict(registration))
        return jsonify(registrations)

#GET method to retrieve a event_registration details, given its id
@app.route("/api/event_registrations/<int:event_registration_id>")
def get_event_registration(event_registration_id):
    res = Event_registration.query.filter_by(id = event_registration_id).all()
    registrations = []
    if len(res) == 0:
        return jsonify(registrations)
    else:
        for registration in res:
            registrations.append(row2dict(registration))
        return jsonify(registrations)

#more methods coming soon.....
