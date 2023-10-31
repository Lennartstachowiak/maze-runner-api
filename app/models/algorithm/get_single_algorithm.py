from db import models

Algorithms = models.Algorithms


def get_single_algorithm(algorithm_id):
    algorithm = Algorithms.query.filter_by(id=algorithm_id).first()
    algorithm_object = {"id": algorithm.id,
                        "name": algorithm.name, "code": algorithm.code}
    return algorithm_object
