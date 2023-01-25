from flask import render_template, Blueprint

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/")
def main_page():
    return render_template("post_form.html")

