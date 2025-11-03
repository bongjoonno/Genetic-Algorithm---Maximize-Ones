from imports import plt
from constants import PROJECT_DIRECTORY, GENETIC_OPERATORS

FIGURE_PATH = PROJECT_DIRECTORY / 'convergence plots' / 'plot.png'

def generate_charts():
        plt.figure(figsize=(12, 9))
        
        for operator, information_dict in GENETIC_OPERATORS.items():
                plt.plot(information_dict['gene_lengths_to_convergences'].keys(), 
                         information_dict['gene_lengths_to_convergences'].values(), 
                         label = operator)

        plt.title('Genetic Operators | OneMax')
        plt.xlabel('Gene Length')
        plt.ylabel('Convergence Time (Generations)')
        plt.legend()
        plt.savefig(FIGURE_PATH)