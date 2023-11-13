from flask import jsonify
from app.models.maze.create_maze_object import create_maze_object
from app.models.maze.get_single_maze import get_single_maze
from db.models import Mazes


def get_single_maze_controller(request):
    maze_id = request.args.get("id")
    maze: type[Mazes] = get_single_maze(maze_id)
    maze_object = create_maze_object(maze)
    return jsonify(maze_object)
