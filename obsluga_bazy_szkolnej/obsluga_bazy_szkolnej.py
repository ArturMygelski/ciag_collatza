class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} z klasy {self.klasa}"


class Nauczyciel:
    def __init__(self, imie, nazwisko, prowadzony_przedmiot, prowadzona_klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.prowadzony_przedmiot = prowadzony_przedmiot
        self.prowadzona_klasa = prowadzona_klasa

    def __repr__(self):
        return f"Nauczyciel {self.imie} {self.nazwisko} prowadzi {self.prowadzony_przedmiot} w klasie {self.prowadzona_klasa}"


class Wychowawca:
    def __init__(self, imie, nazwisko, nazwa_prowadzonej_klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nazwa_prowadzonej_klasy = nazwa_prowadzonej_klasy

    def __repr__(self):
        return f"Wychowawca {self.imie} {self.nazwisko} prowadzi klasę {self.nazwa_prowadzonej_klasy}"


def wyszukaj_uczniow_po_klasie(klasa, lista_wszystkich_uczniow):
    lista_uczniow_klasy = []
    for uczen in lista_wszystkich_uczniow:
        if uczen.klasa == klasa:
            lista_uczniow_klasy.append(uczen)
    return lista_uczniow_klasy

def wyszukaj_ucznia_po_imieniu_i_nazwisku(imie, nazwisko, lista_wszystkich_uczniow):
    for uczen in lista_wszystkich_uczniow:
        if uczen.imie == imie and uczen.nazwisko == nazwisko:
            return uczen.klasa
    return None

def wyszukaj_wychowawce_po_imieniu_i_nazwisku(imie, nazwisko, lista_wszystkich_wychowawcow):
    for wychowawca in lista_wszystkich_wychowawcow:
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            return wychowawca
    return None

def wyszukaj_wychowawce_po_klasie(klasa, lista_wszystkich_wychowawcow):
    for wychowawca in lista_wszystkich_wychowawcow:
        if wychowawca.nazwa_prowadzonej_klasy == klasa:
            return wychowawca
    return None

def wyszukaj_nauczycieli_po_klasie(klasa, lista_wszystkich_nauczycieli):
    lista_nauczycieli = []
    for nauczyciel in lista_wszystkich_nauczycieli:
        if klasa == nauczyciel.prowadzona_klasa:
            lista_nauczycieli.append(nauczyciel)
    return lista_nauczycieli

def wyszukaj_nauczyciela_po_imieniu_i_nazwisku(imie, nazwisko, lista_wszystkich_nauczycieli):
    for nauczyciel in lista_wszystkich_nauczycieli:
        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
            return nauczyciel
    return None

szkola = {
    "uczniowie": [Uczen("Michal", "Zietkowski", "1 a"), Uczen("Marcin", "Nowak", "1 a"), Uczen("Artur", "Szpilka", "1 a"), Uczen("Artur", "Mygelski", "1 b"), Uczen("Katarzyna", "Mygelska","1 b")],
    "nauczyciele": [Nauczyciel("Anna", "Nowak", "biologia", "1 a"), Nauczyciel("Jacek", "Kowalski", "Matematyka", "1 b"), Nauczyciel(imie="Marian", nazwisko="Gąbka", prowadzony_przedmiot="Język Polski", prowadzona_klasa= "1 a")
    ],
    "wychowawcy": [Wychowawca("Anna", "Nowak", "1 b"), Wychowawca("Jacek", "Kowalski", "1 a")],
}

koniec_programu = False
print("Witaj w programie do obsługi bazy szkolnej SP 10!")
while not koniec_programu:
    wybor_uzytkownika = input("Podaj co chcesz zrobić. \n"
                              "1. Utwórz\n"
                              "2. Zarządzaj\n"
                              "3. Zakończ\n")
    if wybor_uzytkownika == "1":
        opcja_do_dodania = input("Co chcesz dodać?\n"
                                 "1. Uczen \n"
                                 "2. Nauczyciel \n"
                                 "3. Wychowawca \n"
                                 "4. Powrót \n")
        if opcja_do_dodania == "1":
            imie = input("Podaj imie ucznia: ")
            nazwisko = input("Podaj nazwisko ucznia: ")
            klasa = input("Podaj nazwę klasy ucznia: ")
            szkola.get("uczniowie").append(Uczen(imie, nazwisko, klasa))
        elif opcja_do_dodania == "2":
            imie = input("Podaj imie nauczyciela: ")
            nazwisko = input("Podaj nazwisko nauczyciela: ")
            prowadzony_przedmiot = input("Podaj nazwę prowadzonego przedmiotu: ")
            prowadzona_klasa = input("Podaj prowadzoną nazwę klasy: ")
            szkola.get("nauczyciele").append(Nauczyciel(imie, nazwisko, prowadzony_przedmiot, prowadzona_klasa))
        elif opcja_do_dodania == "3":
            imie = input("Podaj imie wychowawcy")
            nazwisko = input("Podaj nazwisko wychowawcy")
            nazwa_prowadzonej_klasy = input("Podaj nazwę prowadzonej klasy")
            szkola.get("wychowawcy").append(Wychowawca(imie, nazwisko, nazwa_prowadzonej_klasy))
        elif opcja_do_dodania == "3":
            continue
    elif wybor_uzytkownika == "2":
        opcja_do_wyboru = input("Co chcesz zrobić?\n"
                                "1. Klasa\n"
                                "2. Uczeń\n"
                                "3 .Nauczyciel\n"
                                "4. Wychowawca\n"
                                "5. Koniec\n")
        if opcja_do_wyboru == "1":
            klasa = input("Podaj nazwę klasy: ")
            wychowawca = wyszukaj_wychowawce_po_klasie(klasa, szkola.get("wychowawcy"))
            uczniowie = wyszukaj_uczniow_po_klasie(klasa, szkola.get("uczniowie"))
            if wychowawca:
                print(f"Wychowawca klasy {klasa}: {wychowawca}")
            else:
                print(f"Brak wychowawcy dla klasy {klasa}")
            if uczniowie:
                print(f"Uczniowie w klasie {klasa}: {', '.join(str(uczen) for uczen in uczniowie)}")
            else:
                print(f"Brak uczniów w klasie {klasa}")
        elif opcja_do_wyboru == "2":
            imie_ucznia= input("Podaj imie ucznia: ")
            nazwisko_ucznia = input("Podaj nazwisko ucznia: ")
            klasa = wyszukaj_ucznia_po_imieniu_i_nazwisku(imie_ucznia, nazwisko_ucznia, szkola.get("uczniowie"))
            uczen = wyszukaj_ucznia_po_imieniu_i_nazwisku(imie_ucznia, nazwisko_ucznia, szkola.get("uczniowie"))
            if uczen:
                nauczyciele = wyszukaj_nauczycieli_po_klasie(uczen.klasa, szkola.get("nauczyciele"))
                if nauczyciele:
                    print(f"Lekcje ucznia {uczen}: {', '.join(str(nauczyciel) for nauczyciel in nauczyciele)}")
                else:
                    print(f"Brak nauczycieli dla klasy {uczen.klasa}")
            else:
                print(f"Nie znaleziono ucznia {imie_ucznia} {nazwisko_ucznia}")
        elif opcja_do_wyboru == "3":
            imie_nauczyciela = input("Podaj imie nauczyciela: ")
            nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela: ")
            nauczyciel = wyszukaj_nauczyciela_po_imieniu_i_nazwisku(imie_nauczyciela, nazwisko_nauczyciela, szkola.get("nauczyciele"))
            if nauczyciel:
                print(
                    f"{nauczyciel}")
            else:
                print(f"Nie znaleziono nauczyciela {imie_nauczyciela} {nazwisko_nauczyciela}")
        elif opcja_do_wyboru == "4":
            imie_wychowawcy = input("Podaj imie wychowawcy: ")
            nazwisko_wychowawcy= input("Podaj nazwisko wychowawcy: ")
            wychowawca = wyszukaj_wychowawce_po_imieniu_i_nazwisku(imie_wychowawcy, nazwisko_wychowawcy, szkola.get("wychowawcy"))
            if wychowawca:
                print(wychowawca)
                uczniowie = wyszukaj_uczniow_po_klasie(wychowawca.nazwa_prowadzonej_klasy, szkola.get("uczniowie"))
                if uczniowie:
                    print(f"Uczniowie w klasie wychowawcy {wychowawca.imie} {wychowawca.nazwisko}: {', '.join(str(uczen) for uczen in uczniowie)}")
                else:
                    print(f"Brak uczniów w klasie {wychowawca.nazwa_prowadzonej_klasy}")
            else:
                print(f"Nie znaleziono wychowawcy {imie_wychowawcy} {nazwisko_wychowawcy}")
        elif opcja_do_wyboru == "5":
            continue
    elif wybor_uzytkownika == "3":
        koniec_programu = True
        print("Dziękujemy za skorzystanie z programu!")
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")