from flask import render_template, Blueprint, request
from HW10 import functions

search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


@search_blueprint.route("/")
def search_page():
    s = request.args['s']
    return render_template("post_list.html", posts=functions.find_items(s), word=s)
