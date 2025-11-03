from imports import Path
from genetic_algorithm.repopulate import split_genes_middle, split_genes_random

POPULATION_SIZE = 400
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