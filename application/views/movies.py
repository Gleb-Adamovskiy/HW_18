from flask_restx import Resource, Namespace
from flask import request
from application.database import db
from application import models

movies_ns = Namespace('movies')
movie_schema = models.Movie()
movies_schema = models.Movie(many=True)

@movies_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()
        if movie is None:
            return None, 404
        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        db.session.query(models.Movie).filter(models.Movie.id == movie_id).update(request.json)
        db.session.commit()
        return None, 200

    def delete(self, movie_id):
        db.session.query(models.Movie).filter(models.Movie.id == movie_id).delete()


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies_query = db.session.query(models.Movie).all()
        args = request.args
        director_id = args.get('director_id')
        if director_id is not None:
            movies_query = movies_query.filter(models.Movie.director_id == director_id)
        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies_query = movies_query.filter(models.Movie.genre_id == genre_id)
        movies = movies_query.all()
        return movies_schema.dump(movies), 200

    def post(self):
        movie = movie_schema.load(request.json)
        db.session.add(models.Movie(**movie))
        db.session.commit()
        return None, 201
