# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)
from marshmallow import Schema, fields
from HW_18.setup_db import db


class Movie(db.Model):
    """Модель кино"""
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.String)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship('Genre')
    director = db.relationship('Director')


class MovieSchema(Schema):
    """ Схема для сериализации данных кино"""
    id = fields.Int()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Int()
    rating = fields.String()
    genre_id = fields.Int()
    director_id = fields.Int()
