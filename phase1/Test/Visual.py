import tracemalloc

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from phase1.main.LocalSearch.hill_climbing import hill_climbing
from phase1.main.InformedSearch.A_Star import a_star
from phase1.main.UninformedSearch.BFS import breadth_first_search
from phase1.main.UninformedSearch.DFS import depth_first_search
from phase1.main.UninformedSearch.UCS import uniform_cost_search
from phase1.main.UninformedSearch.IDS import iterative_deepening_search
from phase1.main.InformedSearch.GreedyBestFirstSearch import greedy_best_search
from Problem.grid import path_cost, create_obstacle, grid_init
from phase1.main.LocalSearch.simulated_Annealing import simulated_annealing
from phase1.main.LocalSearch.genatic import genetic_algorithm
import time


def visualize_path(grid, path, start, goal, title):
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
    grid_array[goal[0], goal[1]] = 5  # Mark goal

    # Define colormap and normalization
    cmap = ListedColormap(['lightblue', 'pink', 'black', 'yellow', 'red', 'green'])
    bounds = [0, 1, 2, 3, 4, 5, 6]  # Ensure this matches the grid values used
    norm = BoundaryNorm(bounds, cmap.N)

    # Plot the grid
    plt.imshow(grid_array, cmap=cmap, norm=norm)
    cbar = plt.colorbar(
        ticks=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
        format=plt.FuncFormatter(
            lambda val, loc: ['Highway', 'Narrow Way', 'Obstacle', 'Path', 'Start', 'Goal'][int(val)])
    )
    plt.title(title)
    plt.show()


# Define grid dimensions
rows, cols = 50, 50

grid, start, goal = grid_init(rows, cols)

grid = create_obstacle(grid, rows, cols)
grid = path_cost(grid, rows, cols)

# BFS
bfs_start_time = time.time()
tracemalloc.start()
bfs = breadth_first_search(grid)
bfs_end_time = time.time()
bfs_current, bfs_peak = tracemalloc.get_traced_memory()
print("BFS Path : ", bfs)
print("BFS Execution Time:", (bfs_end_time - bfs_start_time), " ms")
print("BFS Peak memory usage:", repr(bfs_peak / 10 ** 6))
visualize_path(grid, bfs, start, goal, "Breadth First")

# DFS
dfs_start_time = time.time()
tracemalloc.start()
dfs = depth_first_search(grid)
dfs_end_time = time.time()
dfs_current, dfs_peak = tracemalloc.get_traced_memory()
print("DFS Path : ", dfs)
print("DFS Execution Time:", (dfs_end_time - dfs_start_time), " ms")
print("DFS Peak memory usage:", repr(dfs_peak / 10 ** 6))
visualize_path(grid, dfs, start, goal, "Depth First")

# UCS
ucs_start_time = time.time()
tracemalloc.start()
ucs, cost = uniform_cost_search(grid, start, goal)
ucs_end_time = time.time()
ucs_current, ucs_peak = tracemalloc.get_traced_memory()
print("UCS Path : ", ucs)
print("UCS Execution Time:", (ucs_end_time - ucs_start_time), " ms")
print("UCS Peak memory usage:", repr(ucs_peak / 10 ** 6))
visualize_path(grid, ucs, start, goal, "Uniform Cost")

# IDS
ids_start_time = time.time()
tracemalloc.start()
ids_end_time = time.time()
ids = iterative_deepening_search(grid)
ids_current, ids_peak = tracemalloc.get_traced_memory()
print("IDS Path : ", ids)
print("IDS Execution Time:", (ids_end_time - ids_start_time), " ms")
print("IDS Peak memory usage:", repr(ids_peak / 10 ** 6))
visualize_path(grid, ids, start, goal, "Iterative Deepening")

# A*
a_star_start_time = time.time()
tracemalloc.start()
a_star_path = a_star(grid, start, goal)
a_star_end_time = time.time()
A_current, A_peak = tracemalloc.get_traced_memory()
print("A* Path : ", a_star_path)
print("A* Execution Time:", (a_star_end_time - a_star_start_time), " ms")
print("A* Peak memory usage:", repr(A_peak / 10 ** 6))
visualize_path(grid, a_star_path, start, goal, "A Star")

# Greedy
greedy_start_time = time.time()
tracemalloc.start()
greedy_path = greedy_best_search(grid, start, goal)
greedy_end_time = time.time()
greedy_current, greedy_peak = tracemalloc.get_traced_memory()
print("Greedy Path: ", greedy_path)
print("Greedy Execution Time:", (greedy_end_time - greedy_start_time), " ms")
print("Greedy Peak memory usage:", repr(greedy_peak / 10 ** 6))
visualize_path(grid, greedy_path, start, goal, "Greedy Best First")

# Simulated Annealing
start_time = time.time()
tracemalloc.start()
path = simulated_annealing(grid, start, goal, 1000, 0.99, 1000)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
print("Simulated Annealing Execution Time:", (end_time - start_time), " ms")
print("Simulated Annealing Peak memory usage:", repr(peak / 10 ** 6))
visualize_path(grid, path, start, goal, "Simulated Annealing")

# Genetic
gen_start_time = time.time()
tracemalloc.start()
gen_path = genetic_algorithm(grid, start, goal, population_size=100, generations=200, max_path_length=150,
                             mutation_rate=0.2)
gen_end_time = time.time()
gen_current, gen_peak = tracemalloc.get_traced_memory()
print("Genetic Execution Time:", (gen_end_time - gen_start_time), " ms")
print("Genetic memory usage:", repr(gen_peak / 10 ** 6))
visualize_path(grid, gen_path, start, goal, "Genetic")

# Hill Climbing
Hill_Climbing_start_time = time.time()
tracemalloc.start()
Hill_Climbing = hill_climbing(grid, start, goal)
Hill_Climbing_end_time = time.time()
Hill_Climbing_current, Hill_Climbing_peak = tracemalloc.get_traced_memory()
print("Hill Climbing Path : ", Hill_Climbing)
print("Hill Climbing Execution Time:", (Hill_Climbing_end_time - Hill_Climbing_start_time), " ms")
print("Hill Climbing Peak memory usage:", repr(Hill_Climbing_peak / 10 ** 6))
visualize_path(grid, Hill_Climbing, start, goal, "Hill Climbing")
