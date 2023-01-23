import pytest
from starlette.testclient import TestClient

from fastapi_project.fastapi_app.app import app


@pytest.fixture(scope='module')
def test_app():
    client = TestClient(app)
    yield client
