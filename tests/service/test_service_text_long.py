import pytest

from asyncio import run

from src.exceptions.exceptions import SuperException

from src.models.text import TextModel

from src.services.service_text import ServiceText

from tests.conftest import service_text
from tests.mocks.text_mock import TextMock


def test_service_text_long_case_success_one(service_text: ServiceText) -> None:
    text: TextModel = TextModel.model_validate(TextMock.success_1.model_dump())

    translated = run(
        service_text.translate_text(text)
    )

    assert translated == "my heart is made of paper"


def test_service_text_long_case_success_two(service_text: ServiceText) -> None:
    text: TextModel = TextModel.model_validate(TextMock.success_2.model_dump())

    translated = run(
        service_text.translate_text(text)
    )

    assert translated == "I'm at university"


def test_service_text_long_case_success_three(service_text: ServiceText) -> None:
    text: TextModel = TextModel.model_validate(TextMock.success_3.model_dump())

    translated = run(
        service_text.translate_text(text)
    )

    assert translated == "brazil won the cup"


def test_service_text_long_case_except_empty_text(service_text: ServiceText) -> None:
    text: TextModel = TextModel.model_validate(TextMock.failure_2.model_dump())

    with pytest.raises(SuperException) as se:
        run(
            service_text.translate_text(text)
        )

    exc_msg = str(se.value)

    assert exc_msg == "text attribute cannot be empty"


def test_service_text_long_case_except_max_length_five_thousand(service_text: ServiceText) -> None:
    text: TextModel = TextModel.model_validate(TextMock.failure_3.model_dump())

    with pytest.raises(SuperException) as se:
        run(
            service_text.translate_text(text)
        )

    exc_msg = str(se.value)

    assert exc_msg == "text attribute cannot be longer than 5000 characters"
