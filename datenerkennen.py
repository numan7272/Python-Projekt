import os

file_path = "C:/Users/numan/Desktop/Python-Projekt/tests/testordner/test.txt"

if os.path.exists(file_path):
    print(f"Der Standort '{file_path}' existiert")

else:
    print(f"Der Standort '{file_path}' existiert nicht")