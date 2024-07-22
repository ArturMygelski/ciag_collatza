import random
tablica = [[1,2,3],[4,"X",6],[7,8,9]]
tablica_winning_options = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[8,5,2],[9,6,3],[1,5,9],[3,5,7]]
tablica_wyboru_gracza = []
tablica_wyboru_komputera = [5]
def tabliczka():
    for tabliczka in tablica:
        print(tabliczka)
print(tabliczka())
print("ruch gracza: wybierz pole: ")
ruch_gracza = int(input())
def ruch(zawodnik, ruch):
    znak = "O" if zawodnik else "X"
    if ruch <=3:
       tablica[0][ruch-1] = znak
    elif 3< ruch < 7:
        tablica[1][ruch-4] = znak
    else:
        tablica[2][ruch-7] = znak
    tablica_wyboru_gracza.append(ruch) if znak == "O" else tablica_wyboru_komputera.append(ruch)
print(tabliczka())
ruch(True, ruch_gracza)
print(tabliczka())
def komputer_pierwszy(ruch_przeciwnika):
    unikalna_wartosc = False
    while not unikalna_wartosc:
        wybrana_wartosc = random.choice([1, 3, 7, 9])
        if wybrana_wartosc != ruch_przeciwnika:
            unikalna_wartosc = True
            break
    return wybrana_wartosc
ruch_komputera = komputer_pierwszy(ruch_gracza)
ruch(False, ruch_komputera)
print(tabliczka())
print("ruch gracza: wybierz pole: ")
ruch_gracza = int(input())
print(tabliczka())
ruch(True, ruch_gracza)
print(tabliczka())
def komputer_drugi():
    for winning_options in tablica_winning_options:
        wspolna_lista = []
        wspolna_lista_gracza = []
        rozne_elementy = []
        for element in winning_options:
            if element in tablica_wyboru_komputera:
                wspolna_lista.append(element)
            elif element in tablica_wyboru_gracza:
                wspolna_lista_gracza.append(element)
            else:
                rozne_elementy.append(element)

        if len(wspolna_lista) == 2 and len(wspolna_lista_gracza) == 0:
            return rozne_elementy[0]
ruch_komputera = komputer_drugi()
ruch(False, ruch_komputera)
print(tabliczka())





