""" Zadanie

Napisz program, ktory przyjmie od uzytkownika haslo i je oceni jego sile w skali 1-3, ale musi
to zrobic wedlug konkretnych zasad (dlugosc, obecnosc cyfr, wielkosc liter)

 1. Pobranie tekstu od uztkownika:
 2. Stworzenie zmiennnej punkty'punktu = 0'
 3. test 1: czy haslo ma 8 znakow? jesli tak dodaj punkt
 4. test 1: czy haslo ma choc jedna cyfre? jesli tak dodaj punkt
 5. test 1: czy haslo ma wielka litere jesli tak dodaj punkt
 6. Wyswietl wynik na podstawie punktow.
"""
#
# haslo = input("Podaj haslo: ")
# punkty = 0
# ma_cyfre = False
# if len(haslo) >= 8:
#      punkty += 1
# for znak in haslo:
#     if znak.isdigit():
#         ma_cyfre = True
# if ma_cyfre:
#         punkty += 1
# for znak in haslo:
#     if znak.isupper():
#         punkty += 1
#         break
# print(f"Sila hasla {punkty}/3")

def sprawdz_haslo():
    haslo = input("Podaj haslo: ")
    punkty = 0
    ma_cyfre = False
    if len(haslo) >= 8:
        punkty += 1
    for znak in haslo:
        if znak.isdigit():
            ma_cyfre = True
    if ma_cyfre:
        punkty += 1
    for znak in haslo:
        if znak.isupper():
            punkty += 1
            break
    print(f"Sila hasla {punkty}/3")

if __name__ == "__main__":
    sprawdz_haslo()

