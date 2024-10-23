from os import environ
from typing import List

from deepl import Translator, TextResult

from src.models.translate import Translate


class DeepLTranslate:
    translator: Translator

    def __init__(self):
        auth_key = environ["DEEPL_AUTH_KEY"]
        self.translator = Translator(auth_key)

    async def translate(self, translate: Translate) -> TextResult | List[TextResult]:
        text_translated = self.translator.translate_text(**translate.model_dump())

        return text_translated
