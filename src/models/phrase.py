from typing import Optional

from pydantic import BaseModel

from src.enums.enum_source_lang import EnumSourceLang
from src.enums.enum_target_lang import EnumTargetLang


class PhraseModel(BaseModel):
    phrase: str
    target_lang: EnumTargetLang
    source_lang: Optional[EnumSourceLang] = None
