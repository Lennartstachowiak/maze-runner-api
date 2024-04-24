from db.db import db
from db.models import Users, SessionAuth, Algorithms
import subprocess
import datetime


def create_test_users():
    new_user_one = Users(id=100000, username="User One",
                         email="one@web.com", password="password")
    new_user_two = Users(id=100001, username="User Two",
                         email="two@web.com", password="password")
    new_user_three = Users(id=100002, username="User Three",
                           email="three@web.com", password="password")
    db.session.add(new_user_one)
    db.session.add(new_user_two)
    db.session.add(new_user_three)
    db.session.commit()


def create_test_session():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    user_one_session = SessionAuth(id=1, userId=100000, expiryDate=tomorrow)
    user_two_session = SessionAuth(id=2, userId=100001, expiryDate=tomorrow)
    db.session.add(user_one_session)
    db.session.add(user_two_session)
    db.session.commit()


def create_test_algorithm():
    user_one_algorithm = Algorithms(
        id=1, userId=100000, name='User One Algorithm', code='console.log(Hello World)', isWorking=True)
    user_two_algorithm = Algorithms(
        id=2, userId=100001, name='User Two Algorithm', code='console.log(Hello World)', isWorking=True)
    user_three_algorithm = Algorithms(
        id=3, userId=100002, name='User Three Algorithm', code='console.log(Hello World)', isWorking=True)
    db.session.add(user_one_algorithm)
    db.session.add(user_two_algorithm)
    db.session.add(user_three_algorithm)
    db.session.commit()


def create_test_mazes():
    # We already have a script for that
    subprocess.run(["python", "-m" "app.scripts.addDummyDataMazeDB"])


def create_test_highscores():
    # We already have a script for that
    subprocess.run(["python", "-m" "app.scripts.addDummyDataHighscoresDB"])


def create_test_data():
    create_test_users()
    create_test_session()
    create_test_algorithm()
    create_test_mazes()
    create_test_highscores()
