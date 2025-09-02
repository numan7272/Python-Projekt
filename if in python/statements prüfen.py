import time
import sys
import random

text = "Sind Sie berechtigt dieses Produkt zu kaufen?"
for  i in range(len(text)+1):
    sys.stdout.write('\r' + text[:i])
    sys.stdout.flush()
    time.sleep(random.uniform(0.05, 0.1))
print()

Alter = True

while Alter:
    Eingabe = input("Geben Sie ihr Alter in Jahren an: ")

    if Eingabe =="":
        print("Bitte geben Sie was ein!")
        continue

    if not Eingabe.isdigit():
        print("❌ Ungültige Eingabe, bitte nur Zahlen eingeben!")
        continue

    alter = int(Eingabe)


    if alter >= 18:
        print("✅Sie sind berechtigt.")

    else:
        print("╰（‵□′）╯ Sie sind nicht berechtigt dieses Produkt zu kaufen!")
        break





