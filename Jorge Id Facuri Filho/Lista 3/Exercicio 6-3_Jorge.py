import random

def PrimeiroPai(pai):
    for i in range(0,8):
        a = random.choice([1,2,3,4,5,6,7,8])
        pai.append(a)
    return pai


def PrimeiraMae(mae):
    for i in range(0,8):
        b = random.choice([1,2,3,4,5,6,7,8])
        mae.append(b)
    return mae


pai1 = []
mae1 = []
a = pai1
b = mae1


print PrimeiraMae(mae1)
print PrimeiroPai(pai1)
