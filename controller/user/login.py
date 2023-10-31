from flask import jsonify, make_response
from db import models
from services.user.create_session import create_session
from flask_bcrypt import Bcrypt

User = models.User


def login_user(request, api):
    bcrypt = Bcrypt(api)
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        print("user is none")
        return jsonify({"error": "Unauthorized"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        print("Unauthorized")
        return jsonify({"error": "Unauthorized"}), 401

    sessionData = create_session(user)
    res = make_response()
    res.set_cookie(
        "sessionId", value=sessionData["sessionId"], expires=sessionData["expiryDate"], samesite="None", secure=True, httponly=True)
    return res
