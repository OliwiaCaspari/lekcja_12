"""Zadanie :
 Napisz program, ktory zwraca wartosc bezwgledna liczby podanej od uztkownika.
 Program powinien pytac o liczbe tak dlugo, az nie zostanie ona poprawnie podana.

 Pamietajcie, ze uzytkownik nie zawsze wpisze wartosc numeryczna, moze tez wpisac np. kalafior
 """
while True:
    try:
        liczba = int(input("Podaj liczbe, ktora chcesz przeksztalcic na bezwzgledna: "))
        if liczba < 0:
            liczba = - liczba
            print(f"Twoja liczba bezwzgledna to:{liczba}")
            break
        else:
            print(f"Twoja liczba bezwzgledna to:{liczba}")
            break
    except ValueError: