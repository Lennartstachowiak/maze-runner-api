from db import models

Algorithms = models.Algorithms


def get_algorithms(user_id):
    algorithms = Algorithms.query.filter_by(user_id=user_id).all()
    return algorithms
