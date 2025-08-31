import time
import random


operator = input("Gib ein Operator an (+ - * /): ")
zahl1 = float(input("Nenne die erste Zahl: "))
zahl2 = float(input("Nenne die zweite Zahl: "))


if operator == "+":
    Ergebnis = f"Dein Ergebnis lautet {zahl1 + zahl2}"
    for platz1 in Ergebnis:
        print(platz1, end="", flush=True)
        time.sleep(0.1)
elif operator == "-":
     Ergebnis = f"Dein Ergebnis lautet {zahl1 - zahl2}"
     for platz2 in Ergebnis:
          print(platz2, end="", flush=True)
          time.sleep(0.1) 
    
elif operator == "*":
     Ergebnis = f"Dein Ergebnis lautet {zahl1 * zahl2}"
     for platz3 in Ergebnis:
          print(platz3, end="", flush=True)
          time.sleep(0.1)

elif operator == "/":
     Ergebnis = f"Dein Ergebnis lautet {round(zahl1 / zahl2, 3)}"
     for platz4 in Ergebnis:
        print(platz4, end="", flush=True)
        time.sleep(0.1)

else:
     kukubreee = f"{operator} in dir rein!"
     for platz5 in kukubreee:
          print(platz5, end="", flush=True)
          time.sleep(random.uniform(0.04, 0.1))
    