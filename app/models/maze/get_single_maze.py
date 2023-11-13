from db import models

Mazes = models.Mazes


def get_single_maze(maze_id):
    maze = Mazes.query.filter_by(id=maze_id).first()
    return maze
