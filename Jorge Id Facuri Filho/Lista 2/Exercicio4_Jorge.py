l1 = raw_input("COLOQUE O VALOR DA PRIMEIRA STRING: ")
l2 = raw_input("COLOQUE O VALOR DA SEGUNDA STRING: ")

print(" EM RELAÇÃO A PRIMEIRA STRING:\n")
print "---> TAMANHO:",len(l1)
print "---> CONTEÚDO:",l1

print "-------------------------------------"
print(" EM RELAÇÃO A SEGUNDA STRING:\n")
print "---> TAMANHO:",len(l2)
print "---> CONTEÚDO:",l2

print"--------------------------------------"

print"*REALIZANDO AS COMPARAÇÕES*"

if(len(l1) == len(l2)):
  print"AS STRINGS POSSUEM O MESMO TAMANHO"
else:
  print"AS STRINGS POSSUEM TAMANHOS DIFERENTES"

if(l1 == l2):
  print"*AS STRINGS SÃO IGUAIS"
else:
  print"*AS STRINGS SÃO DIFERENTES"
