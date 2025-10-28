from imports import choices, randint

OPPOSITE_GENE_MAP = {'1' : '0', '0' : '1'}

def mutate(children, gene_length):
    for i, child in enumerate(children):
        should_mutate = choices([False, True], [.5, .5])
        
        if should_mutate:
            index_of_gene_to_mutate = randint(0, gene_length)
            current_gene = child[index_of_gene_to_mutate]
            children[i] = child[:index_of_gene_to_mutate] + OPPOSITE_GENE_MAP[current_gene] + child[index_of_gene_to_mutate+1:]
    return children



if __name__ == '__main__':
    print(mutate(['11'], 3))