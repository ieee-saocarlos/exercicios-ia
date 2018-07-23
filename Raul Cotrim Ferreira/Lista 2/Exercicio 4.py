def comprimento():
    if (len(string1) == len(string2)):
        print 'As strings tem o mesmo tamanho'
    else:
        print 'As strings nao tem o mesmo tamanho'

def conteudo():
    if (string1 == string2):
        print 'As strings sao iguais em conteudo'
    else:
        print 'As strings sao diferentes em conteudo'


string1 = raw_input('Digite a string a ser comparada: ')
print 'A string digitada tem tamanho ', len(string1),'e conteudo', string1
print ''
string2 = raw_input('Digite a outra string a ser comparada: ')
print 'A string digitada tem tamanho ', len(string2),'e conteudo', string2
print ''
comprimento()
conteudo()
