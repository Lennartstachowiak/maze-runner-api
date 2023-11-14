from db.db import db
from db.models import Mazes


def add_maze(new_maze: type[Mazes]):
    new_maze.save()
    db.session.commit()
