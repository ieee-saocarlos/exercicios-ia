
def transf_horas(h):
    if(h > 12):
        h1 = h - 12
    return h1
def impressao(a):
    if(a > 12):
        return 'P'
    else:
        return 'A'

while(1):
    horas = input('Digite as horas: ')
    min = input('Digite os minutos: ')
    if(min > 0) and (min < 60):
        if(horas > 0) and (horas < 24):
            print 'O horario no formato 24h eh:', horas, ':', min, '\n\n'
            print 'O horario no formato 12h eh:', transf_horas(horas), ':', min, impressao(horas), '\n\n'
        else:
            print('Erro no formato de hora inserido. tente novamente')
    else:
        print('Erro no formato de hora inserido. tente novamente')
