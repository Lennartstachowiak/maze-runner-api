from flask import jsonify, make_response
from flask_bcrypt import Bcrypt
from app.models.user.register_user import register_user


def register_user_controller(request, api):
    bcrypt = Bcrypt(api)
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    register_data = register_user(bcrypt, username, email, password)
    if register_data is 409:
        return jsonify({"error": "User already exists"}), 409
    else:
        session_data = register_data

    res = make_response()
    res.set_cookie(
        "session_id_maze_runner", value=session_data["session_id_maze_runner"], expires=session_data["expiryDate"], samesite="Strict", secure=True, httponly=True)
    return res
