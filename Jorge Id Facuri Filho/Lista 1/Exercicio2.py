soma = 0
for x in range (1001):
    if(x % 3 == 0 or x % 5 == 0):
        soma = soma + x
print(soma)
