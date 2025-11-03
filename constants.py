from imports import Path
from genetic_algorithm.repopulate import split_genes_middle, split_genes_random

POPULATION_SIZE = 400

# Length of Gene must be > 2 as parental splitting is not possible without at least one gene per parent (e.g. at least 2)
MINIMUM_GENE_LENGTH = 2
MAXIMUM_GENE_LENGTH = 1000
SIMULATION_STEP_SIZE = 5

PROJECT_DIRECTORY = Path.cwd()

GENETIC_OPERATORS = {'Middle Crossover' : 
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