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
    with pytest.raises(SuperException) as se:
        run(
            check_body(
                WordMock.failure_1.model_dump(),
                WordModel
            )
        )

    exc_msg = str(se.value)

    assert exc_msg == "body has invalid data"


def test_controller_check_body_super_exception_text() -> None:
    with pytest.raises(SuperException) as se:
        run(
            check_body(
                TextMock.failure_1.model_dump(),
                TextModel
            )
        )

    exc_msg = str(se.value)

    assert exc_msg == "body has invalid data"


def test_controller_body_validation_error_word() -> None:
    with pytest.raises(ValidationError) as ve:
        WordModel.model_validate(
            WordMock.failure_1.model_dump()
        )

    exc_msg = str(ve.value)

    assert "1 validation error for WordModel\ntarget_lang" in exc_msg


def test_controller_body_validation_error_word_source_lang() -> None:
    with pytest.raises(ValidationError) as ve:
        WordModel.model_validate(
            WordMock.failure_6.model_dump()
        )

    exc_msg = str(ve.value)

    assert "1 validation error for WordModel\nsource_lang" in exc_msg


def test_controller_body_validation_error_text() -> None:
    with pytest.raises(ValidationError) as ve:
        TextModel.model_validate(
            TextMock.failure_1.model_dump()
        )

    exc_msg = str(ve.value)

    assert "1 validation error for TextModel\ntarget_lang" in exc_msg


def test_controller_body_validation_error_text_source_lang() -> None:
    with pytest.raises(ValidationError) as ve:
        TextModel.model_validate(
            TextMock.failure_4.model_dump()
        )

    exc_msg = str(ve.value)

    assert "1 validation error for TextModel\nsource_lang" in exc_msg
