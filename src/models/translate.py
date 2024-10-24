from typing import Optional, List

from deepl import Language
from pydantic import BaseModel


class Translate(BaseModel):
    text: str
    target_lang: Language
    source_lang: Optional[Language] = None
    context: Optional[str] = None
    split_sentences: Optional[str] = None
    preserve_formatting: Optional[bool] = None
    formality: Optional[str] = None
    tag_handling: Optional[str] = None
    outline_detection: Optional[bool] = None
    non_splitting_tags: Optional[List[str]] = None
    splitting_tags: Optional[List[str]] = None
    ignore_tags: Optional[List[str]] = None

    model_config = dict(arbitrary_types_allowed=True)
