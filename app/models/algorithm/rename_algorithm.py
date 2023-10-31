from db.db import db
from db import models

Algorithms = models.Algorithms


def rename_algorithm(user_id, algorithm_id, new_name):
    algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
    if (algorithm.userId == user_id):
        algorithm.name = new_name
        db.session.commit()
        return True
    else:
        return False
