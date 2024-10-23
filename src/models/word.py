from typing import Optional

from pydantic import BaseModel


class WordModel(BaseModel):
    word: str
    target_lang: str
    source_lang: Optional[str] = None
