from db.db import db
from db.models import Users
from app.scripts.addAlgorithms import addAlgorithms
from app.controller.user.session_controller import session_controller


class UserBuilder:
    def __init__(self, bcrypt):
        self.user = Users()
        self.bcrypt = bcrypt

    def set_username(self, username):
        self.user.username = username
        return self

    def set_email(self, email):
        self.user.email = email
        return self

    def set_password(self, password):
        hashed_password = self.bcrypt.generate_password_hash(password).decode("utf-8")
        self.user.password = hashed_password
        return self

    def build(self):
        return self.user


def register_user(bcrypt, username, email, password):
    user_exists = Users.query.filter_by(email=email).first() is not None

    if user_exists:
        return 409

    # Builder Pattern

    user_builder = UserBuilder(bcrypt)
    new_user = user_builder.set_username(username).set_email(email).set_password(password).build()

    #  Add User to db
    db.session.add(new_user)
    db.session.commit()

    # Get User
    user = Users.query.filter_by(email=email).first()

    # Add default user algorithms
    user_id = user.id
    addAlgorithms(user_id)

    sessionData = session_controller(user)
    return sessionData
