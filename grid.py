from random import randint, choice


def grid_init(row, column):
    grid = {}
    for x in range(row):
        for y in range(column):
            position = (x, y)
            grid[position] = {'passable': True, 'cost': 1, 'goal': False, 'start': False}

# impmlented from stack overflow to enure that start != goal
    start_position = (randint(0, row - 1), randint(0, column - 1))
    while True:
        goal_position = (randint(0, row - 1), randint(0, column - 1))
        if goal_position != start_position:
            break

    grid[start_position]['start'] = True
    grid[start_position]['cost'] = 0

    grid[goal_position]['cost'] = 0
    grid[goal_position]['goal'] = True

    return grid, start_position, goal_position

def create_obstacle(grid, row, column):
    obstacles_placed = 0
    obstacle_quantity = int(0.2 * (row * column))
    failed = 0

    #to avoid infinte loop
    while obstacles_placed < obstacle_quantity and failed < 200:
        x_column = randint(0, column - 1)
        y_row = randint(0, row - 1)

        if not grid[(x_column, y_row)]['start'] and not grid[(x_column, y_row)]['goal'] and grid[(x_column, y_row)]['passable']:
            grid[(x_column, y_row)]['passable'] = False
            grid[(x_column, y_row)]['cost'] = 0

            # Placeholder for pathfinding check (DFS)
            is_path_found = True  # Replace this with actual DFS check later

            if is_path_found:
                obstacles_placed += 1
            else:
                grid[(x_column, y_row)]['passable'] = True
                failed += 1

    return grid

def path_cost(grid, row, column):
    for x in range(row):
        for y in range(column):
            # Check if the cell is passable and not an obstacle (cost should not be 0)
            if grid[(x, y)]['passable'] and grid[(x, y)]['cost'] != 0:
                grid[(x, y)]['cost'] = choice([1, 2])  # Randomly set the cost to 1 or 2
    return grid

#tesssttt

# row, column = 50, 50
# grid = grid_init(row, column)

# grid = create_obstacle(grid, row, column)

# for position in [(0, 0), (24, 24), (49, 49)]:
#     print(f"Position {position}: {grid[position]}")




