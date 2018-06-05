string = raw_input("Digite a string a ser verificada: ")
string = string.replace(" ", "")
oposto = string[::-1]

if string == oposto:
    print 'A string eh um palindromo'
else:
    print 'A string nao eh um palindromo'
