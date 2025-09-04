import time

Zeiteinstellung = int(input("Gib deine Zeit in Sekunden an: "))

for x in range(Zeiteinstellung, 0,-1):
    Sekunden = x % 60
    Minuten = int(x / 60) % 60
    Stunden = int(x /3600) 
    print(f"{Stunden:02}:{Minuten:02}:{Sekunden:02}")
    time.sleep(1)

print("Zeit ist abgelaufen!⏲")