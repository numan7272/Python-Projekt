import time
import sys
import random

text = "Sind Sie berechtigt dieses Produkt zu kaufen?"
text2 = "Verarschen kannst du jemanden anderen!"
for  i in range(len(text)+1):
    sys.stdout.write('\r' + text[:i])
    sys.stdout.flush()
    time.sleep(random.uniform(0.05, 0.1))
print()

Alter = (input("Gib deinen Alter an: "))

if Alter >= 18:
    print("Sie sind berechtigt ")
elif Alter < 0:
    for komplett in text2:
        print(komplett, end="", flush=True)
        time.sleep(random.uniform(0.05, 0.1))

elif Alter < 18:
    print("╰（‵□′）╯ Sie sind nicht berechtigt dieses Produkt zu kaufen!")



