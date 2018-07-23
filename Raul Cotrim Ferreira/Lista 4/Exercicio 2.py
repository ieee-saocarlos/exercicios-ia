letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
letras_ma = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
'S', 'T', 'U', 'V', 'X', 'w', 'Y', 'Z']


string = raw_input("Digite a string: ")

n = len(string) + 1

while n > len(string):
    n = int(raw_input("Digite o numero de letras ficaram minusculas: "))

i = 0


while i < n:
    if string[i] in letras or string[i] in letras_ma:
        for j in range(len(letras)):
            if string[i] == letras_ma[j]:
                string = string.replace(string[i], letras[j], 1)

    else:
        n += 1
        if n > len(string):
            print 'O numero determinado de letras eh maior que o numero de letras na string'
            quit()

    i += 1


print string
