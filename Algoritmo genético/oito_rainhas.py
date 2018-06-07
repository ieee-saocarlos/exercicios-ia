import random

def board(cromossome, state):

        for i in range(1, 9):
            print ('---------------------------------')
            places = '|   |   |   |   |   |   |   |   |'
            k = 0
            for gene in cromossome[state]:
                k += 1
                #TODO: find a way to put the queens in places
                if gene + i == 9:
                    places = places.replace(' ', 'M', k*3-1)
                    places = places.replace('M', ' ', k*3-2)

            print (places)
        print('---------------------------------')
        print(cromossome)

def generate_cromossomes(n):
    cromossomes = []
    for i in range (0, n):
        gene = []
        for j in range(0, 8):
            position = random.randint(1, 8)
            gene.append(position)
        cromossomes.append(gene)
    return cromossomes

def crossover(cromossomes):
    k = 0
    children = []
    while k < 2:
        k += 1
        child = []
        for i in range(0, 8):
            bit = random.randint(0, 1)
            child.append(cromossomes[bit][i])
        children.append(child)
    return children

def mutation(cromossomes):
    for k in range (0, 2):
        for l in range (0, 4):
            coluna = random.randint(0, 7)
            linha = random.randint(1, 8)
            cromossomes[k][coluna] = linha

    return cromossomes

def verify_possible_solution(possible_solution):

    k = 0

    p = 1
    s = 1
    diagonal11 = []
    diagonal12 = []
    diagonal21 = []
    diagonal22 = []

    for gene in possible_solution[0]:

        if possible_solution[0].count(gene) != 1:
            p = -1

        k += 1
        diagonal11.append(gene - k)
        diagonal12.append(gene + k)


    for j in diagonal11:
        if diagonal11.count(j) != 1:
            p = -1
    for j in diagonal12:
        if diagonal12.count(j) != 1:
            p = -1


    k = 0
    for gene in possible_solution[1]:

        if possible_solution[1].count(gene) != 1:
            s = -1

        k += 1
        diagonal21.append(gene - k)
        diagonal22.append(gene + k)

    for j in diagonal21:
        if diagonal21.count(j) != 1:
            s = -1
    for j in diagonal22:
        if diagonal22.count(j) != 1:
            s = -1

    if p == 1:
        return 0
    elif s == 1:
        return 1
    else:
        return -1

def main():
    state = -1
    parents = generate_cromossomes(2)
    generation = 0
    while state == -1:
        children = crossover(parents)
        parents = mutation(children)
        state = verify_possible_solution(parents)
        generation += 1

    print(state)
    print('A última geração foi a de número {}'.format(generation))
    board(parents, state)

if (__name__ == '__main__'):
    main()