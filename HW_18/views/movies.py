# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask_restx import Resource, Namespace
from HW_18.dao.model.movie import MovieSchema
from HW_18.implemented import movie_service
from flask import request

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route("/<int:m_id>")
class MovieView(Resource):
    def get(self, m_id: int):
        return movie_schema.dump(movie_service.get_one(m_id)), 200

    def put(self, m_id: int):
        req_json = request.json
        req_json["id"] = m_id
        movie_service.update(req_json)
        return '', 201

    def patch(self, m_id: int):
        req_json = request.json
        req_json["id"] = m_id
        movie_service.update_partial(req_json)
        return '', 204

    def delete(self, m_id: int):
        movie_service.delete(m_id)
        return '', 204
