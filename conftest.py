import pytest
from app_server import app
from mongomock import MongoClient


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Use mongomock for testing
    mongo_client = MongoClient()
    app.mongo_client = mongo_client
    app.db = mongo_client.db['users_db']
    app.collection = app.db['users']

    yield client
