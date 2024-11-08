from heuristic_function import heuristic_function
from grid import grid_init, create_obstacle, path_cost
def hill_climbing(grid, start_position, goal_position):
    
    current = grid[start_position]
    goal_node = grid[goal_position]
    path = [current.position]

    while not current.goal:
        # Filter passable neighbors only
        neighbors = []
        for neighbor in current.children:
            if neighbor.passable:
                neighbors.append(neighbor)

        
        if not neighbors:
            # If there are no passable neighbors then there is no path
            print("No path found!")
            return path

        # Iterate to find the the neighbor with the lowest heueristic value (Manhattan distance) to the goal
        next_node = neighbors[0]
        for neighbor in neighbors[1:]:
            if heuristic_function(neighbor.position, goal_node.position) < heuristic_function(next_node.position, goal_node.position):
                next_node = neighbor

        # Check if the neighbor is closer to the goal
        if heuristic_function(next_node.position, goal_node.position) >= heuristic_function(current.position, goal_node.position):
            # if there is no neighbor with a lower heuristic value then wwe have reached a local maxima
            print("Reached a local maximum.")
            print(goal_node.position)
            return path

        # Move to the selected neighbor
        current = next_node
        path.append(current.position)

    print("Goal reached!")
    return path
# Test 
row, column = 50, 50
grid, start_position, goal_position = grid_init(row, column)
grid = create_obstacle(grid, row, column)
grid = path_cost(grid, row, column)
path = hill_climbing(grid, start_position, goal_position)
print("Path taken:", path)