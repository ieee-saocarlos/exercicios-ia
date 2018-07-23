a = ('x', 'i', 'f', 'v', 'y', 'i', 'o', 'P', '4', 8, '1', 99)
c = 0
b = raw_input("Digite o caracter ou numero a ser verificado se existe no tuple: ")


for i in a:
    i = str(i)
    if b == i:
        print 'O caracter', b,'esta contido no tuple'
        c = 1
        break

if c == 0:
    print 'O caracter', b,'nao esta contido no tuple'
