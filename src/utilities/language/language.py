from typing import Type

from enum import Enum

from deepl import Language


async def get_lang(enum: Enum) -> Language | None:
    if not enum:
        return None

    return Language(name=enum.name, code=enum.value)
