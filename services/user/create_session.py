
from db.db import db
from db import models
from datetime import date, datetime, timedelta

SessionAuth = models.SessionAuth


def is_session_expired(session):
    today = date.today()
    if session.expiryDate <= today:
        session.delete()
        return True
    else:
        return False


def create_session(user):
    # Check if User has session
    if SessionAuth.query.filter_by(userId=user.id).first() is not None:
        session = SessionAuth.query.filter_by(userId=user.id).first()
        print("session", session)
        if is_session_expired(session) is False:
            return {"sessionId": session.id, "expiryDate": session.expiryDate}
    # Create Session
    expiryDate = datetime.today().date() + timedelta(days=7)
    new_session = SessionAuth(userId=user.id, expiryDate=expiryDate)
    print("new_session", new_session)
    # Add session to db
    db.session.add(new_session)
    db.session.commit()
    return {"sessionId": new_session.id, "expiryDate": new_session.expiryDate}
