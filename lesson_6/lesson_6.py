lista_uczniow = [
    {
        "imie": "Michal",
        "nazwisko": "Zietkowski",
        "klasa": "1a",
        "zachowanie": "poprawne"
    },
    {
        "imie": "Adam",
        "nazwisko": "Nowak",
        "klasa": "2a",
        "zachowanie": "poprawne"
    }
]


def popros_uzytkownika_o_dane_ucznia():
    imie = input("Podaj imię ucznia")
    nazwisko = input("Podaj nazwisko ucznia")
    klasa = input("Podaj klasę ucznia")
    return imie, nazwisko, klasa


def wyszukaj_ucznia_w_szkole(imie, nazwisko, klasa):
    for uczen in lista_uczniow:
        if uczen.get("imie") == imie and uczen.get("nazwisko") == nazwisko and uczen.get("klasa") == klasa:
            print(uczen)
            return True
    return False


print("Witaj w programie nasza szkoła")
operacja = input("Podaj co chcesz zrobić.\n1. Dodaj ucznia\n2. Wyszukaj ucznia")
if operacja == "1":
    imie, nazwisko, klasa = popros_uzytkownika_o_dane_ucznia()
    znaleziono_ucznia = wyszukaj_ucznia_w_szkole(imie, nazwisko, klasa)
    if not znaleziono_ucznia:
        lista_uczniow.append({
            "imie": imie,
            "nazwisko": nazwisko,
            "klasa": klasa
        })
    else:
        print("Taki uczen istnieje juz w twoim systemie.")
elif operacja == "2":
    imie, nazwisko, klasa = popros_uzytkownika_o_dane_ucznia()
    znaleziono_ucznia = wyszukaj_ucznia_w_szkole(imie, nazwisko, klasa)
    if not znaleziono_ucznia:
        print("Nie mamy takiego ucznia w naszym systemie.")

# def dodanie_dwoch_liczb(pierwsza_liczba, druga_liczba=15):
#     print(f"pierwsza liczba to: {pierwsza_liczba}, druga liczba to {druga_liczba}")
#     print(pierwsza_liczba + druga_liczba)
#
#
# def pierwsza_liczba_wieksza_od_drugiej(pierwsza_liczba, druga_liczba):
#     if pierwsza_liczba > druga_liczba:
#         return True  # jednoznacze z break i zwroc do zmiennej wartosc True
#     return False
#
#
# dodanie_dwoch_liczb(20, 17)
# dodanie_dwoch_liczb(20)
# # dodanie_dwoch_liczb(druga_liczba=20, pierwsza_liczba=12)
# # dodanie_dwoch_liczb(20, 12)
# # dodanie_dwoch_liczb(20, 111)
# # dodanie_dwoch_liczb(20, 10)
# wynik = pierwsza_liczba_wieksza_od_drugiej(20, 15)
# print(wynik)

auto = {
    "marka": "Fiat",
    "model": "Bravo",
    "rok": 2003,
    "kolor": "czerwony",
    "silnik": "100hp",
    "ilosc_paliwa": 10,
    "pojemnosc_baku": 50
}
# print(auto.get("marka"))
# print(auto["marka"])

auto["ilosc_paliwa"] = 30

class Auto:
    def __init__(self, marka_auta, model_auta, rok_auta, kolor_auta, moc_silnika, ilosc_paliwa_pojazdu, pojemnosc):
        self.marka = marka_auta
        self.model = model_auta
        self.rok = rok_auta
        self.kolor = kolor_auta
        self.moc = moc_silnika
        self.ilosc_paliwa = ilosc_paliwa_pojazdu
        self.pojemnosc_baku = pojemnosc
        print("hura zbudowales auto")

    def uzupelnij_bak_paliwa(self, ilosc_paliwa_wlanego):
        if self.ilosc_paliwa + ilosc_paliwa_wlanego > self.pojemnosc_baku:
            print("Nie mozesz zatankowac az takiej ilosci")
        else:
            self.ilosc_paliwa += ilosc_paliwa_wlanego

    def __repr__(self):
        return f"Auto marki: {self.marka} model: {self.model} rok: {self.rok}"


fiat_bravo = Auto(
    marka_auta="fiat",
    model_auta="bravo",
    rok_auta=2003,
    kolor_auta="czerwony",
    moc_silnika="100hp",
    ilosc_paliwa_pojazdu=10,
    pojemnosc=50
)

mercedes_glc = Auto(
    marka_auta="Mercedes",
    model_auta="GLC",
    rok_auta=2024,
    kolor_auta="czarny",
    moc_silnika="300hp",
    ilosc_paliwa_pojazdu=20,
    pojemnosc=60
)

print(fiat_bravo.model)
print(mercedes_glc.ilosc_paliwa)
fiat_bravo.uzupelnij_bak_paliwa(ilosc_paliwa_wlanego=38)
mercedes_glc.uzupelnij_bak_paliwa(ilosc_paliwa_wlanego=100)
print(fiat_bravo.ilosc_paliwa)
print(mercedes_glc.ilosc_paliwa)
print(fiat_bravo)
print(mercedes_glc)