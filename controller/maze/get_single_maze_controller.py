from flask import jsonify
from db import models
from services.maze.get_single_maze import get_single_maze


def get_single_maze_controller(request):
    maze_id = request.args.get("id")
    maze = get_single_maze(maze_id)
    return jsonify(maze)
