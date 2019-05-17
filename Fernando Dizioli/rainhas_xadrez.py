import random, time
from collections import OrderedDict

#gene selecao

def reproducao(p1, p2):

    resposta = []
    while not all(k in resposta for k in range(8)):
        i = random.randint(0, 7)
        j = random.randint(0, 7)

        resposta.append(p1[i])
        resposta.append(p2[j])

    resposta = list(OrderedDict((x, True) for x in resposta))

    cross1 = random.randint(0, 7)
    cross2 = random.randint(0, 7)
    aux = resposta[cross1]
    resposta[cross1] = resposta[cross2]
    resposta[cross2] = aux

    return resposta

parental = [0, 1, 2, 3, 4, 5, 6, 7]

flag = 1
coisas = 0
while flag == 1:
    coisas+=1
    tabuleiro = [[0 for h in range(8)] for w in range(8)]

    selecao = reproducao(parental, parental)

    #print selecao, "flag:", flag
    rainhas_horizontal = [0 for r in range(8)]
    rainhas_diag_princ = [0 for r in range(13)]
    rainhas_diag_sec = [0 for r in range(13)]

    #preenchendo o tabuleiro
    for m in range(8):
        for n in range(8):
            if m == selecao[n]:
                tabuleiro[m][n] = 'X'
        #teste horizontal
        for n in range(8):
            if tabuleiro[m][n] == 'X':
                rainhas_horizontal[m] += 1
    #print "Teste 1:", rainhas_horizontal

    #teste diagonais secundarias
    for p in range(1,14):
        if p < 8:
            for q in range(p+1):
                #print "Teste 2:", q, p-q, tabuleiro[q][p-q],
                if tabuleiro[q][p-q] == 'X':
                    rainhas_diag_sec[p-1] += 1
                #print rainhas_diag_sec
        else:
            for q in range(p-7, 8):
                #print "Teste 2:", q, p-q, tabuleiro[q][p-q],
                if tabuleiro[q][p-q] == 'X':
                    rainhas_diag_sec[p-1] += 1
                #print rainhas_diag_sec

    for x in range(-6, 7):
        if x < 1:
            for y in range(8+x):
                #print "Teste 3: ", y, y-x, tabuleiro[y][y-x],
                if tabuleiro[y][y-x] == 'X':
                    rainhas_diag_princ[x+6] += 1
                #print rainhas_diag_princ
        else:
            for y in range(x, 8):
                #print "Teste 3: ", y, y-x, tabuleiro[y][y-x],
                if tabuleiro[y][y-x] == 'X':
                    rainhas_diag_princ[x+6] += 1
                #print rainhas_diag_princ

    if all(rainhas_horizontal[i] <= 1 for i in range(len(rainhas_horizontal))):
        if all(rainhas_diag_sec[j] <= 1 for j in range(len(rainhas_diag_sec))):
            if all(rainhas_diag_princ[k] <= 1 for k in range(len(rainhas_diag_princ))):
                flag = 0

    parental = selecao

print coisas, "interacoes"

print ' ',
for m in range(7):
    print "_  ",
print "_"
for m in range(8):
    for n in range(8):
        if m == selecao[n]:
            print "| X",
        else: print "| _",
    print "|"
