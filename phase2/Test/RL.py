from Problem.grid import grid_init, create_obstacle
from phase2.main.ReinforcementLearning.q_learning import train_q_learning

row, column = 5, 5
grid, start, goal = grid_init(row, column)
grid = create_obstacle(grid, row, column)

train_q_learning(grid, row, column)