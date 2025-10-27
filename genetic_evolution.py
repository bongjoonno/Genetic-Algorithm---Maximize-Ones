from constants import POPULATION_SIZE
from repopulate import repopulate

def genetic_evolution(population, perfect_population, gene_split_method, gene_length):
    epochs, epochs_w_no_progress = 0, 0
    
    while population != perfect_population:
        total_1s = sum(gene.count('1') for gene in population)
        
        population_by_fitness_scores = sorted(population, key = lambda gene: gene.count('1'))

        top_50_percent = population_by_fitness_scores[POPULATION_SIZE//2:]

        children = repopulate(top_50_percent, gene_split_method, gene_length)

        population = top_50_percent + children
        
        if total_1s == sum(gene.count('1') for gene in population):
            epochs_w_no_progress += 1
        if epochs_w_no_progress == 100:
            return 0

        epochs += 1
    
    return epochs