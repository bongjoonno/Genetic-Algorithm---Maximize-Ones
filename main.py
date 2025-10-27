from constants import POPULATION_SIZE
from generate_population import generate_population
from repopulate import split_genes_middle, split_genes_random
from genetic_evolution import genetic_evolution

def main():
    population = generate_population(POPULATION_SIZE)
    convergence_for_middle_split = genetic_evolution(population, split_genes_middle)
    convergence_for_random_split = genetic_evolution(population, split_genes_random)
    
    return convergence_for_middle_split, convergence_for_random_split

if __name__ == '__main__':
    print(main())