from imports import plt
from constants import MAIN_DIRECTORY

FIGURE_PATH = f'{MAIN_DIRECTORY}\\convergence plots\\plot.png'

def generate_charts(middle_split_dict, random_split_dict):
        plt.figure(figsize=(12, 9))

        plt.plot(random_split_dict.keys(), random_split_dict.values(), label = 'Random Crossover')
        plt.plot(middle_split_dict.keys(), middle_split_dict.values(), label = 'Middle Crossover')

        plt.title('Middle vs. Random Crossover')
        plt.xlabel('Gene Length')
        plt.ylabel('Convergence Time (Generations)')
        plt.legend()
        plt.savefig(FIGURE_PATH)