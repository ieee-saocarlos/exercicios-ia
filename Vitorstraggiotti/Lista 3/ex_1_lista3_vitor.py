print "Este programa ira mostrar se uma palavra e um palindromo"
palavra = input("digite uma palavra entre aspas: ")
palavra_invertida = palavra[::-1]

if(palavra_invertida == palavra):
    print "\n\nA palavra digitada e um palindromo"
else:
    print "\n\nA palavra digitada nao e um palindromo"
