from app.models.user.remove_session import remove_session
from db import models
from datetime import datetime, timedelta

SessionAuth = models.SessionAuth


def create_new_session(old_session: type[SessionAuth], user):
    if old_session is not None:
        remove_session(old_session)

    expiryDate = datetime.today().date() + timedelta(days=7)
    new_session = SessionAuth(userId=user.id, expiryDate=expiryDate)
    return new_session
