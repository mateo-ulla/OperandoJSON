import requests, webbrowser

respuesta = requests.get('https://api.wheretheiss.at/v1/satellites/25544')
respuesta.raise_for_status()
iss_data = respuesta.json()
    
latitude = iss_data['latitude']
longitude = iss_data['longitude']
print(latitude)
print(longitude)

maps_url = f"https://www.google.com/maps/@{latitude},{longitude},14z?entry=ttu"

webbrowser.open(maps_url)
