import pytest
from db.db import db
from tests.create_test_data import create_test_data
from os import environ


@pytest.fixture
def client_and_session_and_api(client_and_api):
    # Creates all tables before each test and kills each table after each test
    client, api = client_and_api
    with client.application.app_context():
        db.drop_all()  # Just to be sure that the db is empty
        db.create_all()
        create_test_data()
        yield client, db.session, api
        db.drop_all()


def test_root_endpoint(client_and_api):
    client, api = client_and_api
    response = client.get('/')
    response_text = response.text
    assert response_text == "connected"


def test_get_user(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get('/v1/get_user?id=100000',
                          headers={'Origin': '*'})
    user_response = response.get_json()
    assert user_response['email'] == 'one@web.com'


def test_if_user_demo_algorithms_exist(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    client.set_cookie('session_id_maze_runner', '1')
    response = client.get('/v1/get_algorithms',
                          headers={'Origin': '*'})
    algorithm_response = response.get_json()
    assert len(algorithm_response) > 0


def test_get_single_algorithm(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get('/v1/get_single_algorithm?id=3',
                          headers={'Origin': '*'})
    algorithm_response = response.get_json()
    assert algorithm_response['name'] == 'User Three Algorithm'


def test_check_if_multiple_mazes_exist(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get('/v1/get_mazes',
                          headers={'Origin': '*'})
    maze_response = response.get_json()
    assert len(maze_response) > 0


def test_get_single_mazes(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get('/v1/get_single_maze?id=100',
                          headers={'Origin': '*'})
    maze_response = response.get_json()
    assert maze_response['name'] == 'Test Maze'


def test_get_maze_hiscores_exist(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get('/v1/get_single_maze?id=100',
                          headers={'Origin': '*'})
    maze_response = response.get_json()
    assert len(maze_response['highscores']) > 0
