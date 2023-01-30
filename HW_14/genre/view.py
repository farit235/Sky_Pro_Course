from flask import Blueprint
from HW_14 import utils

genre_blueprint = Blueprint("genre_blueprint", __name__)


@genre_blueprint.route("/<genre>")
def search_genre(genre):
    """Вьющка на поиск фильма через жанр get запрос"""
    return utils.find_movie_by_genre(genre)
