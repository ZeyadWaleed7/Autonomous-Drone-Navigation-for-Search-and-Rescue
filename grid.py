from random import randint, choice

from BFS import breadth_first_search


class Node:
    def __init__(self, position, cost=1):
        self.position = position
        self.passable = True
        self.cost = cost
        self.children = []
        self.start = False
        self.goal = False
        self.heuristic = None
    def __lt__(self, other):
        return self.heuristic < other.heuristic


def grid_init(row, column):
    # Step 1: Create nodes for each cell and store in a dictionary
    grid = {}

    for x in range(row):
        for y in range(column):
            grid[(x, y)] = Node((x, y))

    # Step 2: Connect nodes to their valid neighbors
    for x in range(row):
        for y in range(column):
            current_node = grid[(x, y)]

            if current_node.passable:
                neighbors = [
                    (x, y - 1),  # up
                    (x, y + 1),  # down
                    (x - 1, y),  # left
                    (x + 1, y)  # right
                ]

                for x_limit, y_limit in neighbors:
                    if 0 <= x_limit < row and 0 <= y_limit < column:
                        neighbor_node = grid.get((x_limit, y_limit))

                        if neighbor_node and neighbor_node.passable:
                            current_node.children.append(neighbor_node)

    # Step 3: Define start and goal positions
    start_position = (randint(0, row - 1), randint(0, column - 1))
    goal_position = (randint(0, row - 1), randint(0, column - 1))

    while goal_position == start_position:
        goal_position = (randint(0, row - 1), randint(0, column - 1))

    # Set start and goal attributes for selected nodes
    grid[start_position].start = True
    grid[goal_position].goal = True

    return grid, start_position, goal_position


def create_obstacle(grid, row, column):
    obstacles_placed = 0
    obstacle_quantity = int(0.2 * (row * column))
    failed_attempts = 0

    while obstacles_placed < obstacle_quantity and failed_attempts < 200:
        x = randint(0, row - 1)
        y = randint(0, column - 1)
        node = grid[(x, y)]

        if node.passable and not (node.start and node.goal) :
            node.passable = False
            node.cost = float('inf')

            # Placeholder for DFS path-checking (update this if DFS is implemented)
            # is_path_found = True  # Implement DFS or other pathfinding logic if needed
            is_path_found = breadth_first_search(grid)

            if is_path_found:
                obstacles_placed += 1
            else:
                node.passable = True
                failed_attempts += 1

    return grid


def path_cost(grid, row, column):
    for x in range(row):
        for y in range(column):
            node = grid[(x, y)]
            if node.passable and not (node.goal and  node.start):
                node.cost = choice([1, 2])  # 1 = Highway, 2 = Narrow way
    return grid