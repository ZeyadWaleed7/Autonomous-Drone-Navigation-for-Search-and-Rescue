from random import randint, random, choice, sample
from heuristic_function import heuristic_function
from grid import grid_init, create_obstacle, path_cost

def initialize_population(grid, start_position, goal_position, population_size, max_path_length):
    population = []
    count = 0

    while count < population_size:
        path = [start_position]
        current_position = start_position

        while len(path) < max_path_length:
            current_node = grid[current_position]
            neighbors = []
            for neighbor in current_node.children:
                if neighbor.passable:
                    neighbors.append(neighbor.position)

            if not neighbors:
                break

            next_position = choice(neighbors)
            path.append(next_position)
            current_position = next_position

            if current_position == goal_position:
                break

        population.append(path)
        count += 1

    return population


def fitness_function(path, goal_position):
    last_position = path[-1]
    distance_to_goal = heuristic_function(last_position, goal_position)

    return -distance_to_goal - len(path) * 0.1


def crossover(parent1, parent2):
    crossover_point = randint(1, min(len(parent1), len(parent2)) - 1)
    child = parent1[:crossover_point]

    for i in parent2:
        if i not in child:
            child.append(i)

    return child


def mutate(path, grid, mutation_rate):
    if random() < mutation_rate:
        mutation_index = randint(0, len(path) - 1)
        current_node = grid[path[mutation_index]]
        for neighbor in current_node.children:
                if neighbor.passable:
                    neighbors.append(neighbor.position)

        if neighbors:
            path[mutation_index] = choice(neighbors)

    return path


def genetic_algorithm(grid, start_position, goal_position, population_size, generations, max_path_length, mutation_rate):
    population = initialize_population(grid, start_position, goal_position, population_size, max_path_length)

    generation = 0
    best_path = None
    best_score = float('-inf')

    while generation < generations:
        fitness_scores = []
        for path in population:
            fitness_scores.append((path, fitness_function(path, goal_position)))

        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        current_best_path, current_best_score = fitness_scores[0]
        if current_best_score > best_score:
            best_path = current_best_path
            best_score = current_best_score

        if best_path[-1] == goal_position:
            break

        top_individuals = []
        count = 0
        while count < population_size // 2:
            top_individuals.append(fitness_scores[count][0])
            count += 1

        next_generation = []
        count = 0
        while count < population_size:
            parent1 = choice(top_individuals)
            parent2 = choice(top_individuals)
            child = crossover(parent1, parent2)
            child = mutate(child, grid, mutation_rate)
            next_generation.append(child)
            count += 1

        population = next_generation
        generation += 1

    if best_path and best_path[-1] == goal_position:
        print("Goal reached!")
    else:
        print("Couldn't find a complete path.")

    return best_path


# Test
if __name__ == "__main__":
    row, column = 50, 50
    grid, start_position, goal_position = grid_init(row, column)
    grid = create_obstacle(grid, row, column)
    grid = path_cost(grid, row, column)

    print(f"Start position: {start_position}, Goal position: {goal_position}")

    path = genetic_algorithm(
        grid,
        start_position,
        goal_position,
        population_size=100,  
        generations=200,      
        max_path_length=150,  
        mutation_rate=0.2     
    )

    if path:
        print("Path taken is", path)
    else:
        print("No valid path found")
