Zeit = 0
Kapital = 0
Zinsen = 0


while True:
    Zeit = int(input("Gib Zeit in Jahren an: "))
    if Zeit < 0:
        print("Die Zeit kann nicht weniger als 0 Jahre sein!")
    else:
        break

while True:
    Zinsen = float(input("Gib Zinsen in Prozent an: "))
    if Zinsen < 0:
        print("Die Zinsen können nicht weniger als 0 Prozent sein!")
    else:
        break
    

while True:
    Kapital = float(input("Gib Kapital in Eur an: "))
    if Kapital < 0:
        print("Kapital kann nicht weniger als 0€ sein!")
    else:
        break

Ergebnis = Kapital*pow((1+Zinsen/100), Zeit)

print(f"Die Balance nach {Zeit} Jahren: {Ergebnis:,.2f}€")