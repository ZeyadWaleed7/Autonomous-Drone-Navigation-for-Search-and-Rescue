from heapq import heappush, heappop

from grid import reconstruct_path
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

