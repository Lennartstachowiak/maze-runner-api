from os import environ
import pytest
from server.api_file import api
from flask_migrate import upgrade


@pytest.fixture
def client():
    environ['DATABASE_URL'] = 'sqlite://'

    with api.app_context():
        upgrade()
        yield api.test_client()


def test_addition():
    # no arrangement needed
    result = 4+2  # act
    assert result == 6      # assert


# use the default in-memory SQLite database for our tests.
# We don't want our testing data to exist permanently
environ['DATABASE_URL'] = 'sqlite://'
