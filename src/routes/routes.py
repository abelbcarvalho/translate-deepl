from flask import Blueprint, request

from src.controllers.controller_word import ControllerWord


deepl = Blueprint("deepl", __name__)

controller_word = ControllerWord()


@deepl.route("/", methods=["GET"])
def index():
    return {"hello": "world"}


@deepl.route("/translate/word", methods=["POST"])
async def translate_word():
    body = request.json

    return await controller_word.translate_word(body)
