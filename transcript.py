cutDictionaryASCII = {}

cutCharacterASCII = ' !@#$%&\'()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯфабвгдежзийклмнопрстуфхцчшщъыьэюя'

stack = 32
for letter in cutCharacterASCII:
    if letter != 'A':
        cutDictionaryASCII[letter] = stack
        stack += 1
    else:
        cutDictionaryASCII[letter] = stack + 65
        stack += 66

operation = True
while operation != False:
    cipher = []
    terminalCipher = []

    character = input('Enter character set:\n')

    for letter in character:
        cipher.append(str(cutDictionaryASCII[letter]) + ' ')
        if letter != ' ':
            terminalCipher.append('[' + letter + ': ' + str(cutDictionaryASCII[letter]) + '] ')
        else:
            terminalCipher.append('[(space): ' + str(cutDictionaryASCII[letter]) + '] ')
            
    print('\n'.join(terminalCipher))
    print(''.join(cipher))
    print('Characters:', len(cipher))

    question = input('Continue? - ').lower()
    if question == 'no':
        operation = False
