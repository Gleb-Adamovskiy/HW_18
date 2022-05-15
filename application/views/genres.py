from flask_restx import Resource, Namespace
from application.database import db
from application import models

genres_ns = Namespace('genres')
genre_schema = models.Genre()
genres_schema = models.Genre(many=True)

@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = db.session.query(models.Genre).filter(models.Genre.id == genre_id).first()
        if genre is None:
            return None, 404
        return genre_schema.dump(genre), 200


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = db.session.query(models.Genre).all()
        return genres_schema.dump(genres), 200