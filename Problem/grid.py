from random import randint, choice
from phase1.main.UninformedSearch.BFS import breadth_first_search


# reverse (to correct form) the path returned as it is returned reversed
def reconstruct_path(path, start, goal):
    current = goal
    result_path = []
    while current is not None:
        result_path.append(current)
        current = path[current]
    result_path.reverse()
    return result_path


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
    grid = {}

    # create a grid of Nodes
    for x in range(row):
        for y in range(column):
            grid[(x, y)] = Node((x, y))

    for x in range(row):
        for y in range(column):
            current_node = grid[(x, y)]
            # set neighbors
            if current_node.passable:
                neighbors = [
                    (x, y - 1),  # up
                    (x, y + 1),  # down
                    (x - 1, y),  # left
                    (x + 1, y),  # right
                    (x - 1, y - 1),  # top-left
                    (x - 1, y + 1),  # top-right
                    (x + 1, y - 1),  # bottom-left
                    (x + 1, y + 1)  # bottom-right
                ]
                # make sure node doesnt go over the boundries
                for x_limit, y_limit in neighbors:
                    if 0 <= x_limit < row and 0 <= y_limit < column:
                        neighbor_node = grid.get((x_limit, y_limit))
                        # append children
                        if neighbor_node and neighbor_node.passable:
                            current_node.children.append(neighbor_node)

    # initalize start and goal randomly
    start_position = (randint(0, row - 1), randint(0, column - 1))
    goal_position = (randint(0, row - 1), randint(0, column - 1))

    # make sure goal != start
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

    # if too many failed obstacles > 200 then quit and get satisfied with the current number of obstales
    while obstacles_placed < obstacle_quantity and failed_attempts < 200:
        x = randint(0, row - 1)
        y = randint(0, column - 1)
        node = grid[(x, y)]

        # set obstacle and make se sure it is not goal neither start
        if node.passable and not (node.start and node.goal):
            node.passable = False
            node.cost = float('inf')  # set cost to infinty to help with cost calculating algorithms

            # back tracking using bfs to make sure a path still exists
            is_path_found = breadth_first_search(grid)

            if is_path_found:
                obstacles_placed += 1
            # if no path exists then remove the goal blocking obstacle
            else:
                node.passable = True
                failed_attempts += 1

    return grid


def path_cost(grid, row, column):
    for x in range(row):
        for y in range(column):
            node = grid[(x, y)]
            # randomly assign costs
            if node.passable and not (node.goal and node.start):
                node.cost = choice([1, 2])  # 1 = Highway, 2 = Narrow way
    return grid
