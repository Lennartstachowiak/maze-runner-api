
from app.models.user.handle_session import handle_session
from db.db import db
from db import models

SessionAuth = models.SessionAuth


def create_session_controller(user):
    old_session = SessionAuth.query.filter_by(userId=user.id).first()
    session = handle_session(old_session, user)
    db.session.add(session)
    db.session.commit()
    return {"session_id_maze_runner": session.id, "expiryDate": session.expiryDate}
