from imports import yaml
from constants import PROJECT_DIRECTORY

LOGGING_DIRECTORY = PROJECT_DIRECTORY / 'convergence data'

def create_file_path(gene_length_low, gene_length_high, gene_split_method):
    return f'{LOGGING_DIRECTORY}{gene_length_low}-{gene_length_high} {gene_split_method}.yaml'

def save_dicts_to_yaml(file_path, gene_to_convergence_dict):
    with open(file_path, 'w') as f:
        yaml.dump(gene_to_convergence_dict, f)