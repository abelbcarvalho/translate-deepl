import pytest

from asyncio import run

from src.exceptions.exceptions import SuperException
from src.models.word import WordModel
from src.services.service_word import ServiceWord

from tests.conftest import service_word
from tests.mocks.word_mock import WordMock


def test_service_word_single_success_case_one(service_word: ServiceWord) -> None:
    word: WordModel = WordModel.model_validate(WordMock.success_1.model_dump())

    translated = run(
        service_word.translate_word(word)
    )

    assert translated == "Heart"


def test_service_word_single_success_case_two(service_word: ServiceWord) -> None:
    word: WordModel = WordModel.model_validate(WordMock.success_2.model_dump())

    translated = run(
        service_word.translate_word(word)
    )

    assert translated == "Trousers"


def test_service_word_single_success_case_three(service_word: ServiceWord) -> None:
    word: WordModel = WordModel.model_validate(WordMock.success_3.model_dump())

    translated = run(
        service_word.translate_word(word)
    )

    assert translated == "Catalog"


def test_service_word_single_except_empty(service_word: ServiceWord) -> None:
    word: WordModel = WordModel.model_validate(WordMock.failure_2.model_dump())


    with pytest.raises(SuperException) as ex:
        run(
            service_word.translate_word(word)
        )

    exc_msg = str(ex.value)

    assert exc_msg == "word for text can't be empty"


def test_service_word_single_except_greater_than_one(service_word: ServiceWord) -> None:
    word: WordModel = WordModel.model_validate(WordMock.failure_3.model_dump())

    with pytest.raises(SuperException) as se:
        run(
            service_word.translate_word(word)
        )

    str_exc = str(se.value)

    assert str_exc == "word length can't be greater than one"


def test_service_word_single_except_same_word_not_translated(service_word: ServiceWord) -> None:
    word: WordModel = WordModel.model_validate(WordMock.failure_5.model_dump())

    with pytest.raises(SuperException) as se:
        run(
            service_word.translate_word(word)
        )

    str_exc = str(se.value)

    assert str_exc == "you need a context for this word, use text route"
