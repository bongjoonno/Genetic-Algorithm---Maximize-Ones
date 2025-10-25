from constants import POPULATION_SIZE
from generate_population import generate_population

population = generate_population(POPULATION_SIZE)

population_by_fitness_scores = sorted(population, key = lambda gene: gene.count('1'))

top_50_percent = population_by_fitness_scores[POPULATION_SIZE//2:]

print(len(population_by_fitness_scores), len(population), len(top_50_percent))

# eliminate 50% of population

# repopulate
