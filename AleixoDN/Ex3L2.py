def conversao(horas):
    horas[1] = 'A'
    if horas[0] > 12:
        horas[1] = 'P'
        horas[0] = horas[0] - 12
    elif horas[0] == 12:
        horas[1] = 'P'
    return horas

def saida(horas, minutos):
    print "\n", horas[0], minutos, horas[1], "M"

#Inicio da rotina principal
print "\n  -------------------------\n  --Exercicio 3 - Lista 2--\n  -------------------------\n" #Titulo

horas = [0, 0]
fim = 'N'
while (fim == 'N'):
    print "\nInsira o horario a ser convertido..."
    horas[0] = int(raw_input("Horas: "))
    minutos = int(raw_input("Minutos: "))
    if minutos > 59 or horas[0] > 24:
        print "Valores incorretos!"
        break
    horas = conversao(horas)
    saida(horas, minutos)
    fim = 'X'
    while (fim != 'N' and fim !='S'):
        fim = raw_input("\nEncerrar[S][N]?")
