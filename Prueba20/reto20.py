import requests

# URL de ejemplo
url = "https://retosdeprogramacion.com/roadmap"

# Realizar la petición GET
response = requests.get(url)

# Verificar el código de estado de la respuesta
if response.status_code == 200:
    # Comprobar si la respuesta es JSON
    try:
        data = response.json()  # Intentar convertir a JSON
        print(data)
    except ValueError:
        # Si falla, es porque el contenido no es JSON
        print("La respuesta no es un JSON válido. Aquí está el contenido de la respuesta:")
        print(response.text)
else:
    print(f"Error en la petición: {response.status_code}")