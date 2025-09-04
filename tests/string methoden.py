username = input("Bitte geben Sie ihren Namen ein: ")

if len(username) > 12:
    print("Es darf nicht mehr als 12 Zeichen haben!")
elif not username.find(" ") == -1:
    print("Es darf keine Leerzeichen haben!")
elif username.isalnum():
    print("Es darf keine Zahlen haben!")
else:
    print(f"Moin {username}")

  

