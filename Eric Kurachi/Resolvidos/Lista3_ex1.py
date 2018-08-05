#withdraw spaces from string
def nospace(phrase):
    return phrase.replace(" ", "")

#returns the reverse of a string
def invert(phrase):
    return phrase[::-1]

#tells if the phrase is palindrome
def ispalindrome(phrase):
    noSpace = nospace(phrase)
    if (noSpace == invert(noSpace)):
        return True
    else:
        return False

#main
phrase = raw_input("digite uma frase:")
ans = ispalindrome(phrase)

if (ans == 1):
    print 'Essa frase eh um palindromo'
else:
    print 'Essa frase n eh um palindromo'
