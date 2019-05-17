print "\n  -------------------------\n  --Exercicio 4 - Lista 1--\n  -------------------------" #Titulo

i = 600851475143
n = 1
j = 0

while (i != 1): #Verifica de o numero ja foi inteiramente divitido por numeros primos
    n = n+1
    while (i % n == 0): #Verifica se o numero ainda eh divisivel pelo numero primo (n) em loop
        i = i / n #Divide o numero pelo seu menor divisor primo
#        print n, i

        if i == 1:   break #Quebra o loop caso ja tenha sido dividido ao maximo
        if i % n != 0:   n = n+1 #Incrementa o numero divisor caso o numero n possa mais ser dividido pelo anterior

print "\nQual o maior fator primo do numero 600851475143?" #Pergunta
print "\n --> Resposta = ", n, "\n\n" #Resposta
