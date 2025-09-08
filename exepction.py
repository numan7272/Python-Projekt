

try:
    nummer = int(input("Gib eine Nummer ein: "))

    print(1/nummer)
except ZeroDivisionError:
    print("Durch Null teilen geht nicht!")
except ValueError:
    print("Nur Zahlen bitte!")
finally:
    print("Änder es!")