from api import create_api
from db.models import Algorithms
from db.models import User
from addAlgorithms import addAlgorithms

api = create_api()
api.app_context().push()

admin = User.query.filter_by(email="Lennart.Stachowiak@code.berlin").first()
adminId = admin.id

addAlgorithms(adminId)
