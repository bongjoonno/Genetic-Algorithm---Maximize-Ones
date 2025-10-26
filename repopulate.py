from constants import GENE_LENGTH, HALF_GENE_LENGTH
from imports import shuffle

def repopulate(parents):
    shuffle(parents)

    children = []

    for i in range(0, len(parents) - 1, 2):
        child_a, child_b = create_children(parents[i], parents[i+1])
        children.extend([child_a, child_b])
    
    return children

def create_children(parent_a, parent_b):
    first_half_parent_a = parent_a[:HALF_GENE_LENGTH]
    second_half_parent_a = parent_a[HALF_GENE_LENGTH:]

    first_half_parent_b = parent_b[:HALF_GENE_LENGTH]
    second_half_parent_b = parent_b[HALF_GENE_LENGTH:]

    child_a = first_half_parent_a + second_half_parent_b
    child_b = first_half_parent_b + second_half_parent_a

    return child_a, child_b