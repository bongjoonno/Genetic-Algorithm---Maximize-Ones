from imports import choice

def generate_population(population_size, gene_length):
    population = []

    for _ in range(population_size):
        gene = []

        for _ in range(gene_length):
            gene.append(choice(['0', '1']))
        
        population.append(''.join(gene))
    
    return population