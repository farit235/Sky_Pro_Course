from flask import Flask
from search.view import search_blueprint
from rating.view import rating_blueprint
from genre.view import genre_blueprint


app = Flask(__name__)

app.register_blueprint(search_blueprint, url_prefix="/movie/")
app.register_blueprint(rating_blueprint, url_prefix="/rating/")
app.register_blueprint(genre_blueprint, url_prefix="/genre/")

app.run()
