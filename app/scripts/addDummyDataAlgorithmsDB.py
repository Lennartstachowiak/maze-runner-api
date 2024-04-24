import sys
from api import create_api
from db.models import Users
from addAlgorithms import addAlgorithms

api = create_api()
api.app_context().push()

userEmail = sys.argv[1]
print("Email:", userEmail)

admin = Users.query.filter_by(email=userEmail).first()
adminId = admin.id

addAlgorithms(adminId)
