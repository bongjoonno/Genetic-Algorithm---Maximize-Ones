from imports import plt
from constants import MAIN_DIRECTORY

FIGURE_PATH = f'{MAIN_DIRECTORY}\\convergence plots\\plot.png'

def generate_charts(gene_to_convergence_dicts: list[dict]):
    for gene_to_convergence_dict in gene_to_convergence_dicts:
        gene_lengths = list(gene_to_convergence_dict.keys())
        convergences = list(gene_to_convergence_dict.values())

        plt.plot(gene_lengths, convergences, label = 'middle')
        plt.plot(gene_lengths, convergences, label = 'random')

    plt.title('Middle vs. Random Crossover')
    plt.xlabel('Gene Length')
    plt.ylabel('Convergence Time ( In Generations)', rotation = 0)
    
    plt.savefig(FIGURE_PATH)