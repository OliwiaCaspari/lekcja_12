try:
    print(10/0)
except:
    print("Nie dziel przez zero!")
finally:
    print("Blok finally. Zawsze wykonywany")

print("*" * 120)

try:
    print(10/10)
except:
    print("Nie dziel przez zero!")
finally:
    print("Blok finally. Zawsze wykonywany")
