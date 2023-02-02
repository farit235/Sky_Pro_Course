from flask import Flask
from main.view import main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint, url_prefix="/")

app.run()
