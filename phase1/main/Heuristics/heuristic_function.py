import math
#heuristic function that measures the distance between a cell and the goal (Manhattan Distance)
def heuristic_function(pos,goal):
    return abs(pos[0]-goal[0])+abs(pos[1]-goal[1])


    