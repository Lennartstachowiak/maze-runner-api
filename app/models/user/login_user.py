from db import models
from app.controller.user.create_session_controller import create_session_controller

User = models.Users


def login_user(bcrypt, email, password):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return
    if not bcrypt.check_password_hash(user.password, password):
        return
    return user
