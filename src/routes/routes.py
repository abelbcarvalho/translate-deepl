from flask import Blueprint, request

from src.controllers.controller_text import ControllerText
from src.controllers.controller_word import ControllerWord


deepl = Blueprint("deepl", __name__)

controller_word = ControllerWord()
controller_text = ControllerText()


@deepl.route("/", methods=["GET"])
def index():
    return {"hello": "world"}


# word model routes


@deepl.route("/translate/word", methods=["POST"])
async def translate_word():
    body = request.json

    return await controller_word.translate_word(body)


# text model routes


@deepl.route("/translate/text", methods=["POST"])
async def translate_text():
    body = request.json

    return await controller_text.translate_text(body)
