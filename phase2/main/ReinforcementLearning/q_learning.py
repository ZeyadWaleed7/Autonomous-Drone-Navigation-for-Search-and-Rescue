import numpy as np
from random import random, choice
from phase2.main.ReinforcementLearning.actions_reward import ACTIONS, reward_function, is_valid_move
from phase2.main.Visualization.visualization import visualize_policy, visualize_Qtable, visualize_movements, \
    visualize_progress


def train_q_learning(grid, row, column, episodes=1000, alpha=0.1, gamma=0.9, epsilon=1.0,
                     epsilon_decay=0.995):
    """
    episodes: This is the number of training iterations the algorithm will run. Each episode represents a complete
    run from the start state to the goal state (or until a termination condition is met).

    alpha: This is the learning rate, which determines how much new information overrides the old information. A
    higher alpha means the agent learns more quickly, but it might also forget old information faster.

    gamma: This is the discount factor, which determines the importance of future rewards. A value closer to 1 means
    the agent will consider future rewards more heavily, while a value closer to 0 means it will prioritize immediate
    rewards.

    epsilon: This is the exploration rate, which determines the probability of choosing a random action instead of
    the best-known action. This helps the agent explore the environment and avoid getting stuck in local optima. Over
    time, epsilon is decayed to reduce exploration as the agent becomes more confident in its learned policy.

    epsilon_decay: This is the rate at which epsilon is reduced after each episode. It helps the agent gradually
    shift from exploration to exploitation.

    """

    start = [node.position for node in grid.values() if node.start][0]
    goal = [node.position for node in grid.values() if node.goal][0]

    q_table = np.zeros((row * column, len(ACTIONS)))  # Initialize Q-table with zeros

    for episode in range(episodes):
        state = start  # Start state
        total_reward = 0  # Initialize total reward for the episode
        episode_completed = False  # Episode completion flag
        movements = []  # To track the agent's movement patterns

        while not episode_completed:
            state_index = state[0] * column + state[1]  # Convert 2D state to 1D index

            # Epsilon-greedy action selection
            if random() < epsilon:
                action = choice(list(ACTIONS.keys()))  # Random action
            else:
                action = np.argmax(q_table[state_index])  # Best action from Q-table

            # Take action if valid
            if is_valid_move(grid, state, action, row, column):
                # Calculate new state index and reward
                new_state = (state[0] + ACTIONS[action][0], state[1] + ACTIONS[action][1])
                reward = reward_function(new_state, goal)
                new_state_index = new_state[0] * column + new_state[1]

                # Q-learning update
                q_table[state_index, action] = q_table[state_index, action] + alpha * (
                        reward + gamma * np.max(q_table[new_state_index]) - q_table[state_index, action]
                )

                movements.append(new_state)  # Track movements
                state = new_state  # Update state
                total_reward += reward  # Update total reward

                # Check if goal is reached
                if state == goal:
                    episode_completed = True
            else:
                reward = -100  # Penalty for invalid move
                total_reward += reward  # Update total reward

                # Q-learning update for invalid move
                q_table[state_index, action] = q_table[state_index, action] + alpha * (
                        reward - q_table[state_index, action]
                )

        # Decay epsilon
        epsilon = max(0.1, epsilon * epsilon_decay)

        visualize_progress(episode, total_reward)  # Log progress every 100 episodes

        visualize_Qtable(q_table, episode, episodes)  # Visualize Q-table at specific episodes (midway and final)

        visualize_movements(movements, episode, episodes)  # Visualize the agent's movements at the final episode

    visualize_policy(grid, q_table, row, column)  # Visualize the learned policy after training

    return q_table  # Return the trained Q-table
