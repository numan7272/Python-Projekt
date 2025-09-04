import random
import time
import sys

Länge = int(input("Geben Sie an wie lang die Liste seien soll: "))

zahlen = [random.randint(1, 10000) for blablabla in range(Länge)]

Liste1 = f"Unsortierte Liste lautet: {zahlen}"
for platz1 in Liste1:
    print(platz1, end="", flush=True)
    time.sleep(random.uniform(0.05, 0.12))


#Bubble sort
for durchgang in range(len(zahlen)-1):          #äußere Schleife
    for index in range(len(zahlen)-1):
        linke_zahl = zahlen[index]
        rechte_zahl = zahlen[index+1]

        if linke_zahl > rechte_zahl:
            zahlen[index], zahlen[index+1] = rechte_zahl, linke_zahl

print("\n")


print("Ich sortiere", end="")

wiederholungen = 5
for _ in range(wiederholungen):
    for punkte in [".", "..", "..."]:
        sys.stdout.write("\rIch sortiere" + punkte)
        sys.stdout.flush()
        time.sleep(0.5)

print("\n")

Liste3 = f"Sortierte Liste: {zahlen}"
for platz3 in Liste3:
    print(platz3, end="", flush=True)
    time.sleep(random.uniform(0.05, 0.12))



