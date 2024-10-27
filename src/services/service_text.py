from src.exceptions.exceptions import SuperException
from src.models.text import TextModel
from src.use_cases.use_case_text import TextUseCase


class ServiceText:
    def __init__(self):
        self.use_case = TextUseCase()

    async def translate_text(self, text: TextModel) -> str:
        text_str = str(text.text)

        if not text_str:
            raise SuperException("text attribute cannot be empty")

        if len(text_str) > 5000:
            raise SuperException("text attribute cannot be longer than 5000 characters")

        return await self.use_case.execute(text)
