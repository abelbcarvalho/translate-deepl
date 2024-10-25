from src.models.translate import Translate
from src.models.word import WordModel

from src.utilities.language.language import get_lang


async def adapter_word_translate(word: WordModel):
    target = await get_lang(word.target_lang)
    source = await get_lang(word.source_lang)

    return Translate(
        text=word.word,
        target_lang=target,
        source_lang=source,
    )
