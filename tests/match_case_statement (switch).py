def wochentag(tag):
    match tag:
        case "Sonntag" | "Samstag":
            return True
        case "Montag" | "Dienstag" | "Mittwoch" | "Donnerstag" | "Freitag":
            return False
        
        case _:
            return False
        

Eingabe = wochentag(input("Welcher Wochentag ist es: "))

if Eingabe == True:
    print("Es ist Wochenende🥳")
elif Eingabe == False:
    print(f"Es ist noch nicht Wochenende😢")

