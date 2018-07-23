from random import *

possibilidades = []




def verificar(rainhas):
    for i in range(8):
        for k in range(8):
            if k == i:
                continue

            if rainhas[k] == rainhas[i]:
                return 0

            if rainhas[k] - rainhas[i] == k - i or rainhas[k] - rainhas[i] == i - k:
                return 0

    return 1




def misturar(pai1, pai2):
    if pai1 == pai2 == None:
        return ([randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8)])

    if pai1 == None:
        misturar(pai2, pai2)

    if pai2 == None:
        misturar(pai1, pai1)

    m = []
    m.append(pai1)
    m.append(pai2)
    return ([m[randint(0,1)][randint(0,7)], m[randint(0,1)][randint(0,7)], m[randint(0,1)][randint(0,7)], m[randint(0,1)][randint(0,7)], m[randint(0,1)][randint(0,7)], m[randint(0,1)][randint(0,7)], m[randint(0,1)][randint(0,7)], m[randint(0,1)][randint(0,7)]])




def mutacao(gene):
    if gene == None:
        pass
    else:
        chance = randint(1,10)
        if chance < 5:
            k = randint(1,8)
            p = randint(0,7)
            if k != gene[p]:
                gene[p] = k

            else:
                mutacao(gene)
        else:
            k = randint(0,7)
            p = randint(0,7)
            if k != p and gene[k] != gene[p]:
                troc = gene[k]
                gene[k] = gene[p]
                gene[p] = troc

            else:
                mutacao(gene)





for i in range(2):
    possibilidades.append([randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8), randint(1,8)])


a = 0

while verificar(possibilidades[a]) == 0:
    print possibilidades[a]
    x = randint(0,len(possibilidades) - 1)
    y = randint(0,len(possibilidades) - 1)
    if x != y:
        possibilidades.append(misturar(possibilidades[x], possibilidades[y]))
        mut = randint(1,100)
        if mut % 2 == 0:
            mutacao(possibilidades[a+1])

    else:
        a -= 1
    a += 1

print 'A combinacao', possibilidades[a], 'eh uma solucao'
