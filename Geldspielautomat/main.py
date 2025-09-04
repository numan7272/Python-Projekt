import time
import random


def dreh_reihe():
    symbole = ['🔔', '🍉', '🍊',
                '🍒', '💎']
    
    return [random.choice(symbole) for _ in range(3)]

def print_reihe(reihe):
    print(" | ".join(reihe))

def auszahlen(reihe, Wette):
    if reihe[0] == reihe[1] == reihe[2]:
        if reihe[0] == '🍒':
            return Wette * 2
        elif reihe[0] == '🍊':
            return Wette * 1.5
        elif reihe[0] == '💎':
            return Wette * 100
        elif reihe[0] == '🔔':
            return Wette * 25
        elif reihe[0] == '🍉':
            return Wette * 5
    return 0
        
    


def main():
    kontostand = 100
    

    text = "Willkommen zu Python Slots\n"
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.09)


    print("Symbole: 🔔🍉🍊🍒💎")

    while kontostand > 0:
        print(f"Aktueller Kontostand {kontostand}€")

        Wette = input("Gib dein Einsatz an: ")

        if not Wette.isdigit():
            print("Gib eine gültige Nummer an!")
            continue
        
        Wette = int(Wette)

        if Wette > kontostand:
            print("Nicht verfügbares Geld!")
            continue

        if Wette <= 0:
            print("Einsatz muss mehr als 0€ sein!")
            continue

        kontostand -= Wette

        reihe = dreh_reihe()
        print("Dreht...")
        time.sleep(random.uniform(0.05, 0.1))

        print_reihe(reihe)

        auszahlung = auszahlen(reihe, Wette)

        if auszahlung > 0:
            print(f"Du hast {auszahlung}€ gewonnen!")
        else:
            text4 = ["Satz mit X war wohl nix!", 
                     "Das war wohl der Probelauf.", 
                     "Knapp daneben ist auch vorbei."]
            print(random.choice(text4))

        kontostand += auszahlung 

        nochmal = input("Willst du nochmal drehen? (J/N): ").upper()

        if nochmal != 'J':
            break
    print("**********************************")
    print(f"GAME OVER! Dein Kontostand beträgt {kontostand}€")


if __name__ == '__main__':
    main()