from db.db import db
from db import models

SessionAuth = models.SessionAuth


def remove_session_controller(session: type[SessionAuth]):
    session.delete()
    db.session.commit()
