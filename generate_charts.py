from imports import plt
from constants import MAIN_DIRECTORY, GENETIC_OPERATORS

FIGURE_PATH = f'{MAIN_DIRECTORY}\\convergence plots\\plot.png'

def generate_charts(gene_length_to_convergences):
        plt.figure(figsize=(12, 9))
        
        for i, gene_length_to_convergence in enumerate(gene_length_to_convergences):
                plt.plot(gene_length_to_convergence.keys(), gene_length_to_convergence.values(), label = GENETIC_OPERATORS[i])

        plt.title('Genetic Operators | OneMax')
        plt.xlabel('Gene Length')
        plt.ylabel('Convergence Time (Generations)')
        plt.legend()
        plt.savefig(FIGURE_PATH)