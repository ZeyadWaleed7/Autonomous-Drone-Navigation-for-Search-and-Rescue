import heapq

from Reconstruct_path import reconstruct_path

def uniform_cost_search(grid, start_position, goal_position):
    # Priority queue for nodes to explore, storing (cumulative_cost, node_position)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_position))

    # Dictionary to track the cumulative cost to reach each node
    cumulative_cost = {start_position: 0}

    # Dictionary to track the path
    came_from = {start_position: None}

    while priority_queue:
        current_cost, current_position = heapq.heappop(priority_queue)
        current_node = grid[current_position]

        # If the goal is reached, reconstruct the path
        if current_node.goal:
            return reconstruct_path(came_from, current_position), current_cost

        # Explore neighbors
        for neighbor in current_node.children:
            if neighbor.passable:
                new_cost = current_cost + neighbor.cost
                neighbor_position = neighbor.position

                # If this path to the neighbor is better, or the neighbor hasn't been visited yet
                if new_cost < cumulative_cost[neighbor_position] or neighbor_position not in cumulative_cost :
                    cumulative_cost[neighbor_position] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor_position))
                    came_from[neighbor_position] = current_position

    # If no path is found
    return None


