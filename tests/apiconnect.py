import requests

base_url = "https://restcountries.com/v3.1"

def get_country_info(name):
    url = f"{base_url}/name/{name}"
    response = requests.get(url)
    

    if response.status_code == 200:
        print("Daten abgerufen!")
        country_data = response.json()
        return country_data
    else:
        print(f"Fehlgeschlagen beim Abrufen von Daten {response.status_code}")

country_name = "deutschland"

country_info = get_country_info(country_name)




print(country_info)
    
