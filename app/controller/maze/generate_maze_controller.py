from flask import abort, jsonify
from app.models.maze.add_maze import add_maze
from app.models.maze.check_if_maze_available import check_if_maze_available
from app.models.maze.generate_maze import MazeCreationFacade
from app.models.user.get_user import get_user_id
from db.models import Mazes


def generate_maze_controller(request):
    user_id = get_user_id(request)
    maze_name = request.json["mazeName"]
    maze_size = request.json["mazeSize"]
    type = request.json["generateType"]
    is_maze_available = check_if_maze_available(maze_name)
    if not is_maze_available:
        abort(409)
    new_maze: Mazes = MazeCreationFacade().get_generated_maze(user_id, maze_name, maze_size, type)
    add_maze(new_maze)
    return jsonify("New maze generated!")
