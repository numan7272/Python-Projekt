import random
import time

text = "Ich würfel jetzt mein Würfel"

for i in text:
    print(i, end="", flush=True)
    time.sleep(0.1)

print()

for _ in range(10):
    zahl = random.randint(1, 6)
    print(f"\r{zahl}", end="", flush=True)

    time.sleep(0.2)

print(f"\nEndergebnis: {zahl}")