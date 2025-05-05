import requests
import time

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        loc = data.get("loc", "")
        if loc:
            latitude, longitude = loc.split(",")
            print(f"Latitude: {latitude}, Longitude: {longitude}")
            return float(latitude), float(longitude)
        else:
            print("Localização não encontrada.")
    except Exception as e:
        print(f"Erro ao obter localização: {e}")

def track_location(interval=10):
    print("Iniciando rastreamento em tempo real...")
    while True:
        get_location()
        time.sleep(interval)

# Executar
track_location()
