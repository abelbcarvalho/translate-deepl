from typing import Optional

from pydantic import BaseModel


class PhraseModel(BaseModel):
    phrase: str
    target_lang: str
    source_lang: Optional[str] = None
