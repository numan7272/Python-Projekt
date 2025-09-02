nummerfeld = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 9),
              ("*", 0, "#"))


for reihe in nummerfeld:
    for nummer in reihe:
        print(nummer, end=" ")
    print()