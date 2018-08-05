#wins completing a line
def horizontalWin(jogo):
	for i in range(0, 3):
		line = set(jogo[i])
		if (len(line) == 1):
			print (jogo[i][0] + ' ganhou')
			return 1

#wins completing a column
def verticalWin(jogo):
	for i in range(0, 3):
		column = []
		for j in range(0, 3):
			column.append(jogo[j][i])
		col = set(column)
		if (len(col) == 1):
			print (jogo[j][i] + ' ganhou')
			return 1

#wins by completing a diagonal
def diagonalWin(jogo):
	if(jogo[0][0] == jogo[1][1] == jogo[2][2]):
		print(jogo[1][1] + ' ganhou')
		return 1
	if(jogo[0][2] == jogo[1][1] == jogo[2][0]):
		print(jogo[1][1] + ' ganhou')
		return 1


jogo = [['X', 'O', ' '],
	    ['O', 'X', ' '],
	    ['O', 'X', 'X']]

#if no one wins then the game draws
if not(horizontalWin(jogo) or verticalWin(jogo) or diagonalWin(jogo) == 1):
	print 'Deu velha'
