from imports import yaml
from constants import MINIMUM_GENE_LENGTH, MAXIMUM_GENE_LENGTH, PROJECT_DIRECTORY

LOGGING_DIRECTORY = PROJECT_DIRECTORY / 'convergence_data'

def create_file_path(gene_split_method):
    return LOGGING_DIRECTORY / f'{MINIMUM_GENE_LENGTH}-{MAXIMUM_GENE_LENGTH} {gene_split_method}.yaml'

def save_dicts_to_yaml(file_path, gene_to_convergence_dict):
    with open(file_path, 'w') as f:
        yaml.dump(gene_to_convergence_dict, f)