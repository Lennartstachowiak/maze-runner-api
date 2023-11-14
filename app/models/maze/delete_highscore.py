from db.db import db
from db.models import Highscores


def delete_highscore(highscore: Highscores):
    highscore.delete()
    db.session.commit()
