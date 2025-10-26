from constants import POPULATION_SIZE, PERFECT_POPULATION
from repopulate import repopulate

def genetic_evolution(population, gene_split_method):
    epochs = 0
    epochs_w_no_progress = 0
    
    while population != PERFECT_POPULATION:
        total_1s = sum(gene.count('1') for gene in population)
        
        population_by_fitness_scores = sorted(population, key = lambda gene: gene.count('1'))

        top_50_percent = population_by_fitness_scores[POPULATION_SIZE//2:]

        children = repopulate(top_50_percent, gene_split_method)

        population = top_50_percent + children
        
        if total_1s == sum(gene.count('1') for gene in population):
            epochs_w_no_progress += 1
        if epochs_w_no_progress == 100:
            return -1

        epochs += 1
    
    return epochs