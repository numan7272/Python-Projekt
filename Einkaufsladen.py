Lebensmitteln = []
Preise = []
Gesamtkosten = 0

while True:
    Lebensmittel = input("Gib ein welches Lebensmittel du kaufen willst(q zum beenden): ")
    if Lebensmittel.lower() == "q":
        break
    else:
        Preis = float(input(f"Gib ein wie teuer {Lebensmittel} ist: €"))
        Lebensmitteln.append(Lebensmittel)
        Preise.append(Preis)

for Preis in Preise:
    Gesamtkosten += Preis
    
print("--------- DEIN EINKAUF ---------")

for Lebensmittel in Lebensmitteln:
    print(Lebensmittel, end=' | ')


print()
print(f"Deine gesamter Einkauf kostet: {Gesamtkosten:.2f}", end="€")
print()
print("--------------------------------")