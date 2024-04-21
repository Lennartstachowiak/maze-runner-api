from app.models.maze.get_maze_highscores import get_maze_highscores
from db import models

Mazes = models.Mazes


def get_mazes_objects():
    mazes = []
    for maze in Mazes.query.filter_by(creator="official", isTest=False):
        highscores = get_maze_highscores(maze.id)
        mazes.append({"id": maze.id, "name": maze.name,
                      "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscores, "official": True})
    return mazes
