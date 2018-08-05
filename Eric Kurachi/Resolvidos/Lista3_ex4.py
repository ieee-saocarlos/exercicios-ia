while(quit != 'n'):
    print 'Vamos jogar pedra, papel ou tesoura!'
    J1 = int(raw_input("Jogador 1: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura\n"))
    J2 = int(raw_input("Jogador 2: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura\n"))

    if(J1 == J2):
        print 'O jogo empatou. Tentar novamente? (s/n)'
    elif((J1 == 1 and J2 == 2) or (J1 == 2 and J2 == 3) or (J1 == 3 and J2 == 1)):
        print 'O jogador 2 venceu! Jogar novamente? (s/n)'
    else:
        print 'O jogador 1 venceu! Jogar novamente? (s/n)'

    while(quit != 's' and quit != 'n'):
        quit = raw_input()
        if(quit != 's' and quit != 'n'):
            print 'Erro! Digite "s" para sim e "n" para nao \n Jogar novamente?'
