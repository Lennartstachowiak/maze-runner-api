from api import create_api
from db.models import Algorithms

api = create_api()
api.app_context().push()

algorithmList = [
    {"name": "Depth-First Search", "code": """
    (x, y) = node
    cell = maze.structure[x][y]
    if type(cell) == dict:
        cell = Cell(**cell)
    if cell.goal:
        solution.append(node)
        return True
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # W, N, E, S
    for direction, (dx, dy) in zip(['west', 'north', 'east', 'south'], directions):
        next_x, next_y = x + dx, y + dy
        if (0 <= next_x < maze.height and
            0 <= next_y < maze.width and
            not (next_x, next_y) in visited and
                getattr(cell, direction) == 0):
            visited.append((next_x, next_y))
            if dfs((next_x, next_y), maze, solution, visited):
                solution.append(node)
                return True
    return False
     """},
    {"name": "Breadth-First Search", "code": """
    queue = deque([(node, [])])

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.append(node)

        (x, y) = node
        cell = maze.structure[x][y]
        if type(cell) == dict:
            cell = Cell(**cell)

        if cell.goal:
            solution.extend(path + [node])
            return True

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # W, N, E, S

        for direction, (dx, dy) in zip(['west', 'north', 'east', 'south'], directions):
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < maze.height and
                0 <= next_y < maze.width and
                (next_x, next_y) not in visited and
                    getattr(cell, direction) == 0):

                queue.append(((next_x, next_y), path + [node]))

    return False
     """},
    {"name": "Dijkstra's Algorithm", "code": "CODE"},
    {"name": "A* Algorithm", "code": "CODE"},
    {"name": "Greedy Best-First Search", "code": "CODE"},
    {"name": "Bellman Ford Algorithm", "code": "CODE"},
]

for algorithm in algorithmList:
    new_algorithm = Algorithms(name=algorithm["name"], code=algorithm["code"])
    new_algorithm.save()
