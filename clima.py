
import requests

def consultar_clima(ciudad, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric'
    
    print(url)
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temperatura = data['main']['temp']
        descripcion = data['weather'][0]['description']
        print(f'El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C')
    else:
        print(f'Error al consultar el clima: {response.status_code}')

# Reemplaza con la ciudad que desees consultar
ciudad = 'London,UK'

# Reemplaza 'TU_API_KEY' con tu propia clave de API de OpenWeatherMap
api_key = '300eeba85ab2edcc53bac406b8a7d004'

consultar_clima(ciudad, api_key)



