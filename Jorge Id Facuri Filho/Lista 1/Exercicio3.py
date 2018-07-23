Soma1 = 0
Soma2 = 0

for x in range(101):
    Soma1 = x**2 + Soma1
    Soma2 = x + Soma2
print(Soma1 - Soma2**2)
