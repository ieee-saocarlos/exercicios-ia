
print "Entre com duas listas de numeros e sera feita a intersecao"

lista_1 = input("Primeira lista: ")
lista_2 = input("Segunda lista: ")
lista_intersec = []


comprimento_1 = len(lista_1)
comprimento_2 = len(lista_2)


for i in range(0, comprimento_1, 1):
    for j in range(0, comprimento_2, 1):
        if(lista_1[i] == lista_2[j]):
            lista_intersec.append(lista_1[i])
x = 0
j = 0

for i in range(0, len(lista_intersec), 1):
    j = j+1
    if(lista_intersec.count(lista_intersec[i]) != 1):
        lista_intersec.remove(lista_intersec[i])
        i = i-1
        x = x+1
    if((len(lista_intersec) - x) == j):
        break



print lista_intersec
