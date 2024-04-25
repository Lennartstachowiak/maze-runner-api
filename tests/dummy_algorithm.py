from db.models import Algorithms


def get_dummy_algorithm():
    algorithm_object = {
        "name": "Breadth-First Search",
        "code": """function returnSolution(node, maze) {
    const solution = [];
    const visited = [];

    function solveMaze(node) {
        const queue = [];
        queue.push({
            position: node,
            parent: null
            });

        while (queue.length > 0) {
            const currentNode = queue.shift();
            const [x, y] = currentNode.position;
            const cell = maze.structure[x][y];

            visited.push(currentNode.position);

            if (cell.goal) {
                let pathNode = currentNode;
                while (pathNode !== null) {
                    solution.unshift(pathNode.position);
                    pathNode = pathNode.parent;
                }
                break;
            }

            const directions = ['west', 'north', 'east', 'south'];
            const deltas = [[0, -1], [-1, 0], [0, 1], [1, 0]];

            for (let i = 0; i < directions.length; i++) {
                const direction = directions[i];
                const [dx, dy] = deltas[i];
                const next_x = x + dx;
                const next_y = y + dy;

                if (
                    next_x >= 0 && next_x < maze.height &&
                    next_y >= 0 && next_y < maze.width &&
                    !visited.some(([nx, ny]) => nx === next_x && ny === next_y) &&
                    cell[direction] === 0
                ) {
                    const neighborNode = {
                        position: [next_x, next_y],
                        parent: currentNode
                    };
                    queue.push(neighborNode);
                }
            }
        }
    }

    solveMaze(node);
    return JSON.stringify([solution, visited])
}
""",
    }
    algorithm = Algorithms(
        id=100,
        name=algorithm_object["name"],
        code=algorithm_object["code"],
        user_id=0,
        is_working=True,
    )
    return algorithm
