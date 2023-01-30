from flask import Blueprint
from HW_14 import utils

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/<title>")
def search_title(title):
    """Вьющка на поиск фильма по названию через get запрос"""
    return utils.find_movie_by_name(title)


@search_blueprint.route("/<int:from_>/to/<int:to_>")
def search_years(from_, to_):
    """Вьющка на поиск фильма в диапазоне лет get запрос"""
    return utils.find_movie_by_years(from_, to_)




