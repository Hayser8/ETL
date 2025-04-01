import json
import pandas as pd

# Rutas de los archivos originales
archivos_costos = [
    "costos_turisticos_europa.json",
    "costos_turisticos_africa.json",
    "costos_turisticos_america.json",
    "costos_turisticos_asia.json"
]

# 1. Unir todos los archivos de costos turísticos
datos_costos = []
for archivo in archivos_costos:
    with open(archivo, encoding='utf-8') as f:
        datos_costos.extend(json.load(f))

# Guardar el archivo unificado de costos turísticos
with open("costos_turisticos_completo.json", "w", encoding="utf-8") as f:
    json.dump(datos_costos, f, indent=4, ensure_ascii=False)

# 2. Cargar y volver a guardar el archivo de Big Mac
with open("paises_mundo_big_mac.json", encoding="utf-8") as f:
    datos_big_mac = json.load(f)

with open("precios_big_mac.json", "w", encoding="utf-8") as f:
    json.dump(datos_big_mac, f, indent=4, ensure_ascii=False)

print("✅ Archivos generados:\n- costos_turisticos_completo.json\n- precios_big_mac.json")
