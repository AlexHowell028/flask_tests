import pytest
from app import app as flask_demo

@pytest.fixture()
def app():
    yield flask_demo

@pytest.fixture
def client(app):
    return app.test_client()
