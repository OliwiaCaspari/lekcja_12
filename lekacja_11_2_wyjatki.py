while True:
    try:
        liczba_1 = int(input("Podaj pierwsza liczbe: "))
        liczba_2 = int(input(f"Podaj wartosc przez jaka podzielic liczbe {liczba_1}: "))
        print(liczba_1 / liczba_2)
        break
    except ValueError:
        print("Podales inna wartosc niz liczba calkowita")
    except ZeroDivisionError:
        print("Nie dziel przez zero.")
    print("Spróbuj ponownie.\n")

# print("2" + 2) # TypeError
# print(liczba_3) #NameError

