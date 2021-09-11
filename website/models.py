from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    game_type = db.Column(db.String(100)) # FIXME: this would be better as an enum, but I have no idea how to implement
    num_people = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    lat = db.Column(db.Float())
    lng = db.Column(db.Float())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # one to many relationship between user and his/her games

    # user.id calls the id field of the user object

# -- Add in validation

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    games = db.relationship('Game') #reference to Note - specific to one to many rel
