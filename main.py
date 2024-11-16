import time
import tracemalloc
from A_Star import a_star
from simulated_Annealing import simulated_annealing

from GreedyBestFirstSearch import greedy_best_search
from grid import grid_init, create_obstacle, path_cost
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

def visualize_path(grid, path, start, goal,title):
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
    plt.title(title)
    plt.show()


def main():
    # Define grid dimensions
    rows, cols = 50, 50


    grid, start, goal = grid_init(rows, cols)


    grid = create_obstacle(grid, rows, cols)
    grid = path_cost(grid,rows,cols)

    a_star_path = a_star(grid, start, goal)
    print(a_star_path)
    visualize_path(grid, a_star_path, start, goal,"A Star")

    greedy_path = greedy_best_search(grid,start, goal)
    print(greedy_path)
    visualize_path(grid , greedy_path ,start,goal,"Greedy Best First")


    start_time = time.time()
    tracemalloc.start()
    path = simulated_annealing(grid, start, goal,1000,0.99,1000)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Execution Time: {end_time - start_time} seconds")
    print(f"Peak memory usage: {peak / 10**6} MB")
    if path:
        visualize_path(grid, path, start, goal,"Simulated Annealing")
        
if __name__ == "__main__":
    main()