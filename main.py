from genetic_algorithm.full_simulation import full_simulation
from utils.generate_charts import generate_charts

def main():
    gene_length_to_convergences = full_simulation()
    generate_charts(gene_length_to_convergences)

if __name__ == '__main__':
    main()