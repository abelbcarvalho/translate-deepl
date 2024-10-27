from src.core.deepl_translate import DeepLTranslate
from src.exceptions.exceptions import SuperException
from src.models.word import WordModel
from src.utilities.adapters.adapter_word_translate import adapter_word_translate


class WordUseCase:
    def __init__(self):
        self.transl = DeepLTranslate()

    async def execute(self, word: WordModel) -> str:
        text = await adapter_word_translate(word)

        data = await self.transl.translate(text)

        if data.text.lower() == word.word.lower():
            raise SuperException("you need a context for this word, use text route")

        return data.text
