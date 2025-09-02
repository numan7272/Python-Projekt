import math
import time
import matplotlib.pyplot as plt 

Gegenkathete = float(input('Geben Sie die Länge der Gegenkathete in cm an: '))
Ankathete  = float(input('Geben Sie die Länge der Ankathete in cm an: '))

a = Gegenkathete
b = Ankathete

Hypothenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
c = Hypothenuse

text = f"Die Länge der Hypothenuse beträgt {Hypothenuse:.2f} cm."

for buchstaben in text:
    print(buchstaben, end="", flush=True)
    time.sleep(0.01)


x_coords = [0, b, 0, 0]
y_coords = [0, 0, a, 0]


plt.plot(x_coords, y_coords)
plt.text(b/2, -0.2, 'b', fontsize=12, ha='center', va= 'top')
plt.text(-0.2, a/2, 'a', fontsize=12, ha='right', va='center')
plt.text(b/2, a/2, 'c', fontsize=12, ha='left', va='bottom')
plt.show()
