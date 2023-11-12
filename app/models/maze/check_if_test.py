from db.models import Mazes


def check_if_test(maze_id):
    # Get Maze
    maze_object = Mazes.query.filter_by(id=maze_id).first()
    is_test = maze_object.isTest
    return is_test
