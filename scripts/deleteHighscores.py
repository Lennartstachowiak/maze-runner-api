from api import create_api
from db.models import Highscores

api = create_api()
api.app_context().push()

all_highscores = Highscores.query.all()
for highscore in all_highscores:
    highscore.delete()
