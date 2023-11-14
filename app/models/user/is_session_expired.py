from app.models.user.remove_session import remove_session
from db import models
from datetime import date

SessionAuth = models.SessionAuth


def is_session_expired(session: type[SessionAuth]):
    today = date.today()
    if session.expiryDate <= today:
        remove_session(session)
        return True
    else:
        return False
