from imports import np, tqdm
from constants import POPULATION_SIZE, MINIMUM_GENE_LENGTH, MAXIMUM_GENE_LENGTH, SIMULATION_STEP_SIZE, GENETIC_OPERATORS
from genetic_algorithm.generate_population import generate_population
from genetic_algorithm.repopulate import split_genes_middle, split_genes_random
from genetic_algorithm.genetic_evolution import genetic_evolution
from utils.log import create_file_path, save_dicts_to_yaml
from utils.generate_charts import generate_charts

def run_full_simulation():
    for gene_length in tqdm(range(MINIMUM_GENE_LENGTH, MAXIMUM_GENE_LENGTH, SIMULATION_STEP_SIZE)):
        population = generate_population(POPULATION_SIZE, gene_length = gene_length)
        perfect_chromosome = '1'*gene_length
        
        for operator, information_dict in GENETIC_OPERATORS.items():
            GENETIC_OPERATORS[operator]['gene_lengths_to_convergences'][gene_length] = genetic_evolution(population = population, 
                                                                                                        perfect_chromosome = perfect_chromosome,
                                                                                                        gene_split_method = information_dict['gene_split_function'], 
                                                                                                        gene_length = gene_length,
                                                                                                        mutate_children = information_dict['mutate_children'])
        
    for operator, information_dict in GENETIC_OPERATORS.items():
        file_path = (create_file_path(gene_split_method = operator))
        
        save_dicts_to_yaml(file_path = file_path, 
                            gene_to_convergence_dict = information_dict['gene_lengths_to_convergences'])