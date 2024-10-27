import pytest

from asyncio import run

from pydantic import ValidationError

from src.exceptions.exceptions import SuperException
from src.models.text import TextModel
from src.models.word import WordModel
from src.utilities.checkers.check_body import check_body
from tests.mocks.text_mock import TextMock
from tests.mocks.word_mock import WordMock


def test_controller_check_body_super_exception_word() -> None:
    with pytest.raises(SuperException):
        run(
            check_body(
                WordMock.failure_1.model_dump(),
                WordModel
            )
        )


def test_controller_check_body_super_exception_text() -> None:
    with pytest.raises(SuperException):
        run(
            check_body(
                TextMock.failure_1.model_dump(),
                TextModel
            )
        )


def test_controller_body_validation_error_word() -> None:
    with pytest.raises(ValidationError):
        WordModel.model_validate(
            WordMock.failure_1.model_dump()
        )


def test_controller_body_validation_error_text() -> None:
    with pytest.raises(ValidationError):
        TextModel.model_validate(
            TextMock.failure_1.model_dump()
        )
