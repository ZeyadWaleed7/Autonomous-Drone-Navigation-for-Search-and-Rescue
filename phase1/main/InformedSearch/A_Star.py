from heapq import heappush, heappop  # Used for managing the priority queue efficiently

from Problem.grid import reconstruct_path  # Function to rebuild the path from start to goal
from phase1.main.Heuristics.heuristic_function import heuristic_function  # Function to calculate the heuristic (estimated cost)

# A* pathfinding algorithm implementation
def a_star(grid, start, goal):
    priority_queue = []
    heappush(priority_queue, (0, start))  # Add the start node with priority 0
    path = {start: None}  # Dictionary to store the path
    g_cost = {start: 0}  # Tracks the cost to reach each node from the start

    while priority_queue:
        priority, current_position = heappop(priority_queue)

        current_node = grid[current_position]
        if current_node.position == goal:
            return reconstruct_path(path, start, goal)

        for child in current_node.children:
            if child.passable:
                tentative_g_cost = g_cost[current_node.position] + child.cost
                # If the child node has not been visited or a cheaper path is found
                if child.position not in g_cost or tentative_g_cost < g_cost[child.position]:
                    g_cost[child.position] = tentative_g_cost  # Update the g cost for the child
                    # Calculate the f cost (g cost + heuristic)
                    f_cost = tentative_g_cost + heuristic_function(child.position, goal)
                    # Add the child node to the priority queue with its f cost
                    heappush(priority_queue, (f_cost, child.position))
                    # Update the path to reflect the parent of the child node
                    path[child.position] = current_node.position

    return None