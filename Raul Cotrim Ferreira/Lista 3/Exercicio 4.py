i = 0

while (i == 0):
    j1 = raw_input("\nDigite a jogada do primeiro jogador (pedra, papel ou tesoura):    ")
    j2 = raw_input("Digite a jogada do segundo jogador (pedra, papel ou tesoura):    ")
    j1 = j1.lower()
    j2 = j2.lower()
    print ""

    if (j1 == "pedra" and j2 == "pedra") or (j1 == "papel" and j2 == "papel") or (j1 == "tesoura" and j2 == "tesoura"):
        print 'A jogada deu empate!'

    else:
        if (j1 == "pedra" and j2 == "tesoura") or (j1 == "papel" and j2 == "pedra") or (j1 == "tesoura" and j2 == "papel"):
            print 'O jogador 1 ganhou!!\n'
            escolha = raw_input("Deseja jogar novamente?    ")
            escolha = escolha.lower()
            if escolha != "sim":
                i = 1

        elif (j2 == "pedra" and j1 == "tesoura") or (j2 == "papel" and j1 == "pedra") or (j2 == "tesoura" and j1 == "papel"):
            print 'O jogador 2 ganhou!!'
            escolha = raw_input("Deseja jogar novamente?    ")
            escolha = escolha.lower()
            if escolha != "sim":
                i = 1

        else:
            print 'As jogadas assinadas sao invalidas!!!'
