from genetic_algorithm.full_simulation import run_full_simulation
from utils.generate_charts import generate_charts

def main():
    genetic_operators_dict = run_full_simulation()
    generate_charts(genetic_operators_dict)

if __name__ == '__main__':
    main()