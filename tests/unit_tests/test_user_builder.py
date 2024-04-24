from app.models.user.register_user import UserBuilder
from flask_bcrypt import Bcrypt
import pytest

username = "username"
email = "email"
password = "password"


@pytest.fixture
def user_props(client_and_api):
    client, api = client_and_api
    bcrypt = Bcrypt(api)
    user_builder = UserBuilder(bcrypt)
    new_user = user_builder.set_username(username).set_email(email).set_password(password).build()
    return new_user, bcrypt


def test_user_builder_property(user_props):
    new_user, bcrypt = user_props
    assert new_user.username is username
    assert new_user.email is email
    assert new_user.password


def test_user_builder_password_hashed(user_props):
    new_user, bcrypt = user_props
    password_hash = new_user.password
    isHashedSame = bcrypt.check_password_hash(password_hash, password)
    assert isHashedSame
