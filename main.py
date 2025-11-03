from genetic_algorithm.full_simulation import run_full_simulation
from utils.generate_charts import generate_charts
from utils.log import save_dicts_to_pkl

def main():
    genetic_operators_dict = run_full_simulation()

    save_dicts_to_pkl(genetic_operators_dict)
    
    generate_charts(genetic_operators_dict)

if __name__ == '__main__':
    main()