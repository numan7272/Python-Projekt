import random
import time

num = int(input('Gib eine Zahl von 1 bis 10 an.'))

while num < 1 or num > 10:
    print(f"{num} ist nicht gültig")
    num = int(input('Gib eine Zahl von 1 bis 10 an.'))

print(f"Deine Zahl ist {num}")