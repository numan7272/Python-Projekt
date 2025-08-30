import math
import time




radius = float(input('Radius eingeben in cm: '))

Umfang = 2*math.pi*radius

text = f"Der Umfang vom Kreis beträgt {round(Umfang, 2)}cm."

for buchstabe in text: 
    print(buchstabe, end="", flush=True)
    time.sleep(0.1)


 