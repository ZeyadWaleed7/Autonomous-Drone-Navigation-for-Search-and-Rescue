from Problem.Reconstruct_path import rec_path
from collections import deque


def depth_limited_search(grid, limit):
    start_node = [node for node in grid.values() if node.start][0]

    stack = deque([start_node])
    visited = {start_node.position}
    path = {start_node.position: None}
    depth = 0

    while stack:
        current_node = stack.popleft()

        # Check if the current node is the goal
        if current_node.goal:
            return rec_path(path, current_node)  # return the path

        # check if current depth < the current limit
        if depth < limit:
            # perform dfs logic
            for neighbor in current_node.children:
                if neighbor.passable and neighbor.position not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor.position)
                    path[neighbor.position] = current_node

    return None  # Return None if no path is found


def iterative_deepening_search(grid, max_depth=50):
    depth = 0

    while depth <= max_depth:
        result = depth_limited_search(grid, depth)
        if result:
            return result
        depth += 1  # increment depth for next iteration

    return None
