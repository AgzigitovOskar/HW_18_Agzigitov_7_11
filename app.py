from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns


def create_app(config_object):
    """
        Функция создания основного объекта app
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """
        Функция подключения расширений
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)


if __name__ == '__main__':
    config = Config()
    app = create_app(config)
    app.run(host="localhost", port=10005)
