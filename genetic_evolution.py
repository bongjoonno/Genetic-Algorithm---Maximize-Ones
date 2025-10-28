from constants import POPULATION_SIZE
from repopulate import repopulate
from mutate import mutate

def genetic_evolution(population, perfect_chromosome, gene_split_method, gene_length, mutate_children: bool):
    epochs = 0
    population_set = set(population)
    total_1s = sum(gene.count('1') for gene in population)
    
    while perfect_chromosome not in population_set:        
        population_by_fitness_scores = sorted(population, key = lambda gene: gene.count('1'))

        top_50_percent = population_by_fitness_scores[POPULATION_SIZE//2:]

        children = repopulate(top_50_percent, gene_split_method, gene_length)
        
        if mutate_children:
            children = mutate(children, gene_length-1)

        population = top_50_percent + children
        population_set = set(population)
        
        new_1s_count = sum(gene.count('1') for gene in population)
        
        if total_1s == new_1s_count:
            return 0

        epochs += 1
        total_1s = new_1s_count
    
    return epochs