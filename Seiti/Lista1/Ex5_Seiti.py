x, y, aux = 1, 0, 0
soma = 0

while x < 4000000:
  if (x%2 != 0):
    soma += x
  aux = x  
  x += y
  y = aux
print "A soma é:", soma