import time
import random as rnd
from collections import OrderedDict

ti = time.time()

def caminhos(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in caminhos(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0:1] + perm[i:])
        return tmp

val_dist = {'ab':13, 'ba':13, 'ac':9, 'ca':9, 'ad':3, 'da':3, 'ae':15, 'ea':15, 'af':5, 'fa':5, 'bc':12, 'cb':12, 'bd':9, 'db':9,
'be':12, 'eb':12, 'bf':6, 'fb':6, 'cd':10, 'dc':10, 'ce':3, 'ec':3, 'cf':4, 'fc':4, 'de':12, 'ed':12, 'df':13, 'fd':13, 'ef':15, 'fe':15}

def reproducao(p1, p2, n, reprod_por_geracao):
    dist_menor = 100
    for m in range(n):
        for x in range(reprod_por_geracao):
            distancia = 0
            aberracao = []

            #reproducao entre os parentais
            while not ('a' in aberracao and 'b' in aberracao and 'c' in aberracao and 'd' in aberracao and 'e' in aberracao and 'f' in aberracao):
                i = rnd.randint(0,5)
                j = rnd.randint(0,5)
                #print "passo0", p1[i], p1[j], aberracao
                aberracao.append(p1[i])
                #aberracao.append(p1[i+1])
                aberracao.append(p2[j])
                #aberracao.append(p2[j+1])
            #print "passo1"
            aberracao = list(OrderedDict((x, True) for x in aberracao))

            #crossing over
            '''cross1 = rnd.randint(0,5)
            cross2 = rnd.randint(0,5)
            aux = aberracao[cross1]
            aberracao[cross1] = aberracao[cross2]
            aberracao[cross2] = aux'''
            #print "passo2"

            #distancia percorrida
            for n in range(len(aberracao)-1):
                distancia += val_dist[aberracao[n]+aberracao[n+1]]

            #escolha dos melhores genes
            if distancia <= dist_menor:
                dist_menor = distancia
                parent = aberracao
            #print "Parental",x,", reproducao",m,parent

        #reproduzir novamente o melhor gene
        #print "passo3", parent1_g1
        p1 = parent
        p2 = parent

    return parent

reprod = 35
ger = 25

gene1 = 'abcdef'
gene2 = 'fedcba'

resp = reproducao(gene1, gene2, ger, reprod)

distancia = 0
for n in range(len(resp)-1):
    distancia += val_dist[resp[n]+resp[n+1]]

print ger, "geracoes com", reprod, "reproducoes cada:"
print "Resposta:", resp, "com distancia", distancia

'''dist_final = 100
resp = []
for j in range(len(caminhos('abcdef'))):
    distancia = 0

    for i in range(len(caminhos('abcdef')[j])-1):
        distancia += val_dist[caminhos('abcdef')[j][i]+caminhos('abcdef')[j][i+1]]

    #print distancia

    if distancia <= dist_final:
        dist_final = distancia
        resp = caminhos('abcdef')[j]

print "Menor distancia =", dist_final
print "Caminho:", resp'''

tf = time.time()
print "Tempo:",tf-ti, "segundos"
