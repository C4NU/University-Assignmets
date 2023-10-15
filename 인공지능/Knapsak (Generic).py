import random

items = ['A', 'B', 'C', 'D', 'E', 'F']
weights = [15, 3, 2, 5, 9, 20]
values = [15, 7, 10, 5, 8, 17]

max_weight = 50

population_size = 100
generations = 20
mutation_rate = 0.01

def random_population(population_size):
  return [[random.randint(0, 1) for _ in range(len(items))] for _ in range(population_size)]

def fitness(solution):
  total_weight = sum(weights[i] for i in range(len(items)) if solution[i])
  if total_weight > max_weight:
    return 0
  return sum(values[i] for i in range(len(items)) if solution[i])

def crossover(parent1, parent2):
  crossover_point = random.randint(1, len(items) - 1)
  child1 = parent1[:crossover_point] + parent2[crossover_point:]
  child2 = parent2[:crossover_point] + parent1[crossover_point:]
  return child1, child2

def mutate(solution):
  mutated_solution = solution[:]
  for i in range(len(mutated_solution)):
    if random.random() < mutation_rate:
      mutated_solution[i] = 1 - mutated_solution[i]
  return mutated_solution

def genetic_algorithm():
  population = random_population(population_size)
  for _ in range(generations):
    population = sorted(population, key=lambda x: fitness(x), reverse = True)
    new_population = []

    for i in range(population_size // 2):
        parent1, parent2 = population[i], population[i+1]
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])
    population = new_population

  return max(population, key=lambda x: fitness(x))

best_solution = genetic_algorithm()

print("The best combinations is::", best_solution)
print("The total possible value of the items:", sum(values[i] for i in range(len(items)) if best_solution[i]))
print("The total possible weight of the items:", sum(weights[i] for i in range(len(items)) if best_solution[i]))
