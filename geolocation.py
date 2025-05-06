import requests
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import webbrowser

def get_ip_location():
    """Obtém latitude e longitude com base no IP usando ip-api.com."""
    try:
        response = requests.get("http://ip-api.com/json", timeout=5)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'success':
            return data['lat'], data['lon']
    except Exception as e:
        print(f"[ERRO] Não foi possível obter localização por IP: {e}")
    return None, None

def reverse_geocode(latitude, longitude, geolocator=None):
    """Realiza reverse geocoding para obter cidade, estado, bairro e rua."""
    try:
        if not geolocator:
            geolocator = Nominatim(user_agent="geo-tracker", timeout=10)

        location = geolocator.reverse((latitude, longitude), language='pt')
        address = location.raw.get('address', {}) if location else {}

        cidade = (
            address.get('city') or
            address.get('town') or
            address.get('village') or
            address.get('hamlet') or
            "Não identificado"
        )

        estado = address.get('state', "Não identificado")

        bairro = (
            address.get('suburb') or
            address.get('neighbourhood') or
            address.get('residential') or
            "Não identificado"
        )

        rua = (
            address.get('road') or
            address.get('pedestrian') or
            address.get('footway') or
            "Não identificado"
        )

        return cidade, estado, bairro, rua

    except GeocoderTimedOut:
        print("[ERRO] Tempo esgotado na geolocalização.")
    except Exception as e:
        print(f"[ERRO] Falha no reverse geocode: {e}")

    return "Desconhecido", "Desconhecido", "Desconhecido", "Desconhecido"

def abrir_google_maps(latitude, longitude):
    """Abre a localização no Google Maps."""
    url = f"https://www.google.com/maps?q={latitude},{longitude}"
    print(f"🌐 Veja no mapa: {url}")
    webbrowser.open(url)

def track_location(interval=30):
    """Rastreamento contínuo da localização do IP."""
    print("🔍 Iniciando rastreamento de localização via IP...\n(Ctrl+C para parar)\n")
    geolocator = Nominatim(user_agent="geo-tracker-cache", timeout=10)

    try:
        while True:
            lat, lon = get_ip_location()
            if lat and lon:
                cidade, estado, bairro, rua = reverse_geocode(lat, lon, geolocator)
                print(f"📍 Coordenadas: {lat:.6f}, {lon:.6f}")
                print(f"📌 Endereço: Rua {rua}, Bairro {bairro}, {cidade} - {estado}\n")
                abrir_google_maps(lat, lon)
            else:
                print("⚠️ Não foi possível obter localização atual.\n")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n🛑 Rastreamento encerrado pelo usuário.")

# Executar
if __name__ == "__main__":
    track_location(interval=30)
