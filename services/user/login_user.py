from db import models
from services.user.create_session import create_session

User = models.User


def login_user(bcrypt, email, password):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return False
    if not bcrypt.check_password_hash(user.password, password):
        return False
    sessionData = create_session(user)
    return sessionData
