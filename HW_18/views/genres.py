from flask_restx import Resource, Namespace
from flask import request
from HW_18.dao.model.genre import GenreSchema
from HW_18.implemented import genre_service

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return genre_schema.dump(genre_service.get_all()), 200

    def post(self):
        data = request.json
        genre_service.create(data)
        return '', 201


@genre_ns.route("/<int:g_id>")
class DirectorView(Resource):
    def get(self, g_id: int):
        return genres_schema.dump(genre_service.get_one(g_id)), 200

    def put(self, g_id: int):
        req_json = request.json
        req_json["id"] = g_id
        genre_service.update(req_json)
        return '', 201

    def patch(self, g_id: int):
        req_json = request.json
        req_json["id"] = g_id
        genre_service.update_partial(req_json)
        return '', 204

    def delete(self, g_id: int):
        genre_service.delete(g_id)
        return '', 204
