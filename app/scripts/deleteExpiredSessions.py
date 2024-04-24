from api import create_api
from db.models import SessionAuth
from datetime import date

api = create_api()
api.app_context().push()

all_session = SessionAuth.query.all()
today = date.today()
for session in all_session:
    if session.expiry_date <= today:
        print("Delete", session.id, "expired since", session.expiry_date)
        session.delete()
