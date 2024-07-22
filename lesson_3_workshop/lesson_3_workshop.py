# Napisz program do organizacji przetrzymywania dokumentów w szafkach. Po uruchomieniu, aplikacja pyta, ile chcesz dodać dokumentów, a następnie wymaga podania liczby stron dla każdego z nich.
# Na koniec działania program powinien wyświetlić w podsumowaniu:
# 1. Liczbę dokumentów dodanych.
# 2. Łączną liczbę stron.
# 3. Suma niewykorzystanych miejsc w szafkach. Liczba szafek * 100 - łączna liczba stron.
# 4. Która szafka miała najwięcej niewykorzystanych miejsc, jaki to był wynik.
# Restrykcje:
# • Liczba stron dokumentów musi być z przedziału od 1 do 30 stron.
# • Każda szafka może maksymalnie pomieścić 100 stron.
# • W przypadku, jeżeli dodawany dokument przekroczy miejsce w szafce, ma zostać umieszczony w nowej szafce, a obecna zostaje zamknięta.
# • W przypadku podania liczby stron mniejszej od 1 lub większej od 30, dodawanie dokumentów zostaje zakończone i wszystkie szafki są zamknięte. Wyświetlane jest podsumowanie.
# Przykład 1:
#  Ilość dokumentów: 3
# • Liczba stron: 12, 45, 8
# Podsumowanie:
# • Dodano 1 dokument (12+45+8)
# • Łączna liczba stron: 12
# • Suma niewykorzystanych miejsc: 88
# • Najwięcej niewykorzystanych miejsc miała szafka 1 (88)
# Przykład 2:
# • Ilość dokumentów: 4
# • Liczba stron: 20, 30, 50, 25
# Podsumowanie:
# • Dodano 2 dokumenty (20+30+50, 25)
# • Łączna liczba stron: 125
# • Suma niewykorzystanych miejsc: 75
# • Najwięcej niewykorzystanych miejsc miała szafka 2 (75)
# Przykład 3:
# • Ilość dokumentów: 3
# • Liczba stron: 25, 40, 35
# Podsumowanie:
# • Dodano 2 dokumenty (25+40, 35)
# • Łączna liczba stron: 100
# • Suma niewykorzystanych miejsc: 100
# • Najwięcej niewykorzystanych miejsc miała szafka 2 (65)


#dane wejsciowe
#ilosc dokumentow - pierwszy input uzytkownika
#ilosc stron - uzaleznic od ilosci dokumentow (petla for)

print("witaj w naszej sortowni dokumentow")
ilosc_dokumentow = int(input("podaj prosze ile dokumentow chcesz posegregowac - podaj wartosc liczbowa "))
suma_stron = 0
ilosc_szafek = 1
pojemnosc_szafki = 100
pojemnosc_obecnej_szafki = 0
maksymalne_wolne_miejsce = 0
numer_szafki_z_max_pustym_miejscem = 1
ilosc_dodanych_dokumentow = 0
for dokument in range(ilosc_dokumentow):
    ilosc_stron = int(input("podaj ilosc stron dokumentu: "))
    if 1<= ilosc_stron <= 30:
        suma_stron += ilosc_stron
        if ilosc_stron + pojemnosc_obecnej_szafki > pojemnosc_szafki:
            if pojemnosc_szafki - pojemnosc_obecnej_szafki > maksymalne_wolne_miejsce:
                maksymalne_wolne_miejsce = pojemnosc_szafki - pojemnosc_obecnej_szafki
                numer_szafki_z_max_pustym_miejscem = ilosc_szafek
            ilosc_szafek += 1
            pojemnosc_obecnej_szafki = ilosc_stron
        else:
            pojemnosc_obecnej_szafki += ilosc_stron
    else:
        print("ilosc stron nie miesci sie w zakresie referencyjnym 1-30")
if pojemnosc_szafki - pojemnosc_obecnej_szafki > maksymalne_wolne_miejsce:
    maksymalne_wolne_miejsce = pojemnosc_szafki - pojemnosc_obecnej_szafki
    numer_szafki_z_max_pustym_miejscem = ilosc_szafek

print(f"ilosc dodanych dokumentow to: {ilosc_dodanych_dokumentow}")
print(f"ilosc dodanych dokumentow to {ilosc_dokumentow} ")
print(f"suma stron dokumentow to {suma_stron}")
print(f"suma szafek to: {ilosc_szafek}")
print(f"suma wolnych miejsc w szafkach to: {ilosc_szafek * pojemnosc_szafki - suma_stron}")
print(f"najwiecej wolnego miejsca w szafce: {maksymalne_wolne_miejsce}, nr szafki: {numer_szafki_z_max_pustym_miejscem}")



# while True:
#     wybor_gracza = int(input("podaj wybrana opcje (1-3): "))
#     # if wybor_gracza in [1, 2, 3]:
#     if wybor_gracza < 1 or wybor_gracza > 3:
#         print("niepoprawna opcja")
#     else:
#         break