from uuid import uuid4
from .db import db, CRUDMixin
from sqlalchemy import UniqueConstraint, CheckConstraint


def get_uuid():
    return uuid4().hex


# To convert sqlalchemy classes to python dict
def to_dict(model_instance, query_instance=None):
    if hasattr(model_instance, "__table__"):
        return {c.name: str(getattr(model_instance, c.name)) for c in model_instance.__table__.columns}
    else:
        cols = query_instance.column_descriptions
        return {cols[i]["name"]: model_instance[i] for i in range(len(cols))}


# To convert python dict to sqlalchemy classes
def from_dict(dict, model_instance):
    for c in model_instance.__table__.columns:
        setattr(model_instance, c.name, dict[c.name])


# class User(db.Model):
#     __tablename__ = "Users"
#     id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
#     number = db.Column(db.String(15), unique=True)
#     password = db.Column(db.Text, nullable=False)
#     first_name = db.Column(db.String(30))
#     last_name = db.Column(db.String(30))
#     street = db.Column(db.String(50))
#     city = db.Column(db.String(50))
#     zip = db.Column(db.String(50))


# If you change modules you have to run
#   ->  flask db migrate -m 'add picture_url to Cookie'
#       flask db upgrade
# Tutorial -> https://codecookies.xyz/flask-2-tutorial/v1/sql-database-setup/
# If error try
#   -> flask db stamp head
class Users(db.Model, CRUDMixin):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.Text, nullable=False)
    algorithms = db.relationship("Algorithms", backref="user", lazy=True)
    highscores = db.relationship("Highscores", backref="user", lazy=True)
    mazes = db.relationship("Mazes", backref="user", lazy=True)
    sessions = db.relationship("SessionAuth", backref="user", lazy=True)
    mazeFollower = db.relationship("MazeFollowers", backref="user", lazy=True)
    followers = db.relationship(
        "UserFollowers",
        foreign_keys="UserFollowers.followerId",
        backref="followers",
        lazy="dynamic",
    )
    follows = db.relationship(
        "UserFollowers",
        foreign_keys="UserFollowers.userId",
        backref="follows",
        lazy="dynamic",
    )


class SessionAuth(db.Model, CRUDMixin):
    __tablename__ = "sessions"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    userId = db.Column(
        db.String(32),
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True,
        index=True,
    )
    expiryDate = db.Column(db.Date())


class Mazes(db.Model, CRUDMixin):
    __tablename__ = "mazes"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.Text, unique=True, nullable=False)
    difficulty = db.Column(db.Enum("Easy", "Medium", "Hard", name="difficulty"), nullable=False)
    imgLink = db.Column(db.Text, nullable=False)
    structure = db.Column(db.Text, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    isTest = db.Column(db.Boolean, default=False)
    creator = db.Column(db.String(32), db.ForeignKey("users.id"), nullable=False, index=True)
    highscores = db.relationship("Highscores", backref="maze", lazy=True)
    maze_follower = db.relationship("MazeFollowers", backref="maze", lazy=True)


class Highscores(db.Model, CRUDMixin):
    __tablename__ = "highscores"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    userId = db.Column(db.String(32), db.ForeignKey("users.id"), nullable=False, index=True)
    mazeId = db.Column(db.String(32), db.ForeignKey("mazes.id"), nullable=False, index=True)
    algorithm_id = db.Column(
        db.String(32),
        db.ForeignKey("algorithms.id"),
        nullable=False,
        index=True,
    )
    score = db.Column(db.Float, nullable=False)


class Algorithms(db.Model, CRUDMixin):
    __tablename__ = "algorithms"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.Text, nullable=False)
    code = db.Column(db.Text, nullable=False)
    userId = db.Column(db.String(32), db.ForeignKey("users.id"), nullable=False, index=True)
    isWorking = db.Column(db.Boolean, default=False)
    highscores = db.relationship("Highscores", backref="algorithm", lazy=True)


class MazeFollowers(db.Model, CRUDMixin):
    __tablename__ = "maze_followers"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    mazeId = db.Column(db.String(32), db.ForeignKey("mazes.id"), nullable=False, index=True)
    followerId = db.Column(db.String(32), db.ForeignKey("users.id"), nullable=False, index=True)
    __table_args__ = (UniqueConstraint("mazeId", "followerId", name="_maze_follower_uc"),)


class UserFollowers(db.Model, CRUDMixin):
    __tablename__ = "user_followers"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    userId = db.Column(db.String(32), db.ForeignKey("users.id"), nullable=False, index=True)
    followerId = db.Column(db.String(32), db.ForeignKey("users.id"), nullable=False, index=True)
    __table_args__ = (
        UniqueConstraint("userId", "followerId", name="_user_follower_uc"),
        CheckConstraint("userId!=followerId", name="_user_follower_check_"),
    )
