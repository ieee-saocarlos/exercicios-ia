string = "thequickbrownfoxjumpsoverthelazydog"

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'x', 'w', 'y', 'z']



for i in letras:
    a = 0
    for j in string:
        if i == j:
            a += 1

    if a > 1:
        print 'A letra', i, 'eh repetida na string ', string
