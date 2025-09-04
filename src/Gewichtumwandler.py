import time
import random

Gewicht = float(input(f"Gib ein wie viel dein Gewicht wiegt: "))
Einheit = input(f"Wähle deine ursprüngliche Einheit(kg oder lbs): ")

if Einheit in ["kg", "Kg", "KG"]:
    Ergebnis = f"Dein Gewicht in lbs ist {round(Gewicht * 2.20462, 2)}"
    for platz1 in Ergebnis:
        print(platz1, end="", flush=True)
        time.sleep(random.uniform(0.1, 0.15))
elif Einheit in ["lbs", "Lbs", "LBS"]:
    Ergebnis = f"Dein Gewicht in kg ist {round(Gewicht / 2.20462, 2)}"
    for platz2 in Ergebnis:
        print(platz2, end="", flush=True)
        time.sleep(random.uniform(0.1, 0.15))