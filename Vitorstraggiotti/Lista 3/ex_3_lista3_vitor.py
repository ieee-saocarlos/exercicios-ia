from random import*

lista = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista_par = []

for i in range(len(lista)):
    if(lista[i] % 2 == 0):
        lista_par.append(lista[i])
print 'lista de elementos pares: ', lista_par

tamanho = raw_input('Digite o tamanho da lista de numeros que sera gerada: ')

lista_aleatoria =[]
lista_par2 =[]
for i in range(int(tamanho)):
    lista_aleatoria.append(randint(0,1001))

print 'lista aleatoria: ', lista_aleatoria

for i in range(len(lista_aleatoria)):
    if(lista_aleatoria[i] % 2 == 0):
        lista_par2.append(lista_aleatoria[i])
print 'lista de elementos pares da lista aleatoria: ', lista_par2
