from imports import tqdm
from constants import POPULATION_SIZE, MINIMUM_GENE_LENGTH, MAXIMUM_GENE_LENGTH, SIMULATION_STEP_SIZE
from genetic_algorithm.generate_population import generate_population
from genetic_algorithm.repopulate import split_genes_middle, split_genes_random
from genetic_algorithm.genetic_evolution import genetic_evolution

def run_full_simulation():
    genetic_operators_dict = {'Middle Crossover' : 
                             {'gene_split_function' : split_genes_middle,
                              'mutate_children' : False,
                              'gene_lengths_to_convergences' : {}}, 

                              'Middle Crossover Mutation' : 
                             {'gene_split_function' : split_genes_middle,
                              'mutate_children' : True,
                              'gene_lengths_to_convergences' : {}},

                              'Random Crossover' : 
                             {'gene_split_function' : split_genes_random,
                              'mutate_children' : False,
                              'gene_lengths_to_convergences' : {}},

                             'Random Crossover Mutation' : 
                            {'gene_split_function' : split_genes_random,
                             'mutate_children' : True,
                             'gene_lengths_to_convergences' : {}}
                            }
        
    for gene_length in tqdm(range(MINIMUM_GENE_LENGTH, MAXIMUM_GENE_LENGTH, SIMULATION_STEP_SIZE)):
        population = generate_population(POPULATION_SIZE, gene_length = gene_length)
        perfect_chromosome = '1'*gene_length
        
        for operator, information_dict in genetic_operators_dict.items():
            genetic_operators_dict[operator]['gene_lengths_to_convergences'][gene_length] = genetic_evolution(population = population, 
                                                                                                        perfect_chromosome = perfect_chromosome,
                                                                                                        gene_split_method = information_dict['gene_split_function'], 
                                                                                                        gene_length = gene_length,
                                                                                                        mutate_children = information_dict['mutate_children'])
    
    return genetic_operators_dict