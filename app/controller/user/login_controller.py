from flask import abort, jsonify, make_response
from flask_bcrypt import Bcrypt
from app.controller.user.session_controller import session_controller
from app.models.user.login_user import login_user


def login_user_controller(request, api):
    bcrypt = Bcrypt(api)
    email = request.json["email"]
    password = request.json["password"]

    user = login_user(bcrypt, email, password)
    if not user:
        abort(401, "Unauthorized")

    session_data = session_controller(user)

    res = make_response()
    res.set_cookie(
        "session_id_maze_runner", value=session_data["session_id_maze_runner"], expires=session_data["expiryDate"], samesite="None", secure=True, httponly=True)
    return res
