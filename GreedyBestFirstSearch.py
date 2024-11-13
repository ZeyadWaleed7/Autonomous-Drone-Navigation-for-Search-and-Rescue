from queue import PriorityQueue
from heuristic_function import heuristic_function


def greedy_best_first_search(grid,goal_state,initial_state):
    current = grid[initial_state]
    goal_node = grid[goal_state]
    path = []
    fronteir = PriorityQueue()
    fronteir.put((heuristic_function(current.position, goal_node.position), current))
    visited = set()
    while not fronteir.empty():
        currentHeuristic,current=fronteir.get()

        if current.position not in path:
            path.append(current.position)
            print(f"Exploring node: {current.position}")  # Debugging line

        if current.goal:
            print("Goal Reached !")
            return path
        visited.add(current.position)
        for neighbor in current.children:
            if neighbor.passable and not (neighbor.position in visited):
                fronteir.put((heuristic_function(neighbor.position,goal_node.position),neighbor))
                visited.add(neighbor.position)

    print("No Path Exists !")
    return  []


