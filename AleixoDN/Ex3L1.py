print "-------------------------\n--Exercicio 3 - Lista 1--\n-------------------------" #Titulo

soma1 = 0 #Soma dos quadrados
soma2 = 0 #Quadrado da soma

for i in range(1,101): #Roda a soma de quadrados de valores de 1 a 100
    soma1 = soma1 + i*i #Incremento do quadrado do valor do loop

for j in range(1,101): #Roda a soma de valores de 1 a 100
    soma2 = soma2 + j #Incremento do valor do loop
soma2 = soma2*soma2 #Calcula o quadrado da soma

resp = soma1 - soma2 #Subtrai os valores finais dos dois calculos

print "\nEncontre a diferenca entre a soma dos quadrados dos primeiros 100 nume-\nros naturais e o quadrado da soma deles."

print "\n --> Resposta = ", resp, "\n\n" #Imprime a resposta
