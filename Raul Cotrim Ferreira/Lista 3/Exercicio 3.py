from random import *

a_i = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b_i = []

for y in a_i:
    if(y % 2 == 0):
        b_i.append(y)


print 'Para a =', a_i
print 'b =', b_i

print ''

i = randint(0, 20)
a = []
b = []

for j in range(i):
    a.append(randint(0, 101))

print 'Para a =', a

for x in a:
    if (x % 2 == 0):
        b.append(x)

print 'b =', b
