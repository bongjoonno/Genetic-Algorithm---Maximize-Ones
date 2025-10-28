from imports import yaml
from constants import MAIN_DIRECTORY

LOGGING_DIRECTORY = f'{MAIN_DIRECTORY}\\convergence data\\'

def create_file_path(gene_length_low, gene_length_high, gene_split_method):
    return f'{LOGGING_DIRECTORY}{gene_length_low}-{gene_length_high} {gene_split_method}.yaml'

def save_dicts_to_yaml(file_path, gene_to_convergence_dict):
    with open(file_path, 'w') as f:
        yaml.dump(gene_to_convergence_dict, f)


if __name__ == '__main__':
    print(create_file_path(0, 100, 'random'))