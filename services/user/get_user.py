
from flask import abort
from db import models
from services.user.create_session import is_session_expired

User = models.User
SessionAuth = models.SessionAuth


def get_user(request):
    user_id = get_user_id(request)
    user = User.query.filter_by(id=user_id).first()
    return user


def get_user_id(request):
    sessionId = request.cookies.get('sessionId')
    if not sessionId:
        abort(401, "Unauthorized")
    session = SessionAuth.query.filter_by(
        id=sessionId).first()
    session_exists = session is not None
    if not session_exists or is_session_expired(session):
        abort(401, "Unauthorized")
    user_id = SessionAuth.query.get(sessionId).userId
    if not user_id:
        abort(401, "Unauthorized")
    return user_id
