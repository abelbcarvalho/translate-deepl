from flask.testing import FlaskClient

from tests.conftest import base_url, json_to_dict, client
from tests.mocks.text_mock import TextMock


def test_route_text_success_case_one(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/text"),
        json=TextMock.success_1.model_dump()
    )

    assert resp.status_code == 200


def test_route_text_success_case_two(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/text"),
        json=TextMock.success_2.model_dump()
    )

    assert resp.status_code == 200


def test_route_text_success_case_three(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/text"),
        json=TextMock.success_3.model_dump()
    )

    assert resp.status_code == 200


def test_text_route_failure_case_one_body_invalid(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/text"),
        json=TextMock.failure_1.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "body has invalid data"}


def test_text_route_failure_case_two_text_empty(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/text"),
        json=TextMock.failure_2.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {"error": "text attribute cannot be empty"}


def test_text_route_failure_case_three_greater_than_5000_chars(client: FlaskClient) -> None:
    resp = client.post(
        base_url.format("/translate/text"),
        json=TextMock.failure_3.model_dump()
    )

    assert resp.status_code == 400
    assert json_to_dict(resp.data) == {
        "error": "text attribute cannot be longer than 5000 characters"
    }
