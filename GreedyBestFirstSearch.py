from heapq import heappush, heappop
from grid import grid_init, create_obstacle, path_cost, reconstruct_path

from heuristic_function import heuristic_function


def greedy_best_search(grid, start, goal):
    priority_queue = []  # Priority queue to hold nodes to explore, sorted by heuristic value
    heappush(priority_queue, (heuristic_function(grid[start].position, grid[goal].position), grid[start].position))  # Corrected: Add as (priority, item)
    visited = set()  # To keep track of visited nodes
    path = {start: None}  # Path dictionary to track explored paths

    while priority_queue:
        priority, current_position = heappop(priority_queue)  # Retrieve only the position, ignore priority

        current_node = grid[current_position]  # Get the actual node from grid
        if current_node.position == goal:
            return reconstruct_path(path, start, goal)
        visited.add(current_node.position)  # Mark current node as visited

        for child in current_node.children:
            # go to the node if possible and not visited
            if child.position not in visited and child.passable:
                heappush(priority_queue, (heuristic_function(child.position, grid[goal].position), child.position))
                #if it has not added to path add it
                if child.position not in path:
                    path[child.position] = current_node.position
    return None
