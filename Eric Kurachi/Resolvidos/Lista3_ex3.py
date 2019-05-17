from random import *

#creates a random list
def createList():
    list = []
    r = randint(2, 10)
    for i in range (1, r):
        j = randint(0, 100)
        list.append(j)
    list.sort()
    return list


#returns a list with the even numbers
def evenNumbers(list):
    even = []
    for i in list:
        if (i % 2 == 0):
            even.append(i)
    return even

#main
list = createList()
print lists
b = evenNumbers(list)
b = set(b)
print b
