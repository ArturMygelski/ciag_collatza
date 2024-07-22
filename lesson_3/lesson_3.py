import random

def papier_kamien_nozyce():

    lista_opcji = ["papier", "kamien", "nozyce"]
    print("witam w grze papier/kamien/nozyce!")
    print("wybierz opcje z dostapnych ponizej")
    print("1. papier")
    print("2. kamien")
    print("3. nozyce \n")

    # input('''
    # podaj wybrana opcje:
    # ''')
    while True:
        wybor_gracza = int(input("podaj wybrana opcje (1-3): "))
        # if wybor_gracza in [1, 2, 3]:
        if wybor_gracza < 1 or wybor_gracza > 3:
            print("niepoprawna opcja")
        else:
            break

    wybor_gracza_symbol = lista_opcji[wybor_gracza - 1]

    print(f"wybrałeś: {wybor_gracza_symbol}")

    wylosowana_liczba = random.randint(1, 3)
    wylosowana_liczba_symbol = lista_opcji[wylosowana_liczba - 1]
    print(f"komputer wybral: {wylosowana_liczba_symbol}")

    if wybor_gracza_symbol == wylosowana_liczba_symbol:
        print("remis")
    elif (wybor_gracza_symbol == "papier" and wylosowana_liczba_symbol == "kamien") or \
        (wybor_gracza_symbol == "kamien" and wylosowana_liczba_symbol == "nozyce") or \
        (wybor_gracza_symbol == "nozyce" and wylosowana_liczba_symbol == "papier"):
        print("Wygrałeś!")
    else:
        print("komputer Cie pobil")

papier_kamien_nozyce()

