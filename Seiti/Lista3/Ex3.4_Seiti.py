import random

valido = 1
while (valido):
	tipo = input("Digite (1) para jogar contra um computador ou digite (2) para 2 jogadores: ")
	
	if ((tipo != 1) and (tipo != 2)):
		print "ERRO"
		exit()
	
	str1 = raw_input("Jogador 1 - digite pedra, papel ou tesoura: ")
	if (str1 == "pedra"):
		j1 = 1
	elif (str1 == "papel"):
		j1 = 2
	elif (str1 == "tesoura"):
		j1 = 3	
	else:
		print "jogada invalida"
		break

	if (tipo == 1):
		comp = random.randrange(1,3)
		if (j1 == 1):
			if (comp == 1):
				print "Empate" 
			elif (comp == 2):
				print "Vitoria do computador!"
			else:
				print "Vitoria para o jogador!"
		elif (j1 == 2):
			if (comp == 2):
				print "Empate" 
			elif (comp == 3):
				print "Vitoria do computador!"
			else:
				print "Vitoria para o jogador!"
		elif (j1 == 3):
			if (comp == 3):
				print "Empate" 
			elif (comp == 1):
				print "Vitoria do computador!"
			else:
				print "Vitoria para o jogador!"
			
	if (tipo == 2):
		str2 = raw_input("Jogador 2 - digite pedra, papel ou tesoura: ")
		if (str2 == "pedra"):
			j2 = 1
		elif (str2 == "papel"):
			j2 = 2
		elif (str2 == "tesoura"):
			j2 = 3
		else:
			print "jogada invalida"
			break
				
		if (j1 == 1):
			if (j2 == 1):
				print "Empate" 
			elif (j2 == 2):
				print "Vitoria do jogador 2!"
			else:
				print "Vitoria para o jogador 1!"
		elif (j1 == 2):
			if (j2 == 2):
				print "Empate" 
			elif (j2 == 3):
				print "Vitoria do jogador 2!"
			else:
				print "Vitoria para o jogador 1!"
		elif (j1 == 3):
			if (j2 == 3):
				print "Empate" 
			elif (j2 == 1):
				print "Vitoria do jogador 2!"
			else:
				print "Vitoria para o jogador 1!"
		
	valido = raw_input("Deseja jogar novamente? (s/n): ")
	if (valido == "s"):
		valido = 1
	else:
		exit()