from Problem.grid import grid_init, create_obstacle
from phase2.main.ReinforcementLearning.q_learning import train_q_learning, visualize_policy

row, column = 5, 5
grid, start, goal = grid_init(row, column)
grid = create_obstacle(grid, row, column)

q_table = train_q_learning(grid, row, column)
visualize_policy(grid, q_table, row, column)
