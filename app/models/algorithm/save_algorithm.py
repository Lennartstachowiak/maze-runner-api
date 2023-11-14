import string
from db.db import db
from db.models import Algorithms


def save_algorithm(algorithm: type[Algorithms], new_code: string):
    algorithm.code = new_code
    db.session.commit()
