from HW_18.setup_db import db
from marshmallow import Schema, fields

class Director(db.Model):
    """Модель режиссера"""
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class DirectorSchema(Schema):
    """ Схема для сериализации данных режиссера"""
    id = fields.Int()
    name = fields.String()
