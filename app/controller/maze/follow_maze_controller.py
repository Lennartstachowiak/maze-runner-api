from flask import jsonify
from app.models.maze.follow_maze import follow_maze
from app.models.user.get_user import get_user
from flask import abort


def follow_maze_controller(request):
    try:
        user = get_user(request)
        user_id = user.id
        maze_id = request.json["mazeId"]
        register_data = follow_maze(user_id, maze_id)
        if register_data == 409:
            abort(409, "Conflict")
        response = {"status": 200}
        return jsonify(response)
    except Exception:
        abort(400, "Internal server error")
