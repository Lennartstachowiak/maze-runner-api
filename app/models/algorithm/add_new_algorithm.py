from db.db import db
from db.models import Algorithms


def add_new_algorithm(new_algorithm: type[Algorithms]):
    new_algorithm.save()
    db.session.commit()
