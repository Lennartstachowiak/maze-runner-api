from flask import jsonify, make_response
from flask_bcrypt import Bcrypt
from app.models.user.login_user import login_user


def login_user_controller(request, api):
    bcrypt = Bcrypt(api)
    email = request.json["email"]
    password = request.json["password"]

    login_data = login_user(bcrypt, email, password)
    if login_data is False:
        return jsonify({"error": "Unauthorized"}), 401
    else:
        session_data = login_data

    res = make_response()
    res.set_cookie(
        "sessionId", value=session_data["sessionId"], expires=session_data["expiryDate"], samesite="None", secure=True, httponly=True)
    return res