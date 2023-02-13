from flask import request
from flask_restx import Resource, Namespace
from HW_19.dao.model.user import UserSchema
from HW_19.implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        return UserSchema(many=True).dump(user_service.get_all()), 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/movies/{user.id}"}


@user_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        res = UserSchema().dump(user)
        return res, 200

    def put(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
