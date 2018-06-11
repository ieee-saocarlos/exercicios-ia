
print 'JOGADOR 1\n\n Escolha o numero referente a jogada:\n\n  [1]- PEDRA\n  [2]- PAPEL\n  [3]- TESOURA'
jogada_1 = int(raw_input())

print 'JOGADOR 2\n\n Escolha o numero referente a jogada:\n\n  [1]- PEDRA\n  [2]- PAPEL\n  [3]- TESOURA'
jogada_2 = int(raw_input())

if(jogada_1 == jogada_2):
    print '\n\n    EMPATE !!!'

if((jogada_1 == 1) & (jogada_2 == 2)):
    print '\n\n    JOGADOR 2 VENCEU !!!'
if((jogada_1 == 1) & (jogada_2 == 3)):
    print '\n\n    JOGADOR 1 VENCEU !!!'
if((jogada_1 == 2) & (jogada_2 == 1)):
    print '\n\n    JOGADOR 1 VENCEU !!!'
if((jogada_1 == 2) & (jogada_2 == 3)):
    print '\n\n    JOGADOR 2 VENCEU !!!'
if((jogada_1 == 3) & (jogada_2 == 1)):
    print '\n\n    JOGADOR 2 VENCEU !!!'
if((jogada_1 == 3) & (jogada_2 == 2)):
    print '\n\n    JOGADOR 1 VENCEU !!!'
