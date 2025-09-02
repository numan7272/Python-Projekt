import random

Möglichkeiten = ("Schere", "Stein", "Papier")


spielt = True


while spielt:
    Spieler = None
    computer = random.choice(Möglichkeiten)
    
    while Spieler not in Möglichkeiten:
        
        Spieler = input("Schere, Stein oder Papier?: ")
        
        if Spieler  not in Möglichkeiten:
            print("Diese Möglichkeit gibt es nicht!")
            

    
    if Spieler == computer:
        print(f"UNENTSCHIEDEN! \nDu:{Spieler}\nCPU:{computer}")

    elif Spieler == "Schere" and computer == "Papier":
        print("DU HAST GEWONNEN!")
    elif Spieler == "Papier" and computer == "Stein":
        print("DU HAST GEWONNEN!")
    elif Spieler == "Stein" and computer == "Schere":
        print("DU HAST GEWONNEN!")
    else:
        print("DU HAST VERLOREN!")
        
        if not input("Nochmal spielen? (j/n): ").lower() == "j":
            spielt = False
        

    
print("Danke fürs Spielen!")

