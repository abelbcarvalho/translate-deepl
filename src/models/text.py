from typing import Optional

from pydantic import BaseModel


class TextModel(BaseModel):
    text: str
    target_lang: str
    source_lang: Optional[str] = None
