import time
import random

text = "Bababoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"

for abc in text:
    print(abc, end="\r", flush=True)
    time.sleep(random.uniform(0.05, 0.2))
    