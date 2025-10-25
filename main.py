from constants import POPULATION_SIZE
from generate_population import generate_population
from repopulate import repopulate

population = generate_population(POPULATION_SIZE)

for _ in range(100):
    population_by_fitness_scores = sorted(population, key = lambda gene: gene.count('1'))

    top_50_percent = population_by_fitness_scores[POPULATION_SIZE//2:]

    children = repopulate(top_50_percent)

    population = top_50_percent + children

print(population)