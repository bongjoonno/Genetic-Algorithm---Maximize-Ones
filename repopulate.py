from constants import GENE_LENGTH, HALF_GENE_LENGTH
from imports import shuffle, randint

def repopulate(parents, split_method):
    shuffle(parents)

    children = []

    for i in range(0, len(parents) - 1, 2):
        child_a, child_b = create_children(*split_method(parents[i], parents[i+1]))
        children.extend([child_a, child_b])
    
    return children

def split_genes_middle(parent_a, parent_b):
    first_half_parent_a = parent_a[:HALF_GENE_LENGTH]
    second_half_parent_a = parent_a[HALF_GENE_LENGTH:]

    first_half_parent_b = parent_b[:HALF_GENE_LENGTH]
    second_half_parent_b = parent_b[HALF_GENE_LENGTH:]
    
    return (first_half_parent_a,
           first_half_parent_b,
           second_half_parent_a,
           second_half_parent_b)

def split_genes_random(parent_a, parent_b):
    split_point = randint(1, GENE_LENGTH - 1)
    
    first_half_parent_a = parent_a[:split_point]
    second_half_parent_a = parent_a[split_point:]

    first_half_parent_b = parent_b[:split_point]
    second_half_parent_b = parent_b[split_point:]
    
    return (first_half_parent_a,
           first_half_parent_b,
           second_half_parent_a,
           second_half_parent_b)
        
def create_children(
    first_half_parent_a, 
    first_half_parent_b, 
    second_half_parent_a, 
    second_half_parent_b):

    child_a = first_half_parent_a + second_half_parent_b
    child_b = first_half_parent_b + second_half_parent_a

    return child_a, child_b