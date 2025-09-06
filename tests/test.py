import cv2

# Kamera öffnen (0 = Standardkamera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Fehler: Kamera konnte nicht geöffnet werden")
    exit()

while True:
    # Frame lesen
    ret, frame = cap.read()
    if not ret:
        print("Fehler beim Lesen des Frames")
        break

    # Frame anzeigen
    cv2.imshow("Webcam", frame)

    # Mit 'q' beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Alles schließen
cap.release()
cv2.destroyAllWindows()
