import sys
from collections import deque
from random import randint, choice
from grid import grid_init,create_obstacle,path_cost


def depth_limited_search(problem, limit=50):
    """Performs a depth-limited search up to a specified limit."""

    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.position):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            children = [Node(child, cost=1) for child in problem.actions(node.position)]
            for child in children:
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    return recursive_dls(Node(problem.initial_state(), cost=0), problem, limit)


def iterative_deepening_search(problem):
    """Performs iterative deepening search."""
    max_frontier_size = 1
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, limit=depth)
        if result != 'cutoff':
            path = []
            current = result
            while current:
                path.append(current.position)
                current = current.parent  # Assuming nodes have a parent attribute.
            path.reverse()  # Reverse path to get start to goal direction
            return path, max_frontier_size
        max_frontier_size = max(max_frontier_size, depth)

    return None, max_frontier_size