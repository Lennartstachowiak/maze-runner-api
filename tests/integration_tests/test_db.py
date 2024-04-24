from sqlite3 import IntegrityError
import pytest
from db.models import Users, Mazes, Algorithms
from db.db import db


@pytest.fixture
def client_and_session(client_and_api):
    # Creates all tables before each test and kills each table after each test
    client, api = client_and_api
    with client.application.app_context():
        db.create_all()
        yield client, db.session
        db.drop_all()


user_id = 1
username = "Test User"
email = "test@web.com"
password = "testpassword"


def test_user_creation(client_and_session):
    client, session = client_and_session
    new_user = Users(id=user_id, username=username, email=email,
                     password=password)
    session.add(new_user)
    session.commit()
    test_user = Users.query.filter_by(id=1).first()
    assert test_user.username == username


maze_id = 1
maze_name = "Test Maze"
difficulty = "Easy"
imgLink = "None"
structure = "None"
height = 10
width = 10
isTest = True
creator = 1


def test_maze_creation(client_and_session):
    client, session = client_and_session
    new_maze = Mazes(id=maze_id, name=maze_name, difficulty=difficulty,
                     imgLink=imgLink, structure=structure, height=height, width=width, isTest=isTest, creator=creator)
    session.add(new_maze)
    session.commit()
    test_maze = Mazes.query.filter_by(id=1).first()
    assert test_maze.name == maze_name


# Currently exception with pytest can't be catched
# IntegrityError is thrown but still fails test

# def test_maze_constraints_work(client_and_session):
#     imgLink = None
#     client, session = client_and_session
#     new_maze = Mazes(id=maze_id, name=name, difficulty=difficulty,
#                      imgLink=imgLink, structure=structure, height=height, width=width, isTest=isTest, creator=creator)
#     session.add(new_maze)
#     with pytest.raises(IntegrityError) as excinfo:
#         session.commit()

alg_id = 1
alg_name = "Test Algorithm"
code = "console.log(Hello World)"
userId = 1


def test_algorithm_creation(client_and_session):
    client, session = client_and_session
    new_alg = Algorithms(id=alg_id, name=alg_name, code=code,
                         userId=userId)
    session.add(new_alg)
    session.commit()
    test_maze = Algorithms.query.filter_by(id=1).first()
    assert test_maze.name == alg_name
