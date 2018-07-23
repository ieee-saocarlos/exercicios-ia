num = 600851475143
raiz = num ** 0.5
raiz = int(raiz)
primo = 2
for i in range(3,raiz):
    while(num % i) == 0:
        if i > primo:
            primo = i
        num = num/i
print("O maior fator primo eh:", primo)
