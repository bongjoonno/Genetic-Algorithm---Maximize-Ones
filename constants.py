from imports import Path

POPULATION_SIZE = 400

# Length of Gene must be > 2 as parental splitting is not possible without at least one gene per parent (e.g. at least 2)
MINIMUM_GENE_LENGTH = 2
MAXIMUM_GENE_LENGTH = 100
SIMULATION_STEP_SIZE = 1

PROJECT_DIRECTORY = Path.cwd()