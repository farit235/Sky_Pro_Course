from HW_18.setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    """Модель жанра"""
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreSchema(Schema):
    """ Схема для сериализации данных жанров"""
    id = fields.Int()
    name = fields.String()
