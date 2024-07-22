# print("witaj w naszej zappce nano")
# koniec_artykulow = False
# while not koniec_artykulow:
#     produkt = input("podaj mi swój produkt ")
#     if produkt == "":
#         koniec_artykulow = True
#         break
#     elif produkt =="opony":
#         print("brak w sklepie")
#         continue
#     elif produkt == "plyn do kapieli":
#         # print("jeszcze nie ma na skladzie")
#         pass
#     produkt = produkt.lower()
#     # produkt.capitalize() - daje same duze litery
#     produkt_wymaga_sprawdzenia = False
# # if produkt in ["alkohol", "papierosy", "energetyk"]
#     if produkt == "alkohol" or produkt == "papierosy" or produkt == "energetyk":
#         produkt_wymaga_sprawdzenia = True
#         wiek = int(input("podaj swój wiek "))
#         if wiek < 18:
#             print("niestety nie możesz kupić alko! grow up!")
#         else:
#             print(f"Hura, kupiles {produkt}")
#     if not produkt_wymaga_sprawdzenia:
#         print(f"Hura, kupiles {produkt}")

#2
# wiek = int(input("podaj swój wiek "))
# if wiek <= 21:
#     print("powinienes sie uczyc")
# elif 21 < wiek <= 65:
#     print("powinienes pracowac!")
# else:
#     print("powinenes sie emerycic!")

#3
# wiek = int(input("podaj swój wiek "))
# #while warunek ktory musi byc prawdziwy
#     # blok kodu, ktory bedzie wykonywany
# while wiek <= 18:
#     print("nie masz jeszcze 18 lat! grow up!")
# wiek += 1 #wiek = iteracja o 1 wiek +1 #14 -> 15
# else:
# print("skoczona ppetla")
# print("hura jestes juz pelnoletni, mozesz kupic alkohol")

#4 adam
# wyraz = input("podaj wyraz do przeliterowania ")
# #for <zmienna lokalna> in <struktura iterowalna>
# for litera in wyraz:
#     print(litera)

#5
# wiek = int(input("podaj swój wiek "))
# for rok in range(wiek): # range( 10, wiek, 2) - od 10 co 2
#     print(rok + 1)


#6
# lista_uczniow = ["Adam", "Juliusz", "Bartek"]
# for uczen in lista_uczniow:
#     if uczen == "Juliusz":
#         print("Twoj wynik to 70%")
#         break
#     print(uczen)

wyplata = float(input("podaj mi swoja wyplate: "))
if wyplata < 2000:
    print("ZUS zabierze 200 zl")
elif 2000 <= wyplata < 4000:
    print("ZUS zabierze 400 zł")
else:
    print("ZUS wynosi 800 zl")

match wyplata:
    case 2000:
        print("ZUS zabierze 200 zl")
    case 2500:
        print("ZUS zabierze 300 zł")
    case 3000:
        print("ZUS zabierze 400 zł")
    case _:
        print("ZUS zabierze x zł")

