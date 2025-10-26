from constants import POPULATION_SIZE, GENE_LENGTH
from generate_population import generate_population
from repopulate import repopulate, split_genes_middle, split_genes_random

perfect_population = ['1' * GENE_LENGTH for _ in range(POPULATION_SIZE)]

population = generate_population(POPULATION_SIZE)

epochs = 0

convergence_times = []

for _ in range(1_000_000):
    while population != perfect_population:
        population_by_fitness_scores = sorted(population, key = lambda gene: gene.count('1'))

        top_50_percent = population_by_fitness_scores[POPULATION_SIZE//2:]

        children = repopulate(top_50_percent, split_genes_middle)

        population = top_50_percent + children
        epochs += 1
    
    convergence_times.append(epochs)

average_convergence = sum(convergence_times) / len(convergence_times)

print(average_convergence)

'''
SIMPLE MIDDLE CROSSOVER
POPULATION_SIZE = 500
GENE_LENGTH = 10
HALF_GENE_LENGTH = GENE_LENGTH // 2

AVG_CONVERGENCE = 8
'''

'''
RANDOM POINT CROSSOVER
POPULATION_SIZE = 500
GENE_LENGTH = 10
HALF_GENE_LENGTH = GENE_LENGTH // 2

AVG_CONVERGENCE = 8
'''