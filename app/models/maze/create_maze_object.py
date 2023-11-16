from app.models.maze.get_highscores import get_highscores
from app.models.maze.get_highscores_object_list import create_highscores_object_list
from db.models import Mazes


def create_maze_object(maze: type[Mazes]):
    highscores = get_highscores(maze.id)
    highscoreList = create_highscores_object_list(highscores)
    maze = {"id": maze.id, "name": maze.name,
            "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "structure": maze.structure}
    return maze
