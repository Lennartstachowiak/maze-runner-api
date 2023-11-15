from flask import jsonify
from app.models.maze.add_maze import add_maze
from app.models.maze.generate_maze import MazeCreationFacade
from app.models.user.get_user import get_user_id
from db.db import db
from db.models import Mazes


def generate_maze_controller(request):
    user_id = get_user_id(request)
    maze_name = request.json["mazeName"]
    maze_size = request.json["mazeSize"]
    type = request.json["generateType"]
    new_maze: type[Mazes] = MazeCreationFacade().get_generated_maze(
        user_id, maze_name, maze_size, type)
    add_maze(new_maze)
    return jsonify("New maze generated!")
