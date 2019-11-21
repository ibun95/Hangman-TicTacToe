print("************************************")
print("***                              ***")
print("***           TicTacToe          ***")
print("*** Player_1 [X] vs Player_2 [O] ***")
print("***                              ***")
print("************************************")

player_1 = input("Introduceti numele primului jucator:") or "Player_1"
player_2 = input("Introduceti numele jucatorului al doilea:") or "Player_2"

print("Buna " + player_1 + " si " + player_2)

print("     ---Incepe jocul!---")
print("Introduceti pozitia din tastatura \n"
      "numerica ca in figura de mai jos.")
print("      ___ ___ ___ \n"
      "     |_7_|_8_|_9_|\n"
      "     |_4_|_5_|_6_|\n"
      "     |_1_|_2_|_3_|\n")

values_t = ['1', '2', '3', '4',
            '5', '6', '7', '8', '9']
values = [-1 for x in range(9)]
values_s = ['_' for i in range(9)]

click = True
castigator = False
count = 0
pozitii_alese = []

def alege_pozitia(clk):
    '''
    Functie ce permite alegerea unei pozitii si verifica daca pozitia aleasa este permisa
    :param clk:
    :return:
    '''
    global pozitii_alese
    global values
    ales = False
    while ales == False:
        if clk == True:
            pozitie = input("Alege pozitia {0:<20s} [1-9]".format(player_1))
            if pozitie in values_t:
                if pozitie in pozitii_alese:
                    print("     Pozitie deja ocupata. Alegeti o pozitie libera")
                else:
                    pozitii_alese.append(pozitie)
                    values[int(pozitie)-1] = 1
                    ales = True
            else:
                print("Alegeti o cifra dintre: 1, 2, 3, 4, 5, 6, 7, 8, 9")
        elif clk == False:
            pozitie = input("Alege pozitia {0:<20s} [1-9]".format(player_2))
            if pozitie in values_t:
                if pozitie in pozitii_alese:
                    print("     Pozitie deja ocupata. Inceraca o pozitie libera.")
                else:
                    pozitii_alese.append(pozitie)
                    values[int(pozitie)-1] = 0
                    ales = True
            else:print("Alegeti o cifra dintre: 1, 2, 3, 4, 5, 6, 7, 8, 9")

    return pozitie

def print_tabel():
    '''
    Functie ce afiseaza la fiecare alegere tabela de joc
    :return:
    '''
    global pozitii_alese
    global values
    global values_s
    for i in range(9):
        if values[i] == 1:
            values_s[i] = 'X'
        elif values[i] == 0:
            values_s[i] = 'O'
        elif values[i] == -1:
            values_s[i] = '_'
        else:
            print('Valoare gresita')
    print('|_{0:<1s}_|_{1:<1s}_|_{2:<1s}_|'.format(values_s[6], values_s[7], values_s[8]))
    print('|_{0:<1s}_|_{1:<1s}_|_{2:<1s}_|'.format(values_s[3], values_s[4], values_s[5]))
    print('|_{0:<1s}_|_{1:<1s}_|_{2:<1s}_|'.format(values_s[0], values_s[1], values_s[2]))

def verificare(clk):
    '''
    Functie ce verifica daca exista un castigator.
    :param clk:
    :return:
    '''
    global values
    if ((values[0] == values[1] == values [2] == clk) or
        (values[3] == values[4] == values [5] == clk) or
        (values[6] == values[7] == values [8] == clk) or
        (values[0] == values[3] == values [6] == clk) or
        (values[1] == values[4] == values [7] == clk) or
        (values[2] == values[5] == values [6] == clk) or
        (values[0] == values[4] == values [8] == clk) or
        (values[2] == values[4] == values [6] == clk)):
        if clk == 1:
            player_w = player_1
        elif clk == 0:
            player_w = player_2
        print('Felicitari {0:<20s}, ai castigat!'.format(player_w))
        ans =  True
    else:
        ans =  False
    return ans

while ((count <= 8) and (castigator == False)):
    if click == True:
        poz = alege_pozitia(click)
        print_tabel()
        castigator = verificare(click)
        click = False
    elif click == False:
        poz = alege_pozitia(click)
        print_tabel()
        castigator = verificare(click)
        click = True
    if ((count == 8) and (castigator == False)):
        print('Este remiza!')
    count +=1



