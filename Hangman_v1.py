print("************************************")
print("***                              ***")
print("***           Hangman            ***")
print("***                              ***")
print("************************************")

import random
from string import ascii_uppercase

name = input("Introduceti numele jucatorului:") or ('Player')
word_list = ["ROMANIA", "SPANIA", "ITALIA", " CROATIA", "AUSTRIA", "PORTUGALIA", "FRANTA", "AFGANISTAN", "BULGARIA"]

the_word = random.choice(word_list)
the_word_withSpaces = " ".join(the_word)

print("     ---Incepe jocul!---")
litere_ghicite = []

print("Cuvantul este:"+ "__ " * len(the_word))
count = 0
castigator = False
word = ['_' for i in list(the_word) if i.isalpha]

def img(cnt):
    if cnt == 1:
        print(' \n'
              '  |       \n'
              '  |       \n'
              '  |       \n'
              '  |       \n'
              '  |       \n'
              '  |       \n'
              '  |       \n'
              '__|______________ \n')
    elif cnt == 2:
        print('  __________\n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '__|______________ \n')
    elif cnt == 3:
        print('  __________\n'
              '  |         |\n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '__|______________ \n')
    elif cnt == 4:
        print('  __________\n'
              '  |         |\n'
              '  |        ( )\n'
              '  |         |\n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '  |        \n'
              '__|______________ \n')
    elif cnt == 5:
        print('  __________\n'
              '  |         |\n'
              '  |        ( )\n'
              '  |         |\n'
              '  |         | \n'
              '  |         |  \n'
              '  |         \n'
              '  |        \n'
              '__|______________ \n')
    elif cnt == 6:
        print('  __________\n'
              '  |         |\n'
              '  |        ( )\n'
              '  |         |\n'
              '  |        /| \n'
              '  |       / | \n'
              '  |          \n'
              '  |        \n'
              '__|______________ \n')
    elif cnt == 7:
        print('  __________\n'
              '  |         |\n'
              '  |        ( )\n'
              '  |         |\n'
              '  |        /|\ \n'
              '  |       / | \ \n'
              '  |           \n'
              '  |          \n'
              '__|______________ \n')
    elif cnt == 8:
        print('  __________\n'
              '  |         |\n'
              '  |        ( )\n'
              '  |         |\n'
              '  |        /|\ \n'
              '  |       / | \ \n'
              '  |        /   \n'
              '  |       /    \n'
              '__|______________ \n')
    elif cnt == 9:
        print('  __________\n'
              '  |         |\n'
              '  |        ( )\n'
              '  |         |\n'
              '  |        /|\ \n'
              '  |       / | \ \n'
              '  |        / \  \n'
              '  |       /   \ \n'
              '__|______________ \n')

while((count < 9) and (castigator == False)):
    guess = input("Introduceti o litera") or ('1')
    if guess.upper() in ascii_uppercase:
        if guess.upper() in litere_ghicite:
            print("Litera a fost deja aleasa! Alegeti o alta litera in afara de:" + str(litere_ghicite))
        else:
            litere_ghicite.append(guess.upper())
            if guess.upper() in list(the_word):
                i = 0
                for letter in list(the_word):
                    if guess.upper() == letter:
                        word[i] = guess.upper()
                    i += 1
                print(" ".join(word))
            else:
                count += 1
                img(count)
                print(" ".join(word))
        if "".join(word) == the_word:
            castigator = True
            print('Felicitari {0:s}! Ai gasit cuvantul!'.format(name))
    else:
        print("Caracterul ales nu exista! Alegeti alt caracter.")
    if count == 9:
        print('Ai pierdut! Cuvantul era: {0:s}'.format(the_word))
