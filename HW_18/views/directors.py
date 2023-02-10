from flask import request
from flask_restx import Resource, Namespace
from HW_18.dao.model.director import DirectorSchema
from HW_18.implemented import director_service

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return '', 201


@director_ns.route("/<int:d_id>")
class DirectorView(Resource):
    def get(self, d_id: int):
        return director_schema.dump(director_service.get_one(d_id)), 200

    def put(self, d_id: int):
        req_json = request.json
        req_json["id"] = d_id
        director_service.update(req_json)
        return '', 204

    def patch(self, d_id: int):
        req_json = request.json
        req_json["id"] = d_id
        director_service.update_partial(req_json)
        return '', 204

    def delete(self, d_id: int):
        director_service.delete(d_id)
        return '', 204
