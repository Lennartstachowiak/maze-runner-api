from app.models.maze.add_maze_highscore import add_maze_highscore
from db.models import Highscores


def add_maze_highscore_controller(user_id, maze_id, algorithm_id, solution):
    score = solution['score']
    new_highscore = Highscores(
        userId=user_id, mazeId=maze_id, algorithm_id=algorithm_id, score=score)
    add_maze_highscore(new_highscore)
