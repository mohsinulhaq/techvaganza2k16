from app import db
from wtforms import Form, BooleanField, TextField, PasswordField, validators

class User(db.Model):
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
    accomodation = db.Column(db.Boolean(255))
    time = db.Column(db.DateTime())
    special = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    def __str__(self):
        return "<username :%s , first_name :%s , last_name :%s , email :%s , cell :%s , gender :%s , college :%s , batch :%s , branch :%s , accomodation :%s , time :%s , special :%s , active :%s , confirmed_at :%s , roles :%s , events:%s ,organises:%s >"%(self.username,self.first_name,self.last_name,self.email,self.cell,self.gender,self.college,self.batch,self.branch,self.accomodation,self.time,self.special,self.active,self.confirmed_at,self.roles,self.events,self.organises)
    def __repr__(self):
        return "<username :%s , first_name :%s , last_name :%s , email :%s , cell :%s , gender :%s , college :%s , batch :%s , branch :%s , accomodation :%s , time :%s , special :%s , active :%s , confirmed_at :%s , roles :%s , events:%s ,organises:%s>"%(self.username,self.first_name,self.last_name,self.email,self.cell,self.gender,self.college,self.batch,self.branch,self.accomodation,self.time,self.special,self.active,self.confirmed_at,self.roles,self.events,self.organises)
