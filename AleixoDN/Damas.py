import random as rand

def geracao_zero():
    geracao = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for i in range(16):
        for j in range(8):
            geracao[i].append(rand.randint(0, 7))
    return geracao

print "\n  ---------------------\n  --Desafio das Damas--\n  ---------------------\n"

print geracao_zero()
