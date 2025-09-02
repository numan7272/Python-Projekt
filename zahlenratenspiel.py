import random
import time

niedrigste_num = 1
höchste_num = 100
lösung = random.randint(niedrigste_num, höchste_num)
versuche = 0
spielt = True

Willkomenstext = "Hallo und Willkommen zum Zahlenratenspiel!"
Beschreibungstext = f"\nRate eine Zahl zwischen {niedrigste_num} und {höchste_num}"

for i in Willkomenstext:
    print (i, end="", flush=True)
    time.sleep(0.15)


for _ in Beschreibungstext:
    print(_, end="", flush=True)
    time.sleep(0.1)


while spielt:
    

    versuch = input("\nRate eine Zahl: ")

    if versuch.isdigit():
        versuch = int(versuch)
        versuche += 1


        if versuch < niedrigste_num or versuch > höchste_num:
            print(f"Diese Zahl ist nicht zwischen {niedrigste_num} und {höchste_num}!")
            
            Beschreibungstext = f"Rate eine Zahl zwischen {niedrigste_num} und {höchste_num}"
            
            for _ in Beschreibungstext:
                print(_, end="", flush=True)
            time.sleep(0.1)
        elif versuch < lösung:
            print('Zu niedrig! Probier es nochmal!')
        elif versuch > lösung:
            print('Zu hoch! Probier es nochmal!')
        else:
            print(f"RICHTIG! Die Lösung ist {lösung}")
            print(f"Anzahl der Versuche: {versuche}")
            spielt = False
        


    else:
        print("Ungültiger Versuch")
        

        Beschreibungstext = f"Rate eine Zahl zwischen {niedrigste_num} und {höchste_num}"

        for _ in Beschreibungstext:
            print(_, end="", flush=True)
            time.sleep(0.1)
    
    


