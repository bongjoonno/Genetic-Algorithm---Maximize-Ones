from constants import POPULATION_SIZE, GENE_LENGTH, CUR_PATH

def log(average_convergence):
    with CUR_PATH.open('a') as f:
        f.write(f'''
RANDOM POINT CROSSOVER
POPULATION_SIZE = {POPULATION_SIZE}
GENE_LENGTH = {GENE_LENGTH}
AVG_CONVERGENCE = {average_convergence}

''')

if __name__ == '__main__':
    log(5)