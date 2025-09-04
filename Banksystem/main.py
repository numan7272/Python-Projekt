import time


def kontostand_zeigen(kontostand):
    text = f"Dein Kontostand beträgt {kontostand:.2f}€\n"
    for i in text:
        print(i,end="", flush=True)
        time.sleep(0.09)

def einzahlen(kontostand):
    text1 = f"\nDein Kontostand beträgt {kontostand:.2f}€"
    for i in text1:
        print(i,end="", flush=True)
        time.sleep(0.09)


    
    anzahl = float(input("\nGib ein wie viel Geld du einzahlen willst: "))
    if anzahl < 0:
        print("Ungültige Anzahl!")
        return 0
    else:
        return anzahl


def auszahlen(kontostand):
    text = f"Dein Kontostand beträgt {kontostand:.2f}€\n"
    for i in text:
        print(i,end="", flush=True)
        time.sleep(0.09)
    
    anzahl = float(input("Gib ein wie viel Geld du auszahlen willst: "))
    
    
    
    
    if anzahl > kontostand:
        print("Nicht genügend Geld vorhanden!")
        return 0
    elif anzahl < 0:
        print("Die Eingabe muss größer als 0 sein")
        return 0
    else:
        return anzahl


def main():
    kontostand = 0
    is_running = True

    while is_running:
        text = "\nWillkommen bei der Musterbank."

        for i in text:
            print(i, end="", flush=True)

            time.sleep(0.09)
        
        print("\n1. Kontostand anzeigen")
        print("2. Geld einzahlen")
        print("3. Geld auszahlen")
        print("4. Verlassen")

        option = input("\nWähle deine Option (1-4): ")

        if option == '1':
            kontostand_zeigen(kontostand)
        elif option == '2':
            kontostand+=einzahlen(kontostand)
        elif option == '3':
            kontostand-=auszahlen(kontostand)
        elif option == '4':
            is_running = False
        else:
            print("Ungültige Eingabe!")
        
    text = "Musterbank bedankt sich! Schönen Tag noch."

    for i in text:
        print(i, end="", flush=True)

        time.sleep(0.09)
     

     
if __name__ == '__main__':  
    main()
