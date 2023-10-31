from db.db import db
from db import models

SessionAuth = models.SessionAuth


def logout_user(sessionId):
    deleteSession = SessionAuth.query.get(sessionId)
    db.session.delete(deleteSession)
    db.session.commit()
    return True
