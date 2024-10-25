from json import loads

from typing import Generator, Any, Dict

import pytest
from flask.testing import FlaskClient

from app import app


base_url = "http://127.0.0.1:1998/api/v1/deepl{}"


def json_to_dict(data: str) -> Dict[str, Any]:
    return loads(data)


@pytest.fixture(scope="function")
def client() -> Generator[FlaskClient, None, None]:
    with FlaskClient(app) as client:
        yield client
