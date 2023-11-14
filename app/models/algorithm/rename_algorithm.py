import string
from db.db import db
from db.models import Algorithms


def rename_algorithm(algorithm: type[Algorithms], new_name: string):
    algorithm.name = new_name
    db.session.commit()
