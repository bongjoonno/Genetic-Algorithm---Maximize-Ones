from constants import GENE_LENGTH

def create_child(gene):
    left_half = gene[:GENE_LENGTH/2]
    right_half = gene[GENE_LENGTH/2:]

    child_a = left_half + right_half
    child_b = right_half + left_half

    return child_a, child_b