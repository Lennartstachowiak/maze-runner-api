from flask import jsonify
from db import models
from services.maze.get_highscores import get_highscores
from services.maze.get_single_maze import get_single_maze

Mazes = models.Mazes


def get_single_maze_controller(request):
    maze_id = request.args.get("id")
    maze = get_single_maze(maze_id)
    return jsonify(maze)
