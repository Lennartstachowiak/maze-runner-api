from app.models.user.remove_session import remove_session
from app.models.user.add_session import add_session
from app.models.user.handle_session import create_new_session
from db import models

SessionAuth = models.SessionAuth


def session_controller(user):
    old_session = SessionAuth.query.filter_by(userId=user.id).first()
    if old_session is not None:
        remove_session(old_session)
    session = create_new_session(old_session, user)
    add_session(session)
    return {
        "session_id_maze_runner": session.id,
        "expiryDate": session.expiryDate,
    }
