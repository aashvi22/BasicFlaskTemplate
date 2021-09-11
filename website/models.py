from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):#(things it's inheriting from)
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #one to many relationship between user and his/her notes
    #user.id calls the id field of the user object

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #reference to Note - specific to one to many rel
