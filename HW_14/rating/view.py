from flask import Blueprint
from HW_14 import utils

rating_blueprint = Blueprint("rating_blueprint", __name__)


@rating_blueprint.route("/<rating>")
def search_rating(rating):
    """Вьющка на поиск фильма через рейтинг get запрос"""
    return utils.find_movie_by_age_limits(rating)

