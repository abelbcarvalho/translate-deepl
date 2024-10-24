from typing import Optional, List

from pydantic import BaseModel

from src.enums.enum_target_lang import EnumTargetLang
from src.enums.enum_source_lang import EnumSourceLang


class Translate(BaseModel):
    text: str
    target_lang: EnumTargetLang
    source_lang: Optional[EnumSourceLang] = None
    context: Optional[str] = None
    split_sentences: Optional[str] = None
    preserve_formatting: Optional[bool] = None
    formality: Optional[str] = None
    glossary_id: Optional[str] = None
    show_billed_characters: Optional[bool] = None
    tag_handling: Optional[str] = None
    outline_detection: Optional[bool] = None
    non_splitting_tags: Optional[List[str]] = None
    splitting_tags: Optional[List[str]] = None
    ignore_tags: Optional[List[str]] = None
