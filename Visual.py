from heuristic_function import heuristic_function  # Import the specific function
from simulated_Annealing import simulated_annealing
from hill_climbing import hill_climbing
from A_Star import a_star
from genatic import genetic_algorithm
from grid import grid_init, create_obstacle, path_cost, reconstruct_path
import time
import tracemalloc
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm


def visualize_path(grid, path, start, goal):
    # Determine grid dimensions
    max_row = max(key[0] for key in grid) + 1
    max_col = max(key[1] for key in grid) + 1

    # Initialize grid array with a default value
    grid_array = np.zeros((max_row, max_col), dtype=int)

    # Mark obstacles, path, start, and goal
    for (x, y), node in grid.items():
        if not node.passable:
            grid_array[x, y] = 2  # Mark as obstacle
        elif node.cost == 1:
            grid_array[x, y] = 0  # Mark as highway (cost 1)
        elif node.cost == 2:
            grid_array[x, y] = 1  # Mark as narrow way (cost 2)

    for (x, y) in path:
        if (x, y) != start and (x, y) != goal:
            grid_array[x, y] = 3  # Mark path

    grid_array[start[0], start[1]] = 4  # Mark start
    grid_array[goal[0], goal[1]] = 5    # Mark goal

    # Define colormap and normalization
    cmap = ListedColormap(['lightblue', 'pink', 'black', 'yellow', 'red', 'green'])
    bounds = [0, 1, 2, 3, 4, 5, 6]  # Ensure this matches the grid values used
    norm = BoundaryNorm(bounds, cmap.N)

    # Plot the grid
    plt.imshow(grid_array, cmap=cmap, norm=norm)
    cbar = plt.colorbar(
        ticks=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
        format=plt.FuncFormatter(lambda val, loc: ['Highway', 'Narrow Way', 'Obstacle', 'Path', 'Start', 'Goal'][int(val)])
    )
    plt.title("Path Visualization")
    plt.show()



rows, cols = 50, 50


grid, start, goal = grid_init(rows, cols)


grid = create_obstacle(grid, rows, cols)
grid = path_cost(grid,rows,cols)
start_time = time.time()
tracemalloc.start()
path = genetic_algorithm(grid, start, goal,100,200,150,0.2)
print(path)
_ = path  # Suppress display of the returned value
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Peak memory usage: {peak / 10**6} MB")
if path:
    visualize_path(grid, path, start, goal)