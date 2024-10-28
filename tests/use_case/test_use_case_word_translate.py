import pytest

from asyncio import run

from src.exceptions.exceptions import SuperException
from src.models.word import WordModel
from src.use_cases.use_case_word import WordUseCase

from tests.conftest import use_case_word
from tests.mocks.word_mock import WordMock


def test_use_case_word_translate_success(use_case_word: WordUseCase) -> None:
    word: WordModel = WordModel.model_validate(WordMock.success_1.model_dump())

    translated = run(
        use_case_word.execute(word)
    )

    assert translated == "Heart"


def test_use_case_word_translate_except(use_case_word: WordUseCase) -> None:
    word: WordModel = WordModel.model_validate(WordMock.failure_5.model_dump())

    with pytest.raises(SuperException) as se:
        run(
            use_case_word.execute(word)
        )

    exc_msg = str(se.value)

    assert exc_msg == "you need a context for this word, use text route"
