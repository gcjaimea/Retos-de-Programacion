import requests

def obtener_informacion_pokemon(nombre_o_numero):
    try:
        # Realizar la petición a la API para obtener los datos del Pokémon
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre_o_numero.lower()}"
        response = requests.get(url)
        response.raise_for_status()  # Lanzará una excepción si el status code es 4xx o 5xx
        data = response.json()

        # Extraer la información básica del Pokémon
        nombre = data['name'].capitalize()
        id_pokemon = data['id']
        peso = data['weight'] / 10  # El peso se da en decigramos, lo convertimos a kg
        altura = data['height'] / 10  # La altura se da en decímetros, lo convertimos a metros
        tipos = [tipo['type']['name'].capitalize() for tipo in data['types']]

        print(f"\nInformación del Pokémon '{nombre}':")
        print(f"  ID: {id_pokemon}")
        print(f"  Peso: {peso} kg")
        print(f"  Altura: {altura} m")
        print(f"  Tipo(s): {', '.join(tipos)}")

        # Obtener la cadena de evoluciones
        obtener_cadena_evolutiva(data['species']['url'])

        # Obtener los juegos en los que aparece el Pokémon
        juegos = [juego['version']['name'].capitalize() for juego in data['game_indices']]
        print(f"  Juegos en los que aparece: {', '.join(juegos)}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except ValueError:
        print("No se encontró información para este Pokémon.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

def obtener_cadena_evolutiva(species_url):
    try:
        # Realizar la petición a la API para obtener la especie y la cadena evolutiva
        response = requests.get(species_url)
        response.raise_for_status()
        species_data = response.json()

        evolution_chain_url = species_data['evolution_chain']['url']
        response = requests.get(evolution_chain_url)
        response.raise_for_status()
        chain_data = response.json()

        # Obtener los nombres en la cadena evolutiva
        print("  Cadena evolutiva:")
        cadena_evolutiva = []
        chain = chain_data['chain']
        while chain:
            cadena_evolutiva.append(chain['species']['name'].capitalize())
            if chain['evolves_to']:
                chain = chain['evolves_to'][0]
            else:
                chain = None

        print(f"    {' -> '.join(cadena_evolutiva)}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while fetching evolution chain: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred while fetching evolution chain: {err}")
    except Exception as e:
        print(f"Se produjo un error inesperado al obtener la cadena evolutiva: {e}")

if __name__ == "__main__":
    nombre_o_numero = input("Introduce el nombre o número del Pokémon: ")
    obtener_informacion_pokemon(nombre_o_numero)