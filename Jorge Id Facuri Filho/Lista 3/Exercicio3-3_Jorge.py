#---------------------FUNCTIONS--------------------





#----------------------------------------------------#

#----------------PRIMEIRA PARTE----------------------
lista = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nova_lista = []


for n in lista:
   if(n % 2 == 0):
    nova_lista.append(n)

print "A NOVA LISTA COM NUMEROS PARES:\n ",nova_lista



 #---------------SEGUNDA PARTE--------------------#

print"------------------------------"
print"COLOCANDO-SE NUMEROS ALEATORIOS"
print" "
print"DIGITE A SEQUENCIA "
print"DIGITE s PARA FINALIZAR A SEQUENCIA"


lista2 = []
nova_lista2 = []

#---------------CRIAR LISTA----------------------#
x = 0
print "COLOQUE OS VALORES: "
while(x != 's'):
    x = raw_input("COLOQUE OS VALORES: ")
    if(x != 's'):
      lista2.append(x)
      lista2_ordenada = sorted(lista2)

print lista2
print lista2_ordenada

#----------------COLOCAR PARES-------------------#

for n in lista2_ordenada:
    if(int(n) % 2 == 0):
        nova_lista2.append(n)
print "OS NUMEROS PARES DA NOVA LISTA SAO :",nova_lista2
