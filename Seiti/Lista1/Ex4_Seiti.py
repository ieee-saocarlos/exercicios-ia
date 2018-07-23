x = 600851475143
primo = 2
y = x
while (primo < x):
  while (x%primo == 0):
    x = x/primo
  primo += 1
print (f"O maior primo de {y} é: {primo}.")
