from db.db import db
from db.models import Mazes


def delete_maze(maze: type[Mazes]):
    maze.delete()
    db.session.commit()
