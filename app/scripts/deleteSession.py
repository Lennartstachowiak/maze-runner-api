from api import create_api
from db.models import SessionAuth
import sys

api = create_api()
api.app_context().push()

user_id = sys.argv[1]
print("SessionId:", user_id)
session = SessionAuth.query.filter_by(user_id=user_id).first()
print("Delete", session.user_id)
session.delete()
