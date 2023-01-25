from flask import Blueprint, render_template, request
from HW10 import functions

upload_blueprint = Blueprint('upload_blueprint', __name__, template_folder="templates")


@upload_blueprint.route("/", methods=['POST'])
def main_page():
    picture = request.files.get('picture')
    text = request.form.get('content')
    picture.save(f"./uploads/images/{picture.filename}")
    functions.add_to_json(text, picture)
    return render_template('post_uploaded.html', text=text, picture=picture.filename)
