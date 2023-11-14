from db.db import db
from db.models import Highscores


def add_maze_highscore(new_highscore: Highscores):
    new_highscore.save()
    db.session.commit()
