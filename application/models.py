from application.database import db
from marshmallow import Schema, fields

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

class Movie(BaseModel):
    __tablename__ = 'movies'
    title = db.Column(db.String(255))
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))

class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int(required=True)
    rating = fields.Int()

class Genre(BaseModel):
    __tablename__ = 'genres'
    name = db.Column(db.String(255))

class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class Director(BaseModel):
    __tablename__ = 'directors'
    name = db.Column(db.String(255))

class DirectorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

