from db.models import Algorithms


def get_algorithms_objects(algorithms: type[Algorithms]):
    algorithm_object_list = []
    for algorithm in algorithms:
        algorithm_object_list.append(
            {
                "id": algorithm.id,
                "name": algorithm.name,
                "code": algorithm.code,
                "isWorking": algorithm.is_working,
            }
        )
    return algorithm_object_list
