# caesarplus Encrypt Module
# Owner: awesomelewis2007
# Co-Owner: WolfieBoy

def caesar_encrypt(word,shift):
    caesar = ''
    for i in word:
        if (i == ' '):
            caesar += ' '
        else:
            caesar += (chr(ord(i) + shift))
    return caesar
