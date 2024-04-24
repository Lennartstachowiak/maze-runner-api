from sqlalchemy.exc import IntegrityError
from db import models
from db.db import db

MazeFollowers = models.MazeFollowers


def follow_maze(user_id, maze_id):
    try:
        new_maze_follow = MazeFollowers(maze_id=maze_id, follower_id=user_id)
        db.session.add(new_maze_follow)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return 409
