from db.models import Mazes


def delete_maze(user_id, maze_id):
    maze = Mazes.query.filter_by(id=maze_id, creator=user_id).first()
    if not maze:
        return False
    maze.delete()
    return True
