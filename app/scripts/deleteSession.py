from api import create_api
from db.models import SessionAuth
import sys

api = create_api()
api.app_context().push()

userId = sys.argv[1]
print("SessionId:", userId)
session = SessionAuth.query.filter_by(userId=userId).first()
print("Delete", session.userId)
session.delete()
