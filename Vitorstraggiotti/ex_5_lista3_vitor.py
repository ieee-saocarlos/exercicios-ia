
tamanho = int(raw_input('Digite o tamanho do tabuleiro a ser montado: '))
primeira_linha = " --- "
outras_linhas = "|   |"
lista_primeira_linha = []
lista_outras_linhas = []

for i in range(tamanho):
    lista_primeira_linha.append(primeira_linha)
    lista_outras_linhas.append(outras_linhas)
i=0
print lista_primeira_linha
for i in range(tamanho - 1):
    print lista_outras_linhas
    print lista_primeira_linha
