from json import loads

from typing import Generator, Any, Dict

import pytest
from flask.testing import FlaskClient

from app import app
from src.controllers.controller_text import ControllerText
from src.controllers.controller_word import ControllerWord

base_url = "http://127.0.0.1:1998/api/v1/deepl{}"


def json_to_dict(data: str) -> Dict[str, Any]:
    return loads(data)


@pytest.fixture(scope="function")
def client() -> Generator[FlaskClient, None, None]:
    with FlaskClient(app) as client:
        yield client


@pytest.fixture(scope="function")
def controller_word() -> Generator[ControllerWord, None, None]:
    controller = ControllerWord()
    yield controller


@pytest.fixture(scope="function")
def controller_text() -> Generator[ControllerText, None, None]:
    controller = ControllerText()
    yield controller
