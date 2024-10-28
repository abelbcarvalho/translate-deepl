from asyncio import run

from src.controllers.controller_text import ControllerText

from tests.conftest import controller_text, json_to_dict

from tests.mocks.text_mock import TextMock


def test_controller_text_success_case_one(controller_text: ControllerText) -> None:
    resp = run(
        controller_text.translate_text(TextMock.success_1.model_dump())
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"text": "my heart is made of paper"}


def test_controller_text_success_case_two(controller_text: ControllerText) -> None:
    resp = run(
        controller_text.translate_text(TextMock.success_2.model_dump())
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"text": "I'm at university"}


def test_controller_text_success_case_three(controller_text: ControllerText) -> None:
    resp = run(
        controller_text.translate_text(TextMock.success_3.model_dump())
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"text": "brazil won the cup"}


def test_controller_text_failure_case_one_body_invalid(controller_text: ControllerText) -> None:
    resp = run(
        controller_text.translate_text(TextMock.failure_1.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}


def test_controller_text_failure_case_two_text_empty(controller_text: ControllerText) -> None:
    resp = run(
        controller_text.translate_text(TextMock.failure_2.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "text attribute cannot be empty"}


def test_controller_text_failure_case_three_greater_than_5000_chars(controller_text: ControllerText) -> None:
    resp = run(
        controller_text.translate_text(TextMock.failure_3.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {
        "error": "text attribute cannot be longer than 5000 characters"
    }


def test_controller_text_failure_source_lang(controller_text: ControllerText) -> None:
    resp = run(
        controller_text.translate_text(TextMock.failure_4.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}
