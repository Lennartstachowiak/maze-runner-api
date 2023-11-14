from app.models.maze.delete_highscore import delete_highscore
from app.models.maze.get_single_highscore import get_single_highscore
from db.db import db
from db.models import Highscores


def remove_maze_highscore_controller(highscore_id):
    highscore: Highscores = get_single_highscore(highscore_id)
    delete_highscore(highscore)
