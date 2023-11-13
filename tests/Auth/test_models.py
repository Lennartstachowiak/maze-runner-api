from datetime import date, timedelta
from app.models.user.is_session_expired import is_session_expired
import db.db

from db.models import SessionAuth

today = date.today()
tomorrow = today + timedelta(days=1)


def test_session_expired(client):
    session = SessionAuth(userId='shouldBeDeleted', expiryDate=today)
    db.session.add(session)
    db.session.commit()

    current_session = SessionAuth.query.filter_by(
        userId='shouldBeDeleted').first()

    is_session_expired(current_session)

    deleted_session = SessionAuth.query.filter_by(
        userId='shouldBeDeleted').first()
    assert deleted_session is None


def test_session_not_expired(client):
    session = SessionAuth(userId='stillThere', expiryDate=tomorrow)
    db.session.add(session)
    db.session.commit()

    current_session = SessionAuth.query.filter_by(
        userId='stillThere').first()

    is_session_expired(current_session)

    not_deleted_session = SessionAuth.query.filter_by(
        userId='stillThere').first()
    assert not_deleted_session

    session.delete()

    deleted_session = SessionAuth.query.filter_by(
        userId='stillThere').first()
    assert deleted_session is None
