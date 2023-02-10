# -*- coding: utf-8 -*-
from flask import Flask
from flask_restx import Api
from HW_18.config import Config
from HW_18.setup_db import db
from HW_18.views.movies import movie_ns
from HW_18.views.genres import genre_ns
from HW_18.views.directors import director_ns


def create_app(config_object: Config):
    """Создание приложения"""
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    """Конфигурация приложения"""
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    register_extensions(app)
    app.run()
