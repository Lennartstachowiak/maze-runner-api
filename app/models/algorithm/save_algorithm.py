from db.db import db
from db import models

Algorithms = models.Algorithms


def save_algorithm(user_id, algorithm_id, new_code):
    algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
    if (algorithm.userId == user_id):
        algorithm.code = new_code
        db.session.commit()
        return True
    else:
        return False
