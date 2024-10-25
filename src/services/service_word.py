from src.exceptions.exceptions import SuperException
from src.models.word import WordModel
from src.use_cases.use_case_word import WordUseCase


class ServiceWord:
    def __init__(self):
        self.use_case = WordUseCase()

    async def translate_word(self, word: WordModel) -> str:
        str_word = str(word.word)

        if not str_word:
            raise SuperException(
                message="word for text can't be empty"
            )

        if str_word.find(" ") >= 0:
            raise SuperException(
                message="word length can't be greater than one"
            )

        return await self.use_case.execute(word)
