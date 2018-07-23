tamanho = input("Digite o numero inteiro que determinara o tamanho da tabela a ser criada (Ex. numero = N => N x N):")
linha_espaco = ''
linha_traco = ''

for i in range(tamanho):
    print (' ---' * tamanho)
    print ('|   ' * (tamanho + 1))
print (' ---' * tamanho)
