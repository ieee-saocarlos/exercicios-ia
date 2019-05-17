print "\n  -------------------------\n  --Exercicio 4 - Lista 2--\n  -------------------------\n" #Titulo

def getstr(): #Funcao que pede as palavras
    text = [] #Lista para almazenar as palavras
    text.append(raw_input('Insira a primeira palavra: ')) #Armazena a primeira palavra
    text.append(raw_input('Insira a segunda palavra: ')) #Armazena a segunda palavra
    return text

def test_iqual(text): #Informa os conteudos e verifica se as palavras sao iguais
    print "\n\n"
    print "Primeira palavra: ", text[0] #Primeira palavra
    print "Segunda palavra: ", text[1] #Segunda palavra
    if text[0] == text[1]: #Para o caso de ser iguais...
        print "\nAs palavras sao iguais!" #...isso eh informado
    print "\n\n"

def n_letters(arg): #Informa o numero de letras de cada palavra e verifica se sao iguais
    print "A primeira palavra tem", len(text[0]), "letras" #Primeira palavra
    print "A segunda palavra tem", len(text[1]), "letras" #Segunda palavra
    if len(text[0]) == len(text[1]):
        print "\nAs palavras tem o mesmo numero de letras!"
    print "\n\n"

#Inicio da rotina principal
text = getstr() #Adquire as palavras
test_iqual(text) #Informa os seus contedos e testa se sao iguais
n_letters(text) #Informa o numero de letras de cada palavra e testa de sao iguais
