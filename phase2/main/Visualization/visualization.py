import numpy as np
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
    print("Final Movement Patterns:")
    print("───────── Agent Movements ─────────")
    if episode == episodes - 1:
        print(movements, "\n\n\n")


def visualize_progress(episode, total_reward):
    """
    Visualize the progress of the training.
    """
    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}: Total Reward: {total_reward}", "\n\n\n")
