
soma_1 = 0
soma_2 = 0
for i in range(1,101):
    soma_1 += (i ** 2)
    soma_2 += i
resultado = soma_1 - (soma_2 ** 2)
print("  A diferenca entre a soma dos quadrados e o quadrado da soma\n dos 100 primeiros naturais e: ")
print(resultado)
