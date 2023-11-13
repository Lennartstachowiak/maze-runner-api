from db import models
from app.models.maze.get_highscores import get_highscores

Mazes = models.Mazes


def get_mazes_objects():
    mazes = []
    for maze in Mazes.query.filter_by(creator="official"):
        if maze.isTest:
            continue
        highscoreList = get_highscores(maze.id)
        mazes.append({"id": maze.id, "name": maze.name,
                      "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "official": True})
    return mazes
