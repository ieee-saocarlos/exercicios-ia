def conversaoH(h):
    if (h > 12):
        return h - 12
    else:
        return h

def impressao(a):
    if (a > 12):
        return 'PM'
    else:
        return'AM'

def erro():
    print ''
    print 'Valor incopativel!'
    print ''

p = 1
while (p != 0):
        horas = input('Digite o valor das horas: ')
        if (horas >= 0) and (horas <= 24):
            minutos = input('Digite o valor dos minutos: ')
            if(minutos >= 0) and (minutos < 60):
                print ''
                print 'A hora registrada no formato de 24H eh: ', horas,':', minutos
                a = horas
                horas = conversaoH(horas)
                print 'A hora registrada no formato de 12H eh: ', horas,':', minutos, impressao(a)
                print ''
            else:
                erro()
        else:
            erro()
