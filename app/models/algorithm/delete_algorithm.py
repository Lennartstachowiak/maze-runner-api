from db.db import db
from db.models import Algorithms


def delete_algorithm(algorithm: type[Algorithms]):
    algorithm.delete()
    db.session.commit()
