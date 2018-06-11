vet = []

print ('digite 10 números:') 
for i in range (0,10):
	vet.append(input(f'{i+1}º valor: '))
print ('Os números digitados do fim para o começo são:')
for j in range(0,10):
	print (f'{10-j}º:', vet[9-j])