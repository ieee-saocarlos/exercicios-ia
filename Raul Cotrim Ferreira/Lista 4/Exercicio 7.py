from random import *

set1 = set()
set2 = set()
set3 = set()

for i in range(randint(1,20)):
    set1.add(randint(1,100))

for i in range(randint(1,20)):
    set2.add(randint(1,100))


print set1
print set2

set3 = set1 | set2

print set3

set3 = set1 & set2

print set3

set3 = set1 ^ set2

print set3

max = 0
min = 100

for i in set1:
    if i > max:
        max = i

    if i < min:
        min = i

print 'O valor maximo do set 1 eh', max,', e o minimo eh', min

max = 0
min = 100

for i in set2:
    if i > max:
        max = i

    if i < min:
        min = i

print 'O valor maximo do set 2 eh', max,', e o minimo eh', min
