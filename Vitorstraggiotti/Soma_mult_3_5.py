

total_1 = 0
total_2 = 0
for i in range(1, 1000):
    if (i % 3) == 0:
        total_1 += i
    if (i % 5) == 0:
        total_2 += i
total_3 = total_1 + total_2
print("A soma de todos os multiplos de 3 ou 5 menores que 1000 e: ")
print(total_3)
