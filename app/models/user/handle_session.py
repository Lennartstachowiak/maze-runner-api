from app.controller.user.remove_session_controller import remove_session_controller
from db import models
from datetime import datetime, timedelta

SessionAuth = models.SessionAuth


def handle_session(old_session: type[SessionAuth], user):
    if old_session is not None:
        remove_session_controller(old_session)

    expiryDate = datetime.today().date() + timedelta(days=7)
    new_session = SessionAuth(userId=user.id, expiryDate=expiryDate)
    return new_session
