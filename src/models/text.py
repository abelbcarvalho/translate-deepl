from typing import Optional

from pydantic import BaseModel

from src.enums.enum_source_lang import EnumSourceLang
from src.enums.enum_target_lang import EnumTargetLang


class TextModel(BaseModel):
    text: str
    target_lang: EnumTargetLang
    source_lang: Optional[EnumSourceLang] = None
