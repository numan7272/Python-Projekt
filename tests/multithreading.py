import threading
import time

def ins_fitnessstudio_gehen(Trainingseinheit1,Trainingseinheit2 ):
    time.sleep(4)
    print(f"Du hast {Trainingseinheit1} und {Trainingseinheit2} trainiert.")

def müll_rausbringen():
    time.sleep(1)
    print("Du hast den Müll rausgebracht")

def Lernen():
    time.sleep(2)
    print("Du hast gelernt")

chore1 = threading.Thread(target=ins_fitnessstudio_gehen, args=("Beine","Bauch"))
chore1.start()

chore2 = threading.Thread(target=müll_rausbringen)
chore2.start()

chore3 = threading.Thread(target=Lernen)
chore3.start()

chore1.join()
chore2.join()
chore3.join()