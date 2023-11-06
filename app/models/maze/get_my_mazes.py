from app.models.maze.get_highscores import get_highscores
from db import models

Mazes = models.Mazes


def get_my_mazes(user_id):
    mazes = []
    for maze in Mazes.query.filter_by(creator=user_id):
        highscoreList = get_highscores(maze.id)
        mazes.append({"id": maze.id, "name": maze.name,
                      "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "official": False})
    return mazes
