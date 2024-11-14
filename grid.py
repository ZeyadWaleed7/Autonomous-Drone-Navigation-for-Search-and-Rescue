from random import randint, choice
from BFS import breadth_first_search
class Node:
    def __init__(self, position, passable=True, cost=1):
        self.position = position
        self.passable = passable
        self.cost = cost
        self.children = []
        self.start = False
        self.goal = False

def grid_init(row, column):
    # Step 1: Create nodes for each cell and store in a dictionary
    grid = {(x, y): Node((x, y)) for x in range(row) for y in range(column)}

    # Step 2: Connect nodes to their valid neighbors
    for x in range(row):
        for y in range(column):
            current_node = grid[(x, y)]
            if current_node.passable:
                neighbors = [
                    (x, y - 1),  # up
                    (x, y + 1),  # down
                    (x - 1, y),  # left
                    (x + 1, y)   # right
                ]
                for x_limit, y_limitt in neighbors:
                    if 0 <= x_limit < row and 0 <= y_limitt < column:
                        neighbor_node = grid[(x_limit, y_limitt)]
                        if neighbor_node.passable:
                            current_node.children.append(neighbor_node)

    # Step 3: Define start and goal positions
    start_position = (randint(0, row - 1), randint(0, column - 1))
    while True:
        goal_position = (randint(0, row - 1), randint(0, column - 1))
        if goal_position != start_position:
            break

    # Set start and goal attributes for selected nodes
    grid[start_position].start = True
    grid[start_position].cost = 0
    grid[goal_position].goal = True
    grid[goal_position].cost = 0

    return grid, start_position, goal_position

def create_obstacle(grid, row, column):
    obstacles_placed = 0
    obstacle_quantity = int(0.2 * (row * column))
    failed_attempts = 0

    while obstacles_placed < obstacle_quantity and failed_attempts < 200:
        x = randint(0, row - 1)
        y = randint(0, column - 1)
        node = grid[(x, y)]

        if not node.start and not node.goal and node.passable:
            node.passable = False
            node.cost = 0

            # Placeholder for DFS path-checking
            is_path_found = breadth_first_search(grid)

            if is_path_found:
                obstacles_placed += 1
            else:
                print("erooooong ")
                node.passable = True
                failed_attempts += 1

    return grid

def path_cost(grid, row, column):
    for x in range(row):
        for y in range(column):
            node = grid[(x, y)]
            if node.passable and node.cost != 0:
                node.cost = choice([1, 2])
    return grid

# Test case 2: Grid with a blocked path
row, column = 5, 5
grid, start_position, goal_position = grid_init(row, column)
grid = path_cost(grid, row, column)

# Place an obstacle at (2, 2)
grid[(2, 2)].passable = False
grid[(2, 2)].cost = 0

# Perform DFS path checking (this should return False due to the obstacle)
path_exists = breadth_first_search(grid)







print(f"Path found (Single obstacle): {path_exists}")
