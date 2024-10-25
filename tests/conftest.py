from typing import Generator

import pytest
from flask.testing import FlaskClient

from app import app


base_url = "http://127.0.0.1:1998/api/v1/deepl{}"


@pytest.fixture(scope="function")
def client() -> Generator[FlaskClient, None, None]:
    with FlaskClient(app) as client:
        yield client
