from flask import Blueprint


deepl = Blueprint("deepl", __name__)


@deepl.route("/", methods=["GET"])
def index():
    return {"hello": "world"}
