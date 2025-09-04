#Studenten = {"Numan", "Rohat", "Kristian"}

Email = "numanyesil@student.de"

student = input("Melde dich mit deinen Studentennamen an: ")

#if student in Studenten:
#   print(f"Hallo {student}! Willkommen bei dem Test.")
#else:
#    print(f"{student} wurde nicht gefunden.")

if "@" in Email and "." in Email:
    print("gültige Email")

else:
    print("ungültige Email")