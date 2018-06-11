from random import *


def criar_pais(numero):
    cromossomos = []
    for i in range(0, numero):
        gene = []
        for j in range(0,8):
            posicao = randint(1,8)
            gene.append(posicao)
        cromossomos.append(gene)

    return cromossomos


def verificar(cromossomos):
    a = [0,0]

    for i in range(0,2):
        for posicao1 in range(0,8):
            for posicao2 in range(0,8):
                if posicao1 != posicao2:
                    if cromossomos[i][posicao1] == cromossomos[i][posicao2]:
                        a[i] = 1
                    if abs(cromossomos[i][posicao1] - cromossomos[i][posicao2]) == abs(posicao1 - posicao2):
                        a[i] = 1

    if a[0] == 0:
        return 0
    elif a[1] == 0:
        return 1
    else:
        return -1


def criar_filhos(pais):
    cromossomos = []
    for i in range(0,2):
        gene = []
        for j in range(0,8):
            pai = randint(0,1)
            gene.append(pais[pai][j])
        cromossomos.append(gene)

    return cromossomos

def mutacao(pais):
    for i in range(0,2):
        for j in range(0,4):
            lugar = randint(0,7)
            posicao = randint(1,8)
            pais[i][lugar] = posicao

    return pais


def criar_tabela(cromossomo):
    for linha in range(0,8):
        print (' ---------------------------------')
        print ' |  ' * (cromossomo[linha] - 1), '| M | ', ' |  ' *(8 - cromossomo[linha])
    print (' ---------------------------------')


pais = criar_pais(2)
valor = verificar(pais)
geracao = 0
while valor == -1:
    filhos = criar_filhos(pais)
    pais = mutacao(filhos)
    valor = verificar(pais)
    geracao += 1

print 'O cromossomo', valor,'', pais[valor],' resolve o problema na geracao', geracao
criar_tabela(pais[valor])
