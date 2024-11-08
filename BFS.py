def bfs(problem):
    # Start with the initial state in the frontier
    frontier = [problem.init_state]
    # Keep track of explored nodes to avoid repeats
    explored = set()

    # Loop as long as there are nodes to explore
    while frontier:
        # Remove the first element from the frontier
        state = frontier.pop(0)

        # Check if this state is the goal
        if problem.goal_test(state):
            return state, explored  # Return the goal if found

        # Mark this state as explored
        explored.add(state)

        # Add all new states (children) to the frontier
        for action in problem.actions(state):
            # Get the resulting state from this action
            child = problem.result(state, action)
            # Add to frontier if it hasn't been explored or added already
            if child not in explored and child not in frontier:
                frontier.append(child)

    # If no solution is found, return None
    return None, explored


class TreeProblem:
    def __init__(self, init_state, goal_state, tree):
        self.init_state = init_state  # Starting node (root)
        self.goal_state = goal_state  # Goal node
        self.tree = tree              # Tree represented as a dictionary

    def goal_test(self, state):
        # Check if we've reached the goal
        return state == self.goal_state

    def actions(self, state):
        # Get children of the current node
        return self.tree.get(state, [])

    def result(self, state, action):
        # Moving to a child node in the tree
        return action


# Define a simple tree as a dictionary
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Initialize the tree problem with a start and goal node
tree_problem = TreeProblem(init_state='A', goal_state='G', tree=tree)

# Run BFS and print the result
result = bfs(tree_problem)
print("Goal found:", result)
