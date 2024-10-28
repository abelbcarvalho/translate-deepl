from flask.testing import FlaskClient

from tests.conftest import client, base_url, json_to_dict
from tests.mocks.word_mock import WordMock


def test_route_word_single_success_case_one(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.success_1.model_dump()
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"word": "Heart"}


def test_route_word_single_success_case_two(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.success_2.model_dump()
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"word": "Trousers"}


def test_route_word_single_success_case_three(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.success_3.model_dump()
    )

    assert resp.status_code == 200
    assert json_to_dict(resp.data) == {"word": "Catalog"}


def test_route_word_single_failure_case_one(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.failure_1.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}


def test_route_word_single_failure_case_two(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.failure_2.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "word for text can't be empty"}


def test_route_word_single_failure_case_three(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.failure_3.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "word length can't be greater than one"}


def test_route_word_single_failure_case_four(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.failure_4.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}

def test_route_word_single_failure_case_five(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.failure_5.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {
        "error": "you need a context for this word, use text route"
    }

def test_route_word_single_failure_case_six(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/word"),
        json=WordMock.failure_6.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}
