from imports import pickle
from constants import MINIMUM_GENE_LENGTH, MAXIMUM_GENE_LENGTH, PROJECT_DIRECTORY

LOGGING_PATH = PROJECT_DIRECTORY / 'convergence_data' / f'{MINIMUM_GENE_LENGTH}-{MAXIMUM_GENE_LENGTH}.pkl'

def save_dicts_to_pkl(genetic_operators_dict):
    with open(LOGGING_PATH, 'wb') as f:
        pickle.dump(genetic_operators_dict, f)