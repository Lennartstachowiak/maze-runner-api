from app.models.user.remove_session import remove_session
from db import models
from datetime import datetime, timedelta

SessionAuth = models.SessionAuth


def create_new_session(old_session: type[SessionAuth], user):
    if old_session is not None:
        remove_session(old_session)

    expiry_date = datetime.today().date() + timedelta(days=7)
    new_session = SessionAuth(user_id=user.id, expiry_date=expiry_date)
    return new_session
