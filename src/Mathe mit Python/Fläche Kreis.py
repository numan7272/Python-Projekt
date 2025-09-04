import math
import time



radius = float(input('Radius eingeben in cm: '))

Kreisfläche = math.pi* pow(radius, 2)

text = f"Die Fläche vom Kreis beträgt {round(Kreisfläche, 2)}cm²."

for buchstabe in text: 
    print(buchstabe, end="", flush=True)
    time.sleep(0.1)


 