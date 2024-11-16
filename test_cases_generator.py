import random
from grid import grid_init, create_obstacle, path_cost


def generate_random_grid():
    # Generate random grid size
    rows = random.randint(5, 15)
    columns = random.randint(5, 15)

    # Initialize grid
    grid, start_position, goal_position = grid_init(rows, columns)

    # Add obstacles
    grid = create_obstacle(grid, rows, columns)

    # Randomly assign path costs
    grid = path_cost(grid, rows, columns)

    # Return the generated grid
    return grid, start_position, goal_position
