jogo = [['X','O',''],
        ['O','X',''],
        ['O','X','X']]
a = 0

for i in range(0,3):
    if (jogo[i][0] == jogo[i][1]) and (jogo[i][1] == jogo[i][2]) and (jogo[i][0] == 'X' or jogo[i][0] == 'O'):
        if (jogo[i][0] == 'X'):
            print 'O jogador X ganhou!'
            a = 1
        else:
            print 'O jogador O ganhou!'
            a = 1

    elif (jogo[0][i] == jogo[1][i]) and (jogo[1][i] == jogo[2][i]) and (jogo[0][i] == 'X' or jogo[0][i] == 'O'):
        if (jogo[0][i] == 'X'):
            print 'O jogador X ganhou!'
            a = 1
        else:
            print 'O jogador O ganhou!'
            a = 1

if a == 0:
    if (jogo[0][0] == jogo [1][1]) and (jogo[1][1] == jogo[2][2]):
        if (jogo[0][0] == 'X'):
            print 'O jogador X ganhou!'
        else:
            print 'O jogador O ganhou!'
    elif (jogo[0][2] == jogo[1][1]) and (jogo[1][1] == jogo[2][0]):
        if (jogo[0][2] == 'X'):
            print 'O jogador X ganhou!'
        else:
            print 'O jogador O ganhou!'
    else:
        print 'O jogo deu velha, nao ha ganhadores!'
