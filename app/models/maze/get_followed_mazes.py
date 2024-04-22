from app.models.maze.create_maze_object import create_maze_object
from app.models.maze.get_single_maze import get_single_maze
from db.models import Users, MazeFollowers, Mazes


def get_followed_mazes(user: Users):
    mazes_join = MazeFollowers.query.join(
        Mazes, MazeFollowers.mazeId == Mazes.id
    ).filter(MazeFollowers.followerId == user.id).all()
    maze_list = []
    for maze in mazes_join:
        maze_id = maze.maze.id
        maze = get_single_maze(maze_id)
        maze_object = create_maze_object(maze)
        maze_list.append(maze_object)
    return maze_list
