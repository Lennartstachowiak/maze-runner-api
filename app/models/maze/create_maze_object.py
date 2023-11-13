from app.models.maze.get_highscores import get_highscores
from db.models import Mazes


def create_maze_object(maze: type[Mazes]):
    highscoreList = get_highscores(maze.id)
    maze = {"id": maze.id, "name": maze.name,
            "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscoreList, "structure": maze.structure}
    return maze
