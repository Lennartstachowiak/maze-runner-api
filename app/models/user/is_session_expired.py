from app.controller.user.remove_session_controller import remove_session_controller
from db import models
from datetime import date

SessionAuth = models.SessionAuth


def is_session_expired(session: type[SessionAuth]):
    today = date.today()
    if session.expiryDate <= today:
        remove_session_controller(session)
        return True
    else:
        return False
