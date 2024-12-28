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


def reward_function(grid, current_position, action):
    # Calculate the new position based on the action
    new_x, new_y = current_position[0] + ACTIONS[action][0], current_position[1] + ACTIONS[action][1]

    # Access the next node
    next_node = grid[(new_x, new_y)]

    # Case 2: Check if the move reaches the goal
    if next_node.goal:
        return 100  # Large positive reward for reaching the goal

    # Case 3: Assign rewards based on road cost
    if next_node.cost == 1:  # Highway
        return 10  # Higher reward for low-cost roads
    elif next_node.cost == 2:  # Narrow way
        return 5   # Lower reward for higher-cost roads


# grid: A dictionary representing the grid, where the keys are coordinates (x, y) and values are Node objects.
# state: The current position of the agent in the grid, represented as (x, y).
def is_valid_move(grid, state, action, row, column):
    # Calculate the new position based on the action
    new_x, new_y = state[0] + ACTIONS[action][0], state[1] + ACTIONS[action][1]

    # Check if the new position is within bounds
    if not (0 <= new_x < row and 0 <= new_y < column):
        return False

    # Access the node at the new position
    next_node = grid[(new_x, new_y)]

    # Check if the node is passable
    return next_node.passable

