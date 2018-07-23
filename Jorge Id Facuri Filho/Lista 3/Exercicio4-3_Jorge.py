print"BEM VINDO AO JOGO"
print""
print"----------------REGRAS---------------"
print""
print"PAPEL = 1     /_/ "
print"PEDRA = 2      O  "
print"TESOURA = 3    BX "
print"-------------------------------------"
print""
print"***FACAM A JOGADA,JOGADORES***"
n = 1
print "JOGADOR 1: "
n1 = input()
print"JOGADOR 2: "
n2 = input()

def empate():
    if(n1 == n2):
      print"*EMPATE*"

def winJ1():
    if(n1 == 1 and n2 == 2) or (n1 == 2 and n2 == 3) or (n1 == 3 and n2 == 1):
        print"O JOGADOR 1 GANHOU"

def winJ2():
    if(n2 == 1 and n1 == 2) or (n2 == 2 and n1 == 3) or (n2 == 3 and n1 == 1):
        print"O JOGADOR 2 GANHOU"

#--------------------------------------------------------------------#

while(n == 1):
 if((n1 == 1 or n1 == 2 or n1 == 3) and (n2 == 1 or n2 == 2 or n2 == 3)):
    empate()
    winJ1()
    winJ2()

    print""
    n = input('''ESCOLHA SE QUER CONTINUAR

    [1] CONTINUAR
    [2] PARAR''')
    if(n == 1):
     print"FACA AS JOGADAS"
     n1 = input()
     n2 = input()
    else:
     break
 else:
    print("DIGITE CERTOOOOOOOO")
    print""
    print"FACA AS JOGADAS: "
    print"JOGADOR 1"
    n1 = input()
    print"JOGADOR 2"
    n2 = input()


print"O JOGO ACABOU"
