from asyncio import run

from src.models.text import TextModel
from src.use_cases.use_case_text import TextUseCase

from tests.conftest import use_case_text
from tests.mocks.text_mock import TextMock


def test_use_case_text_translate_success(use_case_text: TextUseCase) -> None:
    text: TextModel = TextModel.model_validate(TextMock.success_1.model_dump())

    translated = run(
        use_case_text.execute(text)
    )

    assert translated == "my heart is made of paper"
