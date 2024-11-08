from random import randint


def grid_init(row, column):
    grid = {}
    for x in range (row):
        for y in range (column):
            position = (x, y)
            # Initialize the grid with no obstacles and on the Highway
            grid[position] = {'passable' : True, 'cost' : 1,'goal' : False,'start':False}
    return grid

def create_obstacle(grid):
    obstacles_placed = 0
    row = len(grid)
    column = len(grid[0])
    obstacle_quantity = 0.2 * (row*column)
    while obstacles_placed < obstacle_quantity :
        x_column = randint(0,column-1)
        y_row = randint(0,row-1)
        if not grid[y_row,x_column]['start'] and not grid[y_row,x_column]['goal'] and grid[y_row,x_column]['passable'] :
            grid[x_column,y_row]['passable']=False

            # is_path_found =  DFS(grid) to goal
            is_path_found =  True # test till DFS is done
            if is_path_found
