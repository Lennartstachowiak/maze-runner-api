from api import create_api
from db.models import Algorithms

api = create_api()
api.app_context().push()

all_allgorithm = Algorithms.query.all()
for algorithm in all_allgorithm:
    algorithm.delete()
