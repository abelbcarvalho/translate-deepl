from typing import Optional

from pydantic import BaseModel

from src.enums.enum_source_lang import EnumSourceLang
from src.enums.enum_target_lang import EnumTargetLang

from dataclasses import dataclass


class Text(BaseModel):
    text: str
    target_lang: str
    source_lang: Optional[str] = None


@dataclass
class TextMock:
    success_1 = Text(
        text="meu coração é de papel",
        target_lang=EnumTargetLang.EN_US.value
    )

    success_2 = Text(
        text="eu estou na faculdade",
        target_lang=EnumTargetLang.EN_GB.value,
        source_lang=EnumSourceLang.PT.value
    )

    success_3 = Text(
        text="o brasil ganhou a copa",
        target_lang=EnumTargetLang.EN_US.value,
        source_lang=EnumSourceLang.PT.value
    )

    failure_1 = Text(
        text="Casa",
        target_lang=EnumSourceLang.EN.value
    )

    failure_2 = Text(
        text="",
        target_lang=EnumTargetLang.EN_US.value
    )

    failure_3 = Text(
        text="".join("K" + "abcdefghij" * 500),
        target_lang=EnumTargetLang.EN_US.value
    )
