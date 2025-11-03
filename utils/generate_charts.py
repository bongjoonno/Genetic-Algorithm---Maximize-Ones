from imports import plt
from constants import MINIMUM_GENE_LENGTH, MAXIMUM_GENE_LENGTH, PROJECT_DIRECTORY

FIGURE_PATH = PROJECT_DIRECTORY / 'convergence plots' / f'{MINIMUM_GENE_LENGTH}-{MAXIMUM_GENE_LENGTH} Gene Length'

def generate_charts(genetic_operators_dict):
        plt.figure(figsize=(12, 9))
        
        for operator, information_dict in genetic_operators_dict.items():
                plt.plot(information_dict['gene_lengths_to_convergences'].keys(), 
                         information_dict['gene_lengths_to_convergences'].values(), 
                         label = operator)

        plt.title('Genetic Operators | OneMax')
        plt.xlabel('Gene Length')
        plt.ylabel('Convergence Time (Generations)')
        plt.legend()
        plt.savefig(FIGURE_PATH)