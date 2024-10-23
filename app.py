from os import environ

from flask import Flask

from src.routes.routes import deepl

from dotenv import load_dotenv


load_dotenv()

PORT = int(environ.get("PORT", 5000))
DEBUG = eval(environ.get("DEBUG", True))


app = Flask(__name__)

app.register_blueprint(deepl, url_prefix="/api/v1/deepl")


if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)
