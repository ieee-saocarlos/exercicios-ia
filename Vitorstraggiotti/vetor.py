

n = input('quntos numeros sera digitado: ')
print'digite uma lista com', n, 'numeros'
vetor = input()
vetor_inverso = [0] * n
for i in range(1,n+1):
    vetor_inverso[i-1] = vetor[n-i]
print 'A sequencia em ordem inversa eh: ', vetor_inverso
