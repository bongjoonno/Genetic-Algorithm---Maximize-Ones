from imports import np, tqdm
from constants import POPULATION_SIZE, GENETIC_OPERATORS
from generate_population import generate_population
from repopulate import split_genes_middle, split_genes_random
from genetic_evolution import genetic_evolution
from log import create_file_path, save_dicts_to_yaml
from generate_charts import generate_charts


# Length of Gene must be > 2 as parental splitting is not possible without at least one gene per parent (e.g. at least 2)
MINIMUM_GENE_LENGTH = 2

def main():
    gene_split_methods_funcs = [split_genes_middle, split_genes_middle, split_genes_random, split_genes_random]
    mutate_children = [False, True, False, True]
    gene_length_to_convergences = [{}, {}, {}, {}]

    gene_length_low = 1
    gene_length_high = 1_000
    step_size = 2

    for gene_length in tqdm(range(gene_length_low, gene_length_high, step_size)):
        population = generate_population(POPULATION_SIZE, gene_length = gene_length)
        perfect_chromosome = '1'*gene_length
        
        for i in range(len(gene_length_to_convergences)):
            gene_length_to_convergences[i][gene_length] = genetic_evolution(population = population, 
                                                                            perfect_chromosome = perfect_chromosome,
                                                                            gene_split_method = gene_split_methods_funcs[i], 
                                                                            gene_length = gene_length,
                                                                            mutate_children = mutate_children[i])
            
        
    for i in range(len(GENETIC_OPERATORS)):
        file_path = (create_file_path(gene_length_low = gene_length_low,
                                        gene_length_high = gene_length_high,
                                        gene_split_method = GENETIC_OPERATORS[i]))
        
        save_dicts_to_yaml(file_path = file_path, 
                            gene_to_convergence_dict = gene_length_to_convergences[i])

    return gene_length_to_convergences

if __name__ == '__main__':
    generate_charts(main())