from db.db import db
from db import models
from app.scripts.addAlgorithms import addAlgorithms
from app.models.user.create_session import create_session

User = models.User


def register_user(bcrypt, username, email, password):
    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return 409

    # Builder Pattern

    class UserBuilder:
        def __init__(self):
            self.user = User()

        def set_username(self, username):
            self.user.username = username
            return self

        def set_email(self, email):
            self.user.email = email
            return self

        def set_password(self, password):
            hashed_password = bcrypt.generate_password_hash(
                password).decode('utf-8')
            self.user.password = hashed_password
            return self

        def build(self):
            return self.user

    user_builder = UserBuilder()
    new_user = user_builder.set_username(username).set_email(
        email).set_password(password).build()

    #  Add User to db
    db.session.add(new_user)
    db.session.commit()

    # Get User
    user = User.query.filter_by(email=email).first()

    # Add default user algorithms
    userId = user.id
    addAlgorithms(userId)

    sessionData = create_session(user)
    return sessionData
