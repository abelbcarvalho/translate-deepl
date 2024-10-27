from pydantic import ValidationError

from src.exceptions.exceptions import SuperException
from src.models.word import WordModel
from src.services.service_word import ServiceWord
from src.utilities.checkers.check_body import check_body
from src.utilities.response.response import response


class ControllerWord:
    def __init__(self):
        self.service_word = ServiceWord()

    async def translate_word(self, body: any):
        try:
            word: WordModel = await check_body(body, WordModel)

            data = await self.service_word.translate_word(word)

            return await response(dict(word=data))
        except SuperException as se:
            return await response(
                body=dict(error=se.message),
                code=se.code
            )
