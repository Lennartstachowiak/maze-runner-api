from app.models.maze.get_maze_highscores import get_maze_highscores
from db.models import Mazes


def create_maze_object(maze: type[Mazes]):
    highscores = get_maze_highscores(maze.id)
    maze = {"id": maze.id, "name": maze.name,
            "difficulty": maze.difficulty, "imgLink": maze.imgLink, "highscores": highscores, "structure": maze.structure}
    return maze
