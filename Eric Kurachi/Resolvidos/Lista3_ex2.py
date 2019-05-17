#Returns a list with the common elements of two lists
def commonElements(p, q):
    print p
    P = set(p)
    print P
    Q = set(q)
    R = list(P.intersection(Q))
    return R

#main
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13]
c = commonElements(a, b)

print c
