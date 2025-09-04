import random
from wörterliste import Wörter as gemüse                    #als gemüse weil ich vorher nicht eine wörterliste hatte :)

galgenmännchen = {
            0: (
                "  +---+",
                "  |   |",
                "      |",
                "      |",
                "      |",
                "      |",
                "========"
            ),
            1: (
                "  +---+",
                "  |   |",
                "  O   |",
                "      |",
                "      |",
                "      |",
                "========"
            ),
            2: (
                "  +---+",
                "  |   |",
                "  O   |",
                "  |   |",
                "      |",
                "      |",
                "========"
            ),
            3: (
                "  +---+",
                "  |   |",
                "  O   |",
                " /|   |",
                "      |",
                "      |",
                "========"
            ),
            4: (
                "  +---+",
                "  |   |",
                "  O   |",
                " /|\\  |",
                "      |",
                "      |",
                "========"
            ),
            5: (
                "  +---+",
                "  |   |",
                "  O   |",
                " /|\\  |",
                " /    |",
                "      |",
                "========"
            ),
            6: (
                "  +---+",
                "  |   |",
                "  O   |",
                " /|\\  |",
                " / \\  |",
                "      |",
                "========"
            ),
        }

def display_man(nieten):
    for line in galgenmännchen[nieten]:
        print(line)


def display_hinweis(hinweis):
    print(" ".join(hinweis))
def display_lösung(lösung):
    print(" ".join(lösung))

def main():
    
    lösung = random.choice(gemüse)
    hinweis = ["_"] * len(lösung)
    nieten = 0
    versuche = set()
    is_running = True

    


    while is_running:
        
        display_man(nieten)
        display_hinweis(hinweis)
        versuch = input("Gib ein Wort ein: ").lower()

        if len(versuch) != 1 or not versuch.isalpha():
            print("Ungültige Eingabe!")
            continue
        
        if versuch in versuche:
            print(f"{versuch} ist schon versucht worden!")

        versuche.add(versuch)


        if versuch in lösung:
            for index in range(len(lösung)):
                if lösung[index] == versuch:
                    hinweis[index] = versuch
        else:
            nieten += 1

        if "_" not in hinweis:
           display_man(nieten)
           display_lösung(lösung)
           print("Herzlichen Glückwunsch!\nDu hast den Galgenmännchen gerettet")
           is_running = False
            
        elif nieten >= len(galgenmännchen) -1:
            display_man(nieten)
            display_lösung(lösung)
            print("Schade!\nDer Galgenmännchen wurde erhangen.")
                     



if __name__ == "__main__":
    main()