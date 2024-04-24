def create_algorithm_object(algorithm):
    algorithm_object = {
        "id": algorithm.id,
        "name": algorithm.name,
        "code": algorithm.code,
    }
    return algorithm_object
