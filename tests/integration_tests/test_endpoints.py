import pytest
from db.db import db
from tests.create_test_data import create_test_data


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
    response = client.get("/")
    response_text = response.text
    assert response_text == "connected"


def test_user_registration_works(client_and_session_and_api):
    username = "Test User Registration"
    email = "testUser@web.com"
    password = "t3stp@sSword"
    repeated_password = "t3stp@sSword"
    client, session, api = client_and_session_and_api
    response = client.post(
        "/v1/register",
        headers={"Origin": "*"},
        json={"username": username, "email": email, "password": password, "repeatedPassword": repeated_password},
    )
    status_code = response.status_code
    assert status_code == 200


def test_user_registration_fails_password_check(client_and_session_and_api):
    username = "Test User"
    email = "test@web.com"
    password = "t3stp@sSword"
    repeated_password = "False"
    client, session, api = client_and_session_and_api
    response = client.post(
        "/v1/register",
        headers={"Origin": "*"},
        json={"username": username, "email": email, "password": password, "repeatedPassword": repeated_password},
    )
    status_code = response.status_code
    assert status_code == 401


def test_user_registration_fails_user_email(client_and_session_and_api):
    username = "Test User"
    email = "testUser@web.com"
    password = "t3stp@sSword"
    repeated_password = "t3stp@sSword"
    client, session, api = client_and_session_and_api
    response = client.post(
        "/v1/register",
        headers={"Origin": "*"},
        json={"username": username, "email": email, "password": password, "repeatedPassword": repeated_password},
    )
    status_code = response.status_code
    assert status_code == 200
    response = client.post(
        "/v1/register",
        headers={"Origin": "*"},
        json={"username": username, "email": email, "password": password, "repeatedPassword": repeated_password},
    )
    status_code = response.status_code
    assert status_code == 409  # Conflict because email should be unique


def test_get_user(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get("/v1/get_user?id=100000", headers={"Origin": "*"})
    user_response = response.get_json()
    assert user_response["email"] == "one@web.com"


def test_if_user_demo_algorithms_exist(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    client.set_cookie("session_id_maze_runner", "1")
    response = client.get("/v1/get_algorithms", headers={"Origin": "*"})
    algorithm_response = response.get_json()
    assert len(algorithm_response) > 0


def test_get_single_algorithm(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get("/v1/get_single_algorithm?id=3", headers={"Origin": "*"})
    algorithm_response = response.get_json()
    assert algorithm_response["name"] == "User Three Algorithm"


def test_check_if_multiple_mazes_exist(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get("/v1/get_mazes", headers={"Origin": "*"})
    maze_response = response.get_json()
    assert len(maze_response) > 0


def test_get_single_mazes(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get("/v1/get_single_maze?id=100", headers={"Origin": "*"})
    maze_response = response.get_json()
    assert maze_response["name"] == "Test Maze"


def test_get_maze_hiscores_exist(client_and_session_and_api):
    client, session, api = client_and_session_and_api
    response = client.get("/v1/get_single_maze?id=100", headers={"Origin": "*"})
    maze_response = response.get_json()
    assert len(maze_response["highscores"]) > 0
