from imports import choices

def mutate(children):
    for child in children:
        should_mutate = choices([False, True], [.90, .10])
    pass



if __name__ == '__main__':
    print(mutate(['1100']))