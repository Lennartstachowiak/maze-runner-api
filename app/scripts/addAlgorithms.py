from db.models import Algorithms

default_algorithm = """function returnSolution(node, maze) {
    const solution = [];
    const visited = [];

    function solveMaze(node) {

    }

    solveMaze(node);
    return JSON.stringify([solution, visited])
}
"""

algorithmList = [
    {
        "name": "Depth-First Search",
        "code": """function returnSolution(node, maze) {
    const solution = [];
    const visited = [];

    function solveMaze(node) {
        const [x, y] = node;
        const cell = maze.structure[x][y];

        visited.push(node);

        if (cell.goal) {
            solution.push(node);
            return true;
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
                if (solveMaze([next_x, next_y])) {
                    solution.push(node);
                    return true;
                }
            }
        }

        return false;
    }

    solveMaze(node);
    return JSON.stringify([solution, visited])
}
""",
    },
    {
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
    },
]


def addAlgorithms(id):
    for algorithm in algorithmList:
        new_algorithm = Algorithms(
            name=algorithm["name"],
            code=algorithm["code"],
            userId=id,
            isWorking=True,
        )
        new_algorithm.save()
