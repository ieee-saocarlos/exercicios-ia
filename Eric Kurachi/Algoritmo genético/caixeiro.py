import random

class Cromossome():
    def __init__(self, order):
        self.order = order

    def distance(self):
        #distancias entre as cidades
        dist = {'AB': 13, 'AC':9, 'AD':3, 'AE':15, 'AF':5, 'BC':12, 'BD':9, 'BE':12, 'BF':6, 'CD':10, 'CE':3, 'CF':4, 'DE':12, 'DF':13, 'EF':15}
        totalDistance = 0
        #para cada caminho entre duas cidades encontramos a distancia
        for i in range(0, 5):

            if (ord(self.order[i]) < ord(self.order[i+1])):
                route = self.order[i] + self.order[i+1]
            else:
                route = self.order[i+1] + self.order[i]

            totalDistance += dist[route]

        return totalDistance

def generateCromossome():
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    order = []
    #cria um cromossomo escolhendo aletoriamente a ordem das cidades
    for j in range (0, 6):
        k = 5 - j
        letterChoose = random.randint(0, k)
        order.append(letters[letterChoose])
        del letters[letterChoose]

    return Cromossome(order)

def createGeneration(size):
    generation = []
    #cria uma geracao do tamanho desejado criando o numero pedido de cromossomos
    for i in range(0, size):
        cromossome = generateCromossome()
        generation.append(cromossome)
    return generation

def crossover(parent_X, parent_Y):
    order = []
    cromossome = generateCromossome()
    #realiza o crossover escolhendo 3 letras que serao selecionadas do pai e 3 da mae e colocando na ordem em que aparecem
    for i in range (0, 6):
        if parent_X.order[i] == cromossome.order[0]:
            order.append(cromossome.order[0])
        if parent_X.order[i] == cromossome.order[1]:
            order.append(cromossome.order[1])
        if parent_X.order[i] == cromossome.order[2]:
            order.append(cromossome.order[2])
        if parent_Y.order[i] == cromossome.order[3]:
            order.append(cromossome.order[3])
        if parent_Y.order[i] == cromossome.order[4]:
            order.append(cromossome.order[4])
        if parent_Y.order[i] == cromossome.order[5]:
            order.append(cromossome.order[5])

    cromossome.order = order
    return cromossome


def newGeneration(generation):
    newGeneration = []
    #cria uma geracao cruzando a anterior
    for i in range(0, len(generation), 2):
        child = crossover(generation[i], generation[i+1])
        newGeneration.append(child)
    return newGeneration


def mutation(cromossome):
    position = random.randint(0, 4)
    #troca a ordem de um caminho
    store = cromossome.order[position]
    cromossome.order[position] = cromossome.order[position + 1]
    cromossome.order[position + 1] = store

    return cromossome

def generationMutation(generation):
    #cria uma geracao de individuos que sofreram mutacoes
    for i in range(0, len(generation)):
        mutation(generation[i])
    return generation

def bestCromossomes(group, number):
    distances = []
    best = []
    i = 0
    #preenche uma lista com as distancias
    for cromossome in group:
        distances.append(cromossome.distance())
    #coloca as distancias em ordem crescente
    distances.sort()
    #pega as n menores distancias
    for cromossome in group:
        if i == number:
            break
        if cromossome.distance() <= distances[number-1]:
            i += 1
            best.append(cromossome)

    return best

def main():
    generationSize = 100
    generationNumber = 10
    generation = createGeneration(generationSize)

    for i in range(0, generationNumber):
        best = bestCromossomes(generation, generationSize/2)
        new = newGeneration(generation)
        mutated = generationMutation(new)
        generation = best+mutated

    selected = bestCromossomes(generation, 1)
    print('The best route found is {} and its distance is {}'.format(selected[0].order, selected[0].distance()))

if (__name__ == "__main__"):
    main()