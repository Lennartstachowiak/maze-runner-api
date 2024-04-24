from app.models.maze.get_maze_highscores import get_maze_highscores
from db import models

Mazes = models.Mazes


def get_mazes_objects(user_id):
    mazes = []
    for maze in Mazes.query.filter_by(creator=user_id):
        highscores = get_maze_highscores(maze.id)
        mazes.append(
            {
                "id": maze.id,
                "name": maze.name,
                "difficulty": maze.difficulty,
                "imgLink": maze.imgLink,
                "highscores": highscores,
                "official": False,
            }
        )
    return mazes
