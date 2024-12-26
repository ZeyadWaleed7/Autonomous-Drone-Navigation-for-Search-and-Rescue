from random import choice
import numpy as np

ACTIONS = {
    0: (-1, 0),   # Up
    1: (1, 0),    # Down
    2: (0, -1),   # Left
    3: (0, 1),    # Right
    4: (-1, -1),  # Up-left
    5: (-1, 1),   # Up-right
    6: (1, -1),   # Down-left
    7: (1, 1)     # Down-right
}

def reward_function(state, goal_position):
    if state == goal_position:
        return 100  # Goal reward
    return -1  # Step penalty to prevent the model from taking long paths.

# grid: A dictionary representing the grid, where the keys are coordinates (x, y) and values are Node objects.
# state: The current position of the agent in the grid, represented as (x, y).
def is_valid_move(grid, state, action, row, column):
    new_x, new_y = state[0] + ACTIONS[action][0], state[1] + ACTIONS[action][1]
    return (0 <= new_x < row and 0 <= new_y < column and grid[(new_x, new_y)].passable)
