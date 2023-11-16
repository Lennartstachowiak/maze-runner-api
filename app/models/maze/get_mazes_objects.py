from app.models.maze.get_highscores import get_highscores
from db import models
from app.models.maze.get_highscores_object_list import create_highscores_object_list

Mazes = models.Mazes


def get_mazes_objects():
    mazes = []
    for maze in Mazes.query.filter_by(creator="official", isTest=False):
        highscores = get_highscores(maze.id)
        highscoreList = create_highscores_object_list(highscores)
        mazes.append({"id": maze.id, "name": maze.name,
                      "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "official": True})
    return mazes
