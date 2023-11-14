from db.db import db
from db.models import SessionAuth


def add_session(session: type[SessionAuth]):
    session.save()
    db.session.commit()
