from api import create_api
from db.models import Mazes

api = create_api()
api.app_context().push()

all_mazes = Mazes.query.all()
for maze in all_mazes:
    maze.delete()
