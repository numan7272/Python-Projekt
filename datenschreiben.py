import os


Arbeitende = ["Mr.Krabs", "Thaddäus", "Spongebob", "Patrick"]

file_path = "C:\\Users\\numan\\Desktop\\Python-Projekt\\tests\\testordner\\output.txt"

try:
    with open(file_path, "w") as file:
        for arbeiter in Arbeitende:
            file.write(arbeiter + " ")
        print(f"txt datei '{file_path}' wurde erstellt")
except FileExistsError:
    print("Diese Datei existiert bereits!")