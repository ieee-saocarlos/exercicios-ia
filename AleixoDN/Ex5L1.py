print "\n  -------------------------\n  --Exercicio 5 - Lista 1--\n  -------------------------" #Titulo

a = [1, 2] #Dois primeiros numeros de fibonacci
i = 0 #Variavel ausiliar inicial
sum = 2 #Soma inicia do 3 (soma dos valores iniciais pares)

while (a[((i+1)%2)]<4000000): #Permite calculo ate o primeiro numero maior que 4.000.000
    a[(i%2)] = a[0] + a[1] #Calcula o proximo numero oscilando a coordenada na lista
    if a[(i%2)] % 2 == 0: #Caso o numero calculado seja par...
        sum = sum + a[(i%2)] #...ele sera somado ao valor somado ate entao
#    print a
    i = i + 1 #Incrementa a variavel ausiliar para provocar a oscilacaoda coordenada

print "\nConsiderando os termos da sequencia de Fibonacci cujo valor nao excede 4 milhoes, encontre a soma dos termos pares."
print "\n --> Resposta = ", sum, "\n\n" #Resposta
