menu = {"döner": 8.00,
        "dönerbox": 6.50,
        "pizza": 11.50,
        "pommes": 4.50,
        "pizzabrötchen": 7.50,
        "ayran": 2.70,
        "fanta": 2.50}

einkauf = []
gesamtkosten = 0

print("------------MENÜ------------")

for key, value in menu.items():
    print(f"{key:15}: {value:.2f}€")

print("----------------------------")

while True:
    food = input("Wähle aus was du Essen willst(x zum beenden): ")
    if food.lower() == "x":
        break
    elif menu.get(food) is not None:
        einkauf.append(food)

for food in einkauf:

    gesamtkosten += menu.get(food)
    print(food, end=" | ")

print("----------------------------")
print(f"Das macht: {gesamtkosten:.2f}€ bitte!")
