a = (1,2,3,4,5)

n = int(raw_input("Digite o numero a ser adicionado no tuple (1,2,3,4,5): "))

a = list(a)
a.append(n)
a = tuple(a)

print a
