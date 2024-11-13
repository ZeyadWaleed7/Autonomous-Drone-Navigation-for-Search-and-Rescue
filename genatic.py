import numpy as np
import random
from heuristic_function import heuristic_function
from grid import grid_init, create_obstacle, path_cost

POPULATION_SIZE = 10
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.7
GENERATIONS = 50
GENOME_LENGTH = 100

def initialize_population(grid, start_position):
    population = []

    for i in range(POPULATION_SIZE):
        path = [start_position]

        for j in range(GENOME_LENGTH):
            move = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])

            current_row, current_col = path[-1]
            next_row = current_row + move[0]
            next_col = current_col + move[1]
            next_position = (next_row, next_col)

            if 0 <= next_position[0] < len(grid) and 0 <= next_position[1] < len(grid[0]):
                if grid[next_position].passable:
                    path.append(next_position)

        population.append(path)
    return population

def calculate_fitness(path, goal_position):
    last_position = path[-1]
    return heuristic_function(last_position, goal_position) 

def select_best_paths(population, goal_position):
    return sorted(population, key=lambda path: calculate_fitness(path, goal_position))

def crossover(parent1, parent2):
    crossover_point = random.randint(0, min(len(parent1), len(parent2)) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(path, grid):
    if random.random() < MUTATION_RATE:

        index = random.randint(0, len(path) - 1)
        move = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        next_position = (path[index][0] + move[0], path[index][1] + move[1])

        if 0 <= next_position[0] < len(grid) and 0 <= next_position[1] < len(grid[0]) and grid[next_position].passable:
            path[index] = next_position

    return path

def genetic_algorithm(grid, start_position, goal_position):

    population = initialize_population(grid, start_position)

    for generation in range(GENERATIONS):
        population = select_best_paths(population, goal_position)
        new_population = []

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(population, 2)

            if random.random() < CROSSOVER_RATE:
                child = crossover(parent1, parent2)
            else:
                child = random.choice([parent1, parent2])

            child = mutate(child, grid)
            new_population.append(child)

        population = new_population

        for path in population:
            if path[-1] == goal_position:
                print("Goal reached!")
                return path

    print("No path found after", GENERATIONS, "generations")
    return None
