from flask_restx import Resource, Namespace
from application.database import db
from application import models

directors_ns = Namespace('directors')
director_schema = models.Director()
directors_schema = models.Director(many=True)

@directors_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id):
        director = db.session.query(models.Director).filter(models.Director.id == director_id).first()
        if director is None:
            return None, 404
        return director_schema.dump(director), 200

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(models.Director).all()
        return directors_schema.dump(directors), 200