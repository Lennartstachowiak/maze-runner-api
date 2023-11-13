from app.controller.user.remove_session_controller import remove_session_controller
from db.db import db
from db import models

SessionAuth = models.SessionAuth


def logout_user(sessionId):
    deleteSession = SessionAuth.query.get(sessionId)
    remove_session_controller(deleteSession)
    return True
