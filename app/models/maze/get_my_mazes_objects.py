from app.models.maze.get_highscores import get_highscores
from app.models.maze.get_highscores_object_list import create_highscores_object_list
from db import models

Mazes = models.Mazes


def get_my_mazes_objects(user_id):
    mazes = []
    for maze in Mazes.query.filter_by(creator=user_id):
        highscores = get_highscores(maze.id)
        highscoreList = create_highscores_object_list(highscores)
        mazes.append({"id": maze.id, "name": maze.name,
                      "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "official": False})
    return mazes
