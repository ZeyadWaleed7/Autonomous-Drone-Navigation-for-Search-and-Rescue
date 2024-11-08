from random import randint

def grid_init(row, column):
    grid = {}
    for x in range(row):
        for y in range(column):
            position = (x, y)
            grid[position] = {'position': position, 'passable': True, 'cost': 1, 'goal': False, 'start': False}

    grid[( randint(0, column - 1),  randint(0, row - 1))]['start'] = True
    grid[( randint(0, column - 1),  randint(0, row - 1))]['goal'] = True

    return grid

def create_obstacle(grid, row, column):
    obstacles_placed = 0
    obstacle_quantity = int(0.2 * (row * column))

    while obstacles_placed < obstacle_quantity:
        x_column = randint(0, column - 1)
        y_row = randint(0, row - 1)

        if not grid[(x_column, y_row)]['start'] and not grid[(x_column, y_row)]['goal'] and grid[(x_column, y_row)]['passable']:
            grid[(x_column, y_row)]['passable'] = False
            grid[(x_column, y_row)]['cost'] = 0

            # Placeholder for pathfinding check (DFS/BFS)
            is_path_found = True  # Replace this with actual DFS/BFS check later

            if is_path_found:
                obstacles_placed += 1
            else:
                grid[(x_column, y_row)]['passable'] = True

    return grid


#tesssttt

# row, column = 50, 50
# grid = grid_init(row, column)

# grid = create_obstacle(grid, row, column)

# for position in [(0, 0), (24, 24), (49, 49)]:
#     print(f"Position {position}: {grid[position]}")
