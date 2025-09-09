import time
import datetime
import pygame

def wecker_einstellen(wecker_zeit):
    print(f"Wecker um {wecker_zeit} eingestellt!")
    sound_file = "src/Wecker/Homecoming - Samsung Ringtone.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Aktuelle Zeit: {current_time}", end="\r")
        
        if current_time == wecker_zeit:
            print("\nAUFSTEHEN!⏰")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)


if __name__ == "__main__":
    wecker_zeit = input("Stelle dein Wecker ein (HH:MM:SS): ")

    try:
        datetime.datetime.strptime(wecker_zeit, "%H:%M:%S")
        wecker_einstellen(wecker_zeit)
    except ValueError:
        print("Bitte den Wecker in folgenden Format einstelen (HH:MM:SS)")
   

    

