from db.db import db
from db import models

SessionAuth = models.SessionAuth


def remove_session_controller(session: type[SessionAuth]):
    db.session.delete(session)
    db.session.commit()
