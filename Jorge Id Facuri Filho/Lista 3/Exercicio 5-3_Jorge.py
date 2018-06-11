n = input("COLOQUE O VALOR PARA O TAMANHO DO TABULEIRO N X N: ")
quant = n * n



for x in range(0,n):
    print (" ----- "*(n))
    print ("|      "*(n + 1))
print(" ----- "*(n))

print("A QUANTIDADE DE QUADRADINHOS EH: ", quant)
