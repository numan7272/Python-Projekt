import time
import random

def animationstext(text):
    text1 = f"{text}"
    text2 = f"\n{text}"
    text3 = f"\n{text}"

    for i in text1:
        print(i, end="", flush=True)
        time.sleep(0.08)

    for _ in text2:
        print(_, end="", flush=True)
        time.sleep(0.3)

    for somea in text3:
        print(somea, end="", flush=True)
        time.sleep(random.uniform(0.05, 0.4))
        




def rechnung_anzeige(benutzername, höhe, frist):
    print(f"Hallo {benutzername}!")
    print(f"Deine Rechnung liegt bei {höhe:.2f}€ und ist bis zum {frist} befristet!")

#rechnung_anzeige(input("Gib deinen Benutzernamen an: "), float(input("Gib die kosten für deine Rechnung in Eur an: ")), input("Gib den Fristsdatum an (DD/MM/JJJJ):"))

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z