from flask import abort, jsonify, make_response
from flask_bcrypt import Bcrypt
from app.models.user.login_user import login_user


def login_user_controller(request, api):
    bcrypt = Bcrypt(api)
    email = request.json["email"]
    password = request.json["password"]

    login_data = login_user(bcrypt, email, password)
    if login_data is False:
        abort(401, "Unauthorized")
    else:
        session_data = login_data

    res = make_response()
    res.set_cookie(
        "session_id_maze_runner", value=session_data["session_id_maze_runner"], expires=session_data["expiryDate"], samesite="None", secure=True, httponly=True)
    return res
