from flask import Flask
from application.config import Config
from application.database import db
from flask_restx import Api
from application.views.movies import movies_ns
from application.views.genres import genres_ns
from application.views.directors import directors_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    return app

def configure_app(app: Flask):
    db.init_app(app)
    db.create_all()
    api = Api(app, prefix='/api', doc='/docs')
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)

if __name__ == '__main__':
    app_ = create_app()
    configure_app(app_)
    app_.run()
