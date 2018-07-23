str = raw_input("Digite uma string sem caracteres especiais: ")
strcolada = str.replace(' ', '')
strmin = strcolada.lower()
str2 = strmin[::-1]
if str2 == strmin:
	print "A string e palindromo"
else:
	print "A string nao e um palindromo"
exit()