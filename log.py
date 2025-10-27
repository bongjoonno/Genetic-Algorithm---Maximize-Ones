from constants import POPULATION_SIZE
from imports import Path

LOGGING_PATH = Path.cwd() / 'log.txt'

def log(average_convergence, gene_split_method, gene_length):
    with LOGGING_PATH.open('a') as f:
        f.write(f'''
{gene_split_method}
POPULATION_SIZE = {POPULATION_SIZE}
GENE_LENGTH = {gene_length}
AVG_CONVERGENCE = {average_convergence}

''')

if __name__ == '__main__':
    log(5)