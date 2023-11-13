from db import models

Mazes = models.Mazes
Algorithms = models.Algorithms
algorithm_schema_code = """
function returnSolution(node, maze) {
    const solution = [];
    const visited = [];

    function solveMaze(node) {
    
    }

    solveMaze(node);
    return JSON.stringify([solution, visited])
}
""".strip() + '\n'


def get_new_algorithm(user_id):
    algorithms_count = len(
        Algorithms.query.filter_by(userId=user_id).all())+1
    new_algorithm = Algorithms(
        name=f"Algorithm {algorithms_count}", code=algorithm_schema_code, userId=user_id)
    return new_algorithm
