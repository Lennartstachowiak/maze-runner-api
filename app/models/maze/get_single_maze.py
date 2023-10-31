from db import models
from app.models.maze.get_highscores import get_highscores

Mazes = models.Mazes


def get_single_maze(maze_id):
    maze = Mazes.query.filter_by(id=maze_id).first()
    highscoreList = get_highscores(maze_id)
    maze = {"id": maze.id, "name": maze.name,
            "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "structure": maze.structure}

    return maze
