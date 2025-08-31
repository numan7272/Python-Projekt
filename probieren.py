import time
import random

#2 5 4 3 1

Eingabe = list(input("Gib deine gewünschte sortierte Zahlenliste an: ").split())

list.sort(Eingabe)

text = f"Hier ist deine sortierte Liste{Eingabe}"
for platz1 in text:
    print(platz1, end="", flush=True)
    time.sleep(random.uniform(0.1, 0.15))