str1 = raw_input("Digite uma string: ")
str2 = raw_input("Digite outra string: ")

print 	"O conteudo da string 1 e: " + repr(str1) + " sua quantidade de caracteres e: ", len(str1) 
print 	"O conteudo da string 2 e: " + repr(str2) + " sua quantidade de caracteres e: ", len(str2) 
if (len(str1)==len(str2)):
	print "as strings tem a mesma quantidade de caracteres."
	if(str1==str2):
		print "As strings tem o mesmo conteudo."
	else:
		print "As strings tem conteudo diferente."
	exit()
else:
	print "As strings sao diferentes no tamanho e conteudo."
	exit()