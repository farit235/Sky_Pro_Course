from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from search.search import search_blueprint
from loader.loader import loader_blueprint
from upload.upload import upload_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_blueprint, url_prefix="/")
app.register_blueprint(search_blueprint, url_prefix="/search/")
app.register_blueprint(loader_blueprint, url_prefix="/loader/")
app.register_blueprint(upload_blueprint, url_prefix="/upload/")


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

