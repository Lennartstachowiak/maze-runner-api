import pytest
from db.db import db
from tests.create_test_data import create_test_mazes


@pytest.fixture
def client_and_session_and_api(client_and_api):
    # Creates all tables before each test and kills each table after each test
    client, api = client_and_api
    with client.application.app_context():
        db.drop_all()  # Just to be sure that the db is empty
        db.create_all()
        create_test_mazes()
        yield client, db.session, api
        db.drop_all()


def test_user_authentication_flow(client_and_session_and_api):
    username = "Test User"
    email = "test@web.com"
    password = "t3stp@sSword"
    repeated_password = "t3stp@sSword"

    # Registration
    client, session, api = client_and_session_and_api
    response_registration = client.post(
        "/v1/register",
        headers={"Origin": "*"},
        json={"username": username, "email": email, "password": password, "repeatedPassword": repeated_password},
    )
    session_cookie_registration = client.get_cookie("session_id_maze_runner")
    session_cookie_registration_value = session_cookie_registration.value
    assert response_registration.status_code == 200
    assert session_cookie_registration  # Check if session cookie is returned

    # Check authentication works
    response_auth_after_registration = client.get("/v1/@me", headers={"Origin": "*"})
    assert response_auth_after_registration.status_code == 200

    # Logout
    response_logout = client.post("/v1/logout", headers={"Origin": "*"})
    session_cookie_logout = client.get_cookie("session_id_maze_runner")
    assert response_logout.status_code == 200
    assert session_cookie_logout is None  # Check if cookie removed

    # Check authentication fails
    response_auth_after_logout = client.get("/v1/@me", headers={"Origin": "*"})
    assert response_auth_after_logout.status_code == 401

    # Login
    response_login = client.post(
        "/v1/login", headers={"Origin": "*"}, json={"username": username, "email": email, "password": password}
    )
    session_cookie_login = client.get_cookie("session_id_maze_runner")
    session_cookie_login_value = session_cookie_login.value
    assert response_login.status_code == 200
    assert session_cookie_login  # Check if session cookie is returned

    # Check authentication works
    response_auth_after_login = client.get("/v1/@me", headers={"Origin": "*"})
    assert response_auth_after_login.status_code == 200

    # Check if session from registration is different to login
    assert session_cookie_registration_value != session_cookie_login_value
