from heapq import heappush, heappop
from grid import grid_init, create_obstacle, path_cost

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
    heappush(priority_queue, (heuristic_function(grid[start].position, grid[goal].position), grid[start].position))  # Corrected: Add as (priority, item)
    visited = set()  # To keep track of visited nodes
    path = {start: None}  # Path dictionary to track explored paths

    while priority_queue:
        ignore, current_position = heappop(priority_queue)  # Retrieve only the position, ignore priority

        current_node = grid[current_position]  # Get the actual node from grid
        if current_node.position == goal:
            return reconstruct_path(path, start, goal)
        visited.add(current_node.position)  # Mark current node as visited

        for child in current_node.children:
            if child.position not in visited and child.passable:
                heappush(priority_queue, (heuristic_function(child.position, grid[goal].position), child.position))
                if child.position not in path:
                    path[child.position] = current_node.position
    return None
# Test the greedy best search algorithm
row, column = 50, 50
grid, start_position, goal_position = grid_init(row, column)  # Initialize the grid with nodes
grid = create_obstacle(grid, row, column)  # Create obstacles on the grid
grid = path_cost(grid, row, column)  # Optionally adjust path costs

# Run greedy best search
path = greedy_best_search(grid, start_position, goal_position)
if path:
    print("Path found:", path)
else:
    print("No path found.")


