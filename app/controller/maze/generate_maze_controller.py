from flask import jsonify
from app.models.maze.generate_maze import generate_maze
from app.models.user.get_user import get_user_id


def generate_maze_controller(request):
    user_id = get_user_id(request)
    maze_name = request.json["mazeName"]
    maze_size = request.json["mazeSize"]
    isGenerated = generate_maze(user_id, maze_name, maze_size)
    if isGenerated:
        return jsonify("New maze generated!")
