from imports import np
from constants import POPULATION_SIZE
from generate_population import generate_population
from repopulate import split_genes_middle, split_genes_random
from genetic_evolution import genetic_evolution
from log import create_file_path, save_dicts_to_yaml
from generate_charts import generate_charts


# Length of Gene must be > 2 as parental splitting is not possible without at least one gene per parent (e.g. at least 2)
MINIMUM_GENE_LENGTH = 2

def main():
    gene_length_to_middle_split_convergences, 
    gene_length_to_random_split_convergences,
    gene_length_to_random_split_mutate_convergences = {}, {}, {}

    gene_length_low = MINIMUM_GENE_LENGTH
    gene_length_high = 100
    step_size = 1

    for gene_length in range(gene_length_low, gene_length_high, step_size):
        population = generate_population(POPULATION_SIZE, gene_length = gene_length)
        perfect_population = ['1'*gene_length for _ in range(POPULATION_SIZE)]
       
        convergence_for_middle_split = genetic_evolution(population = population, 
                                                         perfect_population = perfect_population,
                                                         gene_split_method = split_genes_middle, 
                                                         gene_length = gene_length,
                                                         mutate_children = False)
        
        convergence_for_random_split = genetic_evolution(population = population, 
                                                         perfect_population = perfect_population,
                                                         gene_split_method = split_genes_random, 
                                                         gene_length = gene_length,
                                                         mutate_children = False)
        
        convergence_for_random_split_mutate = genetic_evolution(population = population, 
                                                         perfect_population = perfect_population,
                                                         gene_split_method = split_genes_random, 
                                                         gene_length = gene_length,
                                                         mutate_children = True)
    
        gene_length_to_middle_split_convergences[gene_length] = convergence_for_middle_split
        gene_length_to_random_split_convergences[gene_length] = convergence_for_random_split
        gene_length_to_random_split_mutate_convergences[gene_length] = convergence_for_random_split_mutate

    middle_split_file_path = create_file_path(gene_length_low = gene_length_low,
                                              gene_length_high = gene_length_high,
                                              gene_split_method = 'middle-split')

    random_split_file_path = create_file_path(gene_length_low = gene_length_low,
                                              gene_length_high = gene_length_high,
                                              gene_split_method = 'random-split')
    
    random_split_mutate_file_path = create_file_path(gene_length_low = gene_length_low,
                                              gene_length_high = gene_length_high,
                                              gene_split_method = 'random-split-mutate')
    
    
    save_dicts_to_yaml(file_path = middle_split_file_path, 
                       gene_to_convergence_dict = gene_length_to_middle_split_convergences)
    
    save_dicts_to_yaml(file_path = random_split_file_path, 
                       gene_to_convergence_dict = gene_length_to_random_split_convergences)
    
    save_dicts_to_yaml(file_path = random_split_mutate_file_path, 
                       gene_to_convergence_dict = gene_length_to_random_split_mutate_convergences)

    return (gene_length_to_middle_split_convergences, gene_length_to_random_split_convergences, gene_length_to_random_split_mutate_convergences)

if __name__ == '__main__':
    (gene_length_to_middle_split_convergences, 
    gene_length_to_random_split_convergences, 
    gene_length_to_random_split_mutate_convergences) = main()
    
    generate_charts(gene_length_to_middle_split_convergences, gene_length_to_random_split_convergences, gene_length_to_random_split_mutate_convergences)