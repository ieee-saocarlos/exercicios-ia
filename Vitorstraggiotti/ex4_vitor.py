

str1 = raw_input('digite uma string qualquer: ')
str2 = raw_input('digite uma segunda string: ')
print "a primeira string digitada foi: ", str1
print "a segunda string digitada foi: ", str2
comprimento1 = len(str1)
comprimento2 = len(str2)
print "\nA primeira string possue ", comprimento1, " digitos."
print "A segunda string possue ", comprimento2, " digitos."

if (comprimento1 != comprimento2):
    print "\nAs strings possuem tamanhos diferentes."
else:
    print "\nAs strings possuem tamanhos iguais"

if(comprimento1 == comprimento2):
    for i in range(comprimento2):
        if(str1[i] != str2[i]):
            print '\nAs strings sao diferentes'
            i = i - 1
            break
    if(comprimento2 - 1 == i):
        print '\nAs strings sao iguais'
else:
    print 'As strings sao diferentes'
n = input('aperte alguma tecla para sair: ')
