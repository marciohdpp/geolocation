#!/usr/bin/env python3
import sys
import logging
from geopy.geocoders import Nominatim

logfile = "/var/www/html/logs/script_debug.log"
logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("Script iniciado")

def reverse_geocode(lat, lon):
    try:
        geolocator = Nominatim(user_agent="geo-accurate", timeout=10)
        location = geolocator.reverse((lat, lon), language='pt')
        address = location.raw.get('address', {}) if location else {}

        cidade = address.get('city') or address.get('town') or "Não identificado"
        estado = address.get('state', "Não identificado")
        bairro = address.get('suburb') or address.get('neighbourhood') or "Não identificado"
        rua = address.get('road') or "Não identificado"

        result = (
            f"📍 Coordenadas: {lat}, {lon}\n"
            f"📌 Endereço: Rua {rua}, Bairro {bairro}, {cidade} - {estado}\n"
            f"🗺 Mapa: https://www.google.com/maps?q={lat},{lon}"
        )

        logging.debug("Endereço resolvido")
        logging.debug(result)
        print(result)
    except Exception as e:
        logging.error(f"Erro ao fazer reverse geocode: {e}")
        print(f"Erro no script: {e}")

if _name_ == "_main_":
    if len(sys.argv) != 3:
        logging.error("Argumentos ausentes")
        print("Uso: script.py <latitude> <longitude>")
        sys.exit(1)

    lat = float(sys.argv[1])
    lon = float(sys.argv[2])
    reverse_geocode(lat, lon)
