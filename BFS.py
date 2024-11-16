from collections import deque
from Reconstruct_path import rec_path


def breadth_first_search(grid):
    start_node = [node for node in grid.values() if node.start][0]

    queue = deque([start_node])
    visited = {start_node.position}
    path = {start_node.position: None}

    while queue:
        current_node = queue.popleft()

        # Check if we've reached the goal
        if current_node.goal:
            return rec_path(path,current_node)

        # Visit all passable, unvisited neighbors
        for neighbor in current_node.children:
            if neighbor.passable and neighbor.position not in visited:
                queue.append(neighbor)
                visited.add(neighbor.position)
                path[neighbor.position] = current_node

    return None  # Return None if no path is found
