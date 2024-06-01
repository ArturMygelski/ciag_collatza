print("witaj w moim skromnym ciągu Collatza")
def ciag_collatza(x):
    dlugosc = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        dlugosc += 1
    return dlugosc

x = int(input("Podaj liczbę x w przedziale od 1 do 100: "))
if 1 <= x <= 100:
    dlugosc = ciag_collatza(x)
    if dlugosc is not None:
        print(f"Długość ciągu Collatza dla liczby {x} wynosi {dlugosc}.")
    else:
        print("Podana liczba musi być w przedziale od 1 do 100")
else:
    print("Podano nieprawidłową wartość. Proszę podać liczbę całkowitą w przedziale od 1 do 100.")

