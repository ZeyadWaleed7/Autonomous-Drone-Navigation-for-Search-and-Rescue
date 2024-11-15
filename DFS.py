from collections import deque

def depth_first_search(grid):
    start_node = [node for node in grid.values() if node.start][0]

    queue = deque([start_node])
    visited = {start_node.position}

    while queue:
        current_node = queue.pop()

        # Check if we've reached the goal
        if current_node.goal:
            return True  # Path exists

        # Visit all passable, unvisited neighbors
        for neighbor in current_node.children:
            if neighbor.position not in visited and neighbor.passable:
                queue.append(neighbor)
                visited.add(neighbor.position)

    return False  # Path does not exist if the goal was not reached
