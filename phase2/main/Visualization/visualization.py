import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

from phase2.main.ReinforcementLearning.actions_reward import ACTIONS


def visualize_policy(grid, q_table, row, column):
    """
        Visualize the learned policy.
    """

    policy = np.full((row, column), ' ')  # Initialize the policy grid

    # Identify start and goal nodes positions
    start_position = [node.position for node in grid.values() if node.start][0]
    goal_position = [node.position for node in grid.values() if node.goal][0]

    # Fill the policy grid with directions based on Q-table values
    for x in range(row):
        for y in range(column):
            state_index = x * column + y

            # Get the best action and its direction
            best_action = np.argmax(q_table[state_index])
            direction = list(ACTIONS.values())[best_action]
            if direction == (-1, 0):
                policy[x, y] = '↑'
            elif direction == (1, 0):
                policy[x, y] = '↓'
            elif direction == (0, -1):
                policy[x, y] = '←'
            elif direction == (0, 1):
                policy[x, y] = '→'
            elif direction == (-1, -1):
                policy[x, y] = '↖'  # up-left
            elif direction == (-1, 1):
                policy[x, y] = '↗'  # up-right
            elif direction == (1, -1):
                policy[x, y] = '↙'  # down-left
            elif direction == (1, 1):
                policy[x, y] = '↘'  # down-right

            # print("Learned Policy 1:")
            # print(policy)

        # print("Learned Policy 2:")
        # print(policy)

    print("───────── Learned Policy ─────────")
    print(policy, "\n\n\n")

    policy[start_position] = 'S'
    policy[goal_position] = 'G'

    print("───────── Learned Policy (with start and goal) ─────────")
    print(policy, "\n\n\n")


def visualize_Qtable(q_table, episode, episodes):
    """
        Visualize the Q-table.
    """

    if (episode + 1) == episodes // 2:
        print("Midway Q-values:")
        print("───────── Q-Table ─────────")
        print(q_table, "\n\n\n")

    if episode == episodes - 1:
        print("Final Q-values:")
        print("───────── Q-Table ─────────")
        print(q_table, "\n\n\n")


def visualize_movements(movements, episode, episodes):
    """
        Visualize the agent's movements.
    """

    if episode == episodes - 1:
        print("Final Movement Patterns:")
        print("───────── Agent Movements ─────────")
        print(movements, "\n\n\n")


def visualize_progress(episode, total_reward):
    """
    Visualize the progress of the training.
    """
    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}: Total Reward: {total_reward}")


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
