from flask import make_response
from db.db import db
from db import models

SessionAuth = models.SessionAuth


def logout_user(request):
    sessionId = request.cookies.get('sessionId')
    deleteSession = SessionAuth.query.get(sessionId)
    db.session.delete(deleteSession)
    db.session.commit()
    res = make_response()
    res.delete_cookie('sessionId',)
    return res
