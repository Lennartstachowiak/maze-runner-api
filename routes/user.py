from flask import jsonify, request, make_response, abort
from db.db import db
from db import models
from flask_bcrypt import Bcrypt
from flask_session import Session
from datetime import date, datetime, timedelta
from scripts.addAlgorithms import addAlgorithms

User = models.User
Algorithms = models.Algorithms
SessionAuth = models.SessionAuth


# @ api.route("/v1/get_all", methods=["GET"])
# def get_all():
#     allUsers = []
#     for user in User.query.all():
#         allUsers.append({
#             "id": user.id,
#             "email": user.email,
#         })
#     return jsonify(allUsers)

def register_user_routes(api):
    bcrypt = Bcrypt(api)

    @api.route("/", methods=["GET"])
    def connect():
        print("lknsfkjnfkj")
        message = "connected"
        print(message)
        return message

    @ api.route("/v1/@me", methods=["GET"])
    def get_current_user():
        user = get_user(request)
        res = {
            "id": user.id,
            "email": user.email
        }
        return jsonify(res)

    @ api.route("/v1/register", methods=["POST"])
    def register_user():

        email = request.json["email"]
        password = request.json["password"]

        user_exists = User.query.filter_by(email=email).first() is not None

        if user_exists:
            return jsonify({"error": "User already exists"}), 409

        # Create User
        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')
        new_user = User(email=email, password=hashed_password)
        #  Add User to db
        db.session.add(new_user)
        db.session.commit()

        # Get User
        user = User.query.filter_by(email=email).first()

        # Add default user algorithms
        userId = user.id
        addAlgorithms(userId)

        sessionData = create_session(user)
        res = make_response()
        res.set_cookie(
            "sessionId", value=sessionData["sessionId"], expires=sessionData["expiryDate"], samesite="None", secure=True, httponly=True)
        return res

    @ api.route("/v1/login", methods=["POST"])
    def login_user():
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

    @ api.route("/v1/logout", methods=["POST"])
    def logout_user():
        sessionId = request.cookies.get('sessionId')
        deleteSession = SessionAuth.query.get(sessionId)
        db.session.delete(deleteSession)
        db.session.commit()
        res = make_response()
        res.delete_cookie('sessionId',)
        return res


def get_user_id(request):
    sessionId = request.cookies.get('sessionId')
    if not sessionId:
        abort(401, "Unauthorized")
    session = SessionAuth.query.filter_by(
        id=sessionId).first()
    session_exists = session is not None
    if not session_exists or is_session_expired(session):
        abort(401, "Unauthorized")
    user_id = SessionAuth.query.get(sessionId).userId
    if not user_id:
        abort(401, "Unauthorized")
    return user_id


def get_user(request):
    user_id = get_user_id(request)
    user = User.query.filter_by(id=user_id).first()
    return user


def is_session_expired(session):
    today = date.today()
    if session.expiryDate <= today:
        session.delete()
        return True
    else:
        return False


def create_session(user):
    # Check if User has session
    if SessionAuth.query.filter_by(userId=user.id).first() is not None:
        session = SessionAuth.query.filter_by(userId=user.id).first()
        print("session", session)
        if is_session_expired(session) is False:
            return {"sessionId": session.id, "expiryDate": session.expiryDate}
    # Create Session
    expiryDate = datetime.today().date() + timedelta(days=7)
    new_session = SessionAuth(userId=user.id, expiryDate=expiryDate)
    print("new_session", new_session)
    # Add session to db
    db.session.add(new_session)
    db.session.commit()
    return {"sessionId": new_session.id, "expiryDate": new_session.expiryDate}
