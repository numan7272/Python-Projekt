reihen = int(input("Gib ein die Anzahl an Reihen die du haben willst: "))
zeilen = int(input("Gib ein die Anzahl an Zeilen die du haben willst: "))
symbol = input("Gib ein Symbol: ")

for x in range(reihen):
    for y in range(zeilen):
        print(symbol, end="")
    print()