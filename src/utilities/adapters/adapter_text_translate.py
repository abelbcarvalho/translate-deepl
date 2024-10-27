from src.models.text import TextModel
from src.models.translate import Translate

from src.utilities.language.language import get_lang


async def adapter_text_translate(text: TextModel):
    target = await get_lang(text.target_lang)
    source = await get_lang(text.source_lang)

    return Translate(
        text=text.text,
        target_lang=target,
        source_lang=source
    )
