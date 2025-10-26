from imports import choice
from constants import GENE_LENGTH

def generate_population(population_size):
    population = []

    for _ in range(population_size):
        gene = []

        for _ in range(GENE_LENGTH):
            gene.append(choice(['0', '1']))
        
        population.append(''.join(gene))
    
    return population