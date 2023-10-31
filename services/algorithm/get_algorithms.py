from db import models

Algorithms = models.Algorithms


def get_algorithms(user_id):
    algorithmList = []
    for algorithm in Algorithms.query.filter_by(userId=user_id).all():
        algorithmList.append(
            {"id": algorithm.id, "name": algorithm.name, "code": algorithm.code, "isWorking": algorithm.isWorking})
    return algorithmList
