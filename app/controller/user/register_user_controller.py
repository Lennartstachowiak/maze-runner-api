from flask import abort, make_response
from flask_bcrypt import Bcrypt
from app.models.user.check_if_valid_register import check_if_valid_register
from app.models.user.register_user import register_user


def register_user_controller(request, api):
    bcrypt = Bcrypt(api)
    username = request.json.get("username")
    email = request.json.get("email")
    email = email.lower()
    password = request.json.get("password")
    repeated_password = request.json.get("repeatedPassword")

    are_credentials_valid = check_if_valid_register(
        email, password, repeated_password)

    if not are_credentials_valid:
        abort(401)

    register_data = register_user(bcrypt, username, email, password)
    if register_data == 409:
        abort(409)

    session_data = register_data

    res = make_response()
    res.set_cookie(
        "session_id_maze_runner", value=session_data["session_id_maze_runner"], expires=session_data["expiryDate"], samesite="None", secure=True, httponly=True)
    return res
