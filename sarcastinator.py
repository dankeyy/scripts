""" a fUnCtIoN To pRiNt yOuR SeNtEnCe iN A SaRcAsTiC FoRm """

def sarcastinator(sentence): 
    uol = (str.lower, str.upper) # upper or lower
    return ''.join( uol[i % 2](letter) for i, letter in enumerate(sentence) )


if __name__ == '__main__':
    #sentence = 'this is not a sarcastic sentence'
    sentence = input('Enter a sentence:\n> ')
    print(sarcastinator(sentence))