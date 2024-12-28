from Problem.grid import grid_init, create_obstacle, path_cost
from phase2.main.ReinforcementLearning.q_learning import train_q_learning
from phase1.main.InformedSearch.A_Star import a_star
from phase2.main.Visualization.visualization import visualize_path
import time
import tracemalloc


row, column = 5, 5
grid, start, goal = grid_init(row, column)
grid = create_obstacle(grid, row, column)
grid = path_cost(grid, row, column)

# qlearning
qlearning_start_time = time.time()
tracemalloc.start()
q_table, qlearning_path = train_q_learning(grid, row, column)
qlearning_end_time = time.time()
qlearning_current, qlearning_peak = tracemalloc.get_traced_memory()

print("qlearning Execution Time:", (qlearning_end_time - qlearning_start_time)," ms")
print("qlearning Peak memory usage:", repr(qlearning_peak / 10 ** 6))
visualize_path(grid, qlearning_path, start, goal, "Q Learning")

# A*
a_star_start_time = time.time()
tracemalloc.start()
a_star_path = a_star(grid, start, goal)
a_star_end_time = time.time()
A_current, A_peak = tracemalloc.get_traced_memory()
print("A* Path : ", a_star_path)
print("A* Execution Time:", (a_star_end_time - a_star_start_time)," ms")
print("A* Peak memory usage:", repr(A_peak / 10 ** 6))
visualize_path(grid, a_star_path, start, goal, "A Star")


'''
    As the qlearning results in same as A* results,
    so we can confirm that the qlearning alogorithm works correct
    and the agent trained well. 
'''
