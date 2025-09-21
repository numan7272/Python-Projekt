#Studenten = {"Numan", "Rohat", "Kristian"}

Email = "numanyesil@student.de"

student = input("Melde dich mit deinen Studentenemail an: ")

#if student in Studenten:
#   print(f"Hallo {student}! Willkommen bei dem Test.")
#else:
#    print(f"{student} wurde nicht gefunden.")

if "@" in student and "." in student:
    print("gültige Email")

else:
    print("ungültige Email")