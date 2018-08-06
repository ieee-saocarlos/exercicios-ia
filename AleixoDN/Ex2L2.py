print "\n  -------------------------\n  --Exercicio 2 - Lista 2--\n  -------------------------" #Titulo
print "\nConsidere um vetor da forma v = [a, b, c, d, e, f, g, h, i, j]"
print "\nFaca um Programa que leia um vetor de 10 numeros reais e mostre-os na ordem inversa.\n"

charbytes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] #Letras que indicam o local no vetor a ser editado
vec = [0] * 10 #Vetor a ser editado e invertido
j = 9

for i in charbytes: #Roda os elementos do vetor a serem editados
    print "Quanto ao elemento", "'%s'" % i, "do vetor..." #Mostra o elemento do vetor que o usuario vai editar
    vec[j] = int(raw_input ("...digite seu valor: ")) #Armazena os valores de forma invertida no vetor
    j -= 1

print "\n --> Resposta = ", vec, "\n\n" #Resposta
