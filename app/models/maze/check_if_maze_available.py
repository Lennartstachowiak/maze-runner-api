from db import models


Mazes = models.Mazes


def check_if_maze_available(maze_name):
    mazes = Mazes.query.filter_by(name=maze_name).all()
    if len(mazes) > 0:
        return False
    return True
