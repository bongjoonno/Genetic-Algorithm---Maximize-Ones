from constants import POPULATION_SIZE
from generate_population import generate_population
from repopulate import split_genes_middle, split_genes_random
from genetic_evolution import genetic_evolution

def main():
    for gene_length in range(2, 100, 2):
        population = generate_population(POPULATION_SIZE, gene_length = gene_length)
        perfect_population = ['1'*gene_length for _ in range(POPULATION_SIZE)]
       
        convergence_for_middle_split = genetic_evolution(population = population, 
                                                         perfect_population = perfect_population,
                                                         gene_split_method = split_genes_middle, 
                                                         gene_length = gene_length)
        
        convergence_for_random_split = genetic_evolution(population = population, 
                                                         perfect_population = perfect_population,
                                                         gene_split_method = split_genes_random, 
                                                         gene_length = gene_length)
    
        print(gene_length, convergence_for_middle_split, convergence_for_random_split)

if __name__ == '__main__':
    print(main())