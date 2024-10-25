from typing import Optional

from pydantic import BaseModel

from src.enums.enum_source_lang import EnumSourceLang
from src.enums.enum_target_lang import EnumTargetLang

from dataclasses import dataclass, field


class Word(BaseModel):
    word: str
    target_lang: str
    source_lang: Optional[str] = None


@dataclass
class WordMock:
    success_1 = Word(
        word="Coração",
        target_lang=EnumTargetLang.EN_US.value
    )

    success_2 = Word(
        word="Calças",
        target_lang=EnumTargetLang.EN_GB.value,
        source_lang=EnumSourceLang.PT.value
    )

    success_3 = Word(
        word="Catálogo",
        target_lang=EnumTargetLang.EN_US.value,
        source_lang=EnumSourceLang.PT.value
    )

    failure_1 = Word(
        word="Casa",
        target_lang=EnumSourceLang.EN.value
    )

    failure_2 = Word(
        word="",
        target_lang=EnumTargetLang.EN_US.value
    )

    failure_3 = Word(
        word="Guarda Chuva",
        target_lang=EnumTargetLang.ES.value
    )

    failure_4 = Word(
        word="Chuva",
        target_lang=EnumTargetLang.ES.value,
        source_lang=EnumTargetLang.PT_BR.value
    )
