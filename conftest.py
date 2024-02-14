import pytest
from app_server import app as flask_app


@pytest.fixture
def app():
   
    flask_app.config.update({
        "TESTING": True,
    })

    yield flask_app  

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()