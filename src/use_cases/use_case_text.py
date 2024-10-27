from src.core.deepl_translate import DeepLTranslate
from src.models.text import TextModel
from src.utilities.adapters.adapter_text_translate import adapter_text_translate


class TextUseCase:
    def __init__(self):
        self.deepl = DeepLTranslate()

    async def execute(self, text: TextModel) -> str:
        for_translate = await adapter_text_translate(text)

        new_text = await self.deepl.translate(for_translate)

        return new_text.text
