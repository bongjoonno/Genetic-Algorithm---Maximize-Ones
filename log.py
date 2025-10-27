from imports import Path, json

LOGGING_DIRECTORY = str(Path.cwd())

def create_file_path(gene_length_low, gene_length_high, gene_split_method):
    return f'{LOGGING_DIRECTORY}\\{gene_length_low}-{gene_length_high} {gene_split_method}.json'

def save_dicts_to_json(file_path, gene_to_convergence_dict):
    with open(file_path, 'w') as f:
        json.dump(gene_to_convergence_dict, f)


if __name__ == '__main__':
    print(create_file_path(0, 100, 'random'))