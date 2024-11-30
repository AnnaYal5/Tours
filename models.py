from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class Tour(db.Model):
    __tablename__ = "tour"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(450), nullable=False)
    departure_id = db.Column(db.Integer, db.ForeignKey("departure.id"))
    picture = db.Column(db.String(550), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(150), nullable=False)
    nights = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(20), nullable=False)


class Departure(db.Model):
    __tablename__ = "departure"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    tours = db.relationship("Tour", backref="departure", lazy=True)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    u_email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)



