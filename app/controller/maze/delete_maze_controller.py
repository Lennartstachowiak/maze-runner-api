from flask import abort, jsonify
from app.models.maze.delete_maze import delete_maze
from app.models.user.get_user import get_user_id


def delete_maze_controller(request):
    user_id = get_user_id(request)
    maze_id = request.json["mazeId"]
    isDeleted = delete_maze(user_id, maze_id)
    if isDeleted:
        return jsonify("Maze deleted!")
    else:
        abort(401, "Unauthorized")
