from json import loads

from typing import Generator, Any, Dict

import pytest
from flask.testing import FlaskClient

from app import app
from src.controllers.controller_text import ControllerText
from src.controllers.controller_word import ControllerWord
from src.services.service_text import ServiceText
from src.services.service_word import ServiceWord
from src.use_cases.use_case_text import TextUseCase
from src.use_cases.use_case_word import WordUseCase

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


@pytest.fixture(scope="function")
def service_word() -> Generator[ServiceWord, None, None]:
    service = ServiceWord()
    yield service


@pytest.fixture(scope="function")
def service_text() -> Generator[ServiceText, None, None]:
    service = ServiceText()
    yield service


@pytest.fixture(scope="function")
def use_case_word() -> Generator[WordUseCase, None, None]:
    use_case = WordUseCase()
    yield use_case


@pytest.fixture(scope="function")
def use_case_text() -> Generator[TextUseCase, None, None]:
    use_case = TextUseCase()
    yield use_case
