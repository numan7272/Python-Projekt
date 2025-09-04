import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()

random.shuffle(key)


#print(f"chars: {chars}")
#print(f"key  : {key}")


#verschlüsselung
texteingabe = input("Gib eine Nachricht zum verschlüsseln: ")
verschlüsselter_text = ""

for buchstabe in texteingabe:
    index = chars.index(buchstabe)
    verschlüsselter_text += key[index]

print(f"Originaler Text: {texteingabe}")
print(f"verschlüsselter Text: {verschlüsselter_text}")


#entschlüsselung
verschlüsselter_text = input("Gib eine Nachricht zum entschlüsseln: ")
texteingabe = ""

for buchstabe in verschlüsselter_text:
    index = key.index(buchstabe)
    texteingabe += chars[index]


print(f"verschlüsselter Text: {verschlüsselter_text}")
print(f"Originaler Text: {texteingabe}")