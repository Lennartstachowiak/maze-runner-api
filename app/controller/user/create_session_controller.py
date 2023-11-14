
from app.controller.user.remove_session_controller import remove_session_controller
from app.models.user.handle_session import create_new_session
from db.db import db
from db import models

SessionAuth = models.SessionAuth


def create_session_controller(user):
    old_session = SessionAuth.query.filter_by(userId=user.id).first()
    if old_session is not None:
        remove_session_controller(old_session)
    session = create_new_session(old_session, user)
    db.session.add(session)
    db.session.commit()
    return {"session_id_maze_runner": session.id, "expiryDate": session.expiryDate}
