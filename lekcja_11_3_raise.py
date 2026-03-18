try:
    raise SyntaxError
except SyntaxError:
    print("Nastapil blad skladniowy")

try:
    print(10/0)
except ZeroDivisionError as e:
    print("Nie dziel przez zero!")
    print(e, e.args, type(e))
except Exception:
    print("Klasa ogolny blad")
print(10/0)