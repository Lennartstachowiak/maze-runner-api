from api import create_api
from db.models import Algorithms

api = create_api()
api.app_context().push()

algorithmList = [
    {"name": "Depth-First Search", "code": "CODE"},
    {"name": "Breadth-First Search", "code": "CODE"},
    {"name": "Dijkstra's Algorithm", "code": "CODE"},
    {"name": "A* Algorithm", "code": "CODE"},
    {"name": "Greedy Best-First Search", "code": "CODE"},
    {"name": "Bellman Ford Algorithm", "code": "CODE"},
]

for algorithm in algorithmList:
    new_algorithm = Algorithms(name=algorithm["name"], code=algorithm["code"])
    new_algorithm.save()
