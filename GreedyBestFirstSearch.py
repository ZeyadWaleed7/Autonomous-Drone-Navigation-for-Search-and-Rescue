from heapq import heappush, heappop

from heuristic_function import heuristic_function

def reconstruct_path(path, start, goal):
    current = goal
    result_path = []
    while current is not None:
        result_path.append(current)
        current = path[current]
    result_path.reverse()
    return result_path

def greedy_best_search(grid, start, goal):
    priority_queue = []  # Priority queue to hold nodes to explore, sorted by heuristic value
    heappush(priority_queue, (heuristic_function(grid[start].position, grid[goal].position), grid[start]))  # Corrected: Add as (priority, item)
    visited = set()  # To keep track of visited nodes
    path = {start: None}  # Path dictionary to track explored paths

    while priority_queue:
        current_node = heappop(priority_queue)[1]  #  Retrieve node from (priority, item)

        if current_node.position == goal:
            return reconstruct_path(path, start, goal)
        visited.add(current_node.position)  # Mark current node as visited

        for child in current_node.children:
            if child.position not in visited and child.passable:
                heappush(priority_queue, (heuristic_function(child.position, grid[goal].position), child))
                if child.position not in path:
                    path[child.position] = current_node.position
    return None


