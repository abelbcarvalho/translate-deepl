from asyncio import run

from src.controllers.controller_word import ControllerWord

from tests.conftest import controller_word, json_to_dict
from tests.mocks.word_mock import WordMock


def test_controller_word_single_success_case_one(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.success_1.model_dump())
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"word": "Heart"}


def test_controller_word_single_success_case_two(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.success_2.model_dump())
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"word": "Trousers"}


def test_controller_word_single_success_case_three(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.success_3.model_dump())
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"word": "Catalog"}


def test_controller_word_single_failure_case_one(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.failure_1.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}


def test_controller_word_single_failure_case_two(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.failure_2.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "word for text can't be empty"}


def test_controller_word_single_failure_case_three(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.failure_3.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "word length can't be greater than one"}


def test_controller_word_single_failure_case_four(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.failure_4.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}

def test_controller_word_single_failure_case_five(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.failure_5.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {
        "error": "you need a context for this word, use text route"
    }


def test_controller_word_single_failure_source_lang(controller_word: ControllerWord) -> None:
    resp = run(
        controller_word.translate_word(WordMock.failure_6.model_dump())
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {
        "error": "body has invalid data"
    }
