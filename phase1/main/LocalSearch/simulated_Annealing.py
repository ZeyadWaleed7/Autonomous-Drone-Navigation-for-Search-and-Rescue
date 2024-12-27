from phase1.main.Heuristics.heuristic_function import heuristic_function  # Import the specific function
from random import choice, uniform
import math


def simulated_annealing(grid, start_position, goal_position, initial_temp, cooling_rate, max_iter):
    # Initialize 
    current_position = start_position
    current_cost = heuristic_function(current_position, goal_position)  # Call the heuristic function
    temperature = initial_temp
    path = [current_position]

    for i in range(max_iter):
        # Get the start Node from the grid
        current_node = grid[current_position]
        
        # Get passable neighbors from the current node
        neighbors = []
        for neighbor in current_node.children:  
            if neighbor.passable:
                neighbors.append(neighbor)

        if not neighbors:
            print("No path found")
            return path
        
        # Randomly select a passable neighbor
        next_position = choice(neighbors).position
        next_cost = heuristic_function(next_position, goal_position)  
        
        # Calculate the change in cost 
        delta_cost = next_cost - current_cost
        
        # Condition
        if delta_cost < 0 or uniform(0, 1) < math.exp(-delta_cost / temperature):
            current_position = next_position
            current_cost = next_cost
            path.append(current_position)
            
            # Check if goal is reached
            if current_position == goal_position:
                print("Goal reached!")
                return path

        # Cool down temperature
        temperature *= cooling_rate
        
        # Stop if temperature reaches zero
        if temperature <= 0:
            break

    print("Couldn't find a complete path.")
    return path
