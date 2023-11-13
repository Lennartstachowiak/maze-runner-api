from app.models.maze.get_single_highscore import get_single_highscore
from db.db import db
from db.models import Highscores


def remove_maze_highscore(highscore_id):
    highscore: Highscores = get_single_highscore(highscore_id)
    highscore.delete()
    db.session.commit()
