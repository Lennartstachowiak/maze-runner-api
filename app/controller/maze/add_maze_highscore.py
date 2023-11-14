from db.db import db
from db.models import Highscores


def add_maze_highscore(user_id, maze_id, algorithm_id, solution):
    score = solution['score']
    new_highscore = Highscores(
        userId=user_id, mazeId=maze_id, algorithm_id=algorithm_id, score=score)
    new_highscore.save()
    db.session.commit()
