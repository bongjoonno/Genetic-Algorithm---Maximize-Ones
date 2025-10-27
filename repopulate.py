from imports import shuffle, randint

def repopulate(parents, gene_split_method, gene_length):
    shuffle(parents)

    children = []

    for i in range(0, len(parents) - 1, 2):
        child_a, child_b = create_children(*gene_split_method(parents[i], parents[i+1], gene_length))
        children.extend([child_a, child_b])
    
    return children

def create_children(
    first_half_parent_a, 
    first_half_parent_b, 
    second_half_parent_a, 
    second_half_parent_b):

    child_a = first_half_parent_a + second_half_parent_b
    child_b = first_half_parent_b + second_half_parent_a

    return child_a, child_b

def split_genes_middle(parent_a, parent_b, gene_length):
    first_half_parent_a = parent_a[:gene_length//2]
    second_half_parent_a = parent_a[gene_length//2:]

    first_half_parent_b = parent_b[:gene_length//2]
    second_half_parent_b = parent_b[gene_length//2:]
    
    return (first_half_parent_a,
           first_half_parent_b,
           second_half_parent_a,
           second_half_parent_b)

def split_genes_random(parent_a, parent_b, gene_length):
    split_point = randint(1, gene_length - 1)
    
    first_half_parent_a = parent_a[:split_point]
    second_half_parent_a = parent_a[split_point:]

    first_half_parent_b = parent_b[:split_point]
    second_half_parent_b = parent_b[split_point:]
    
    return (first_half_parent_a,
           first_half_parent_b,
           second_half_parent_a,
           second_half_parent_b)