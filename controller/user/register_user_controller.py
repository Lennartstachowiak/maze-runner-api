from flask import jsonify, make_response
from db import models
from flask_bcrypt import Bcrypt
from services.user.register_user import register_user

User = models.User


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
        "sessionId", value=session_data["sessionId"], expires=session_data["expiryDate"], samesite="None", secure=True, httponly=True)
    return res
