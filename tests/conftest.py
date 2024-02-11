from os import environ
import pytest
from api import create_api
from flask_migrate import upgrade


@pytest.fixture  # This will always be executed if a test runs
def client():
    # use the default in-memory SQLite database for our tests.
    # We don't want our testing data to exist permanently
    environ['DATABASE_URL'] = 'sqlite://'

    api = create_api()

    with api.app_context():
        upgrade()
        yield api.test_client()
