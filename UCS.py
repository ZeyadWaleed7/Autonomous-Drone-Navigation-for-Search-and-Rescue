import heapq

from Reconstruct_path import reconstruct_path, rec_path


def uniform_cost_search(grid, start_position, goal_position):
    priority_queue = []  # Priority queue
    heapq.heappush(priority_queue, (0, start_position))

    cumulative_cost = {start_position: 0}  # for tracking cost

    path = {start_position: None}

    while priority_queue:
        current_cost, current_position = heapq.heappop(priority_queue)
        current_node = grid[current_position]

        # Check if the current node is the goal
        if current_node.goal:
            return reconstruct_path(path, start_position, goal_position), current_cost  # return the path

        # Visit all passable nodes
        for neighbor in current_node.children:
            if neighbor.passable:
                new_cost = current_cost + neighbor.cost
                neighbor_position = neighbor.position

                # check if there is a better path (lower cost) or a neighbor node is not visited yet
                if neighbor_position not in cumulative_cost or new_cost < cumulative_cost[neighbor_position]:
                    cumulative_cost[neighbor_position] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor_position))
                    path[neighbor_position] = current_position

    return None  # Return None if no path is found
