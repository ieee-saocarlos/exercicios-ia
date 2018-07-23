a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in range(0,len(b)):
    for j in range(0, len(a)):
        if a[j] == b[i]:
            c.append(a[j])

j = 0
i = 0

tam = len(c) - 1

for i in range(0, tam):
    for j in range(0, tam):
        if (c[i] == c[j]) and (i != j):
            del(c[i])


print c
