from heapq import heappush, heappop

from grid import reconstruct_path, grid_init, create_obstacle
from heuristic_function import heuristic_function


def a_star(grid,start,goal):
    priority_queue = []
    heappush(priority_queue,(0,start))
    path = {start:None}
    g_cost= {start:0}

    while priority_queue:
        priority, current_position = heappop(priority_queue)

        current_node = grid[current_position]
        if current_node.position == goal:
            return reconstruct_path(path,start,goal)

        for child in current_node.children:
            if  child.passable:
                tentative_g_cost = g_cost[current_node.position] + child.cost
                if child.position not in g_cost or tentative_g_cost < g_cost[child.position]:
                    g_cost[child.position] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic_function(child.position,goal)
                    heappush(priority_queue, (f_cost,child.position))
                    path[child.position] = current_node.position

    return None

def run_test_cases():
    # Test Case 1: Basic Path (Straight Line)
    grid, start, goal = grid_init(5, 5)
    path = a_star(grid, start, goal)
    print("Test Case 1 - Basic Path:", path)

    # Test Case 2: Grid with Obstacles
    grid, start, goal = grid_init(5, 5)
    # Manually set obstacles
    for obstacle_pos in [(1, 1), (2, 2), (3, 3)]:
        grid[obstacle_pos].passable = False
    path = a_star(grid, start, goal)
    print("Test Case 2 - Obstacles:", path)

    # Test Case 3: No Possible Path
    grid, start, goal = grid_init(5, 5)
    for obstacle_pos in [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)]:
        grid[obstacle_pos].passable = False
    path = a_star(grid, start, goal)
    print("Test Case 3 - No Path Available:", path)

    # Test Case 4: Start Equals Goal
    grid, start, goal = grid_init(5, 5)
    start = (2, 2)
    goal = (2, 2)
    grid[start].start = True
    grid[goal].goal = True
    path = a_star(grid, start, goal)
    print("Test Case 4 - Start Equals Goal:", path)

    # Test Case 5: Large Grid Test
    grid, start, goal = grid_init(50, 50)
    create_obstacle(grid, 50, 50)  # Randomly add obstacles
    path = a_star(grid, start, goal)
    print("Test Case 5 - Large Grid:", path)

run_test_cases()
