import re

def mostrar_menu():
    print("Validar un email: [e]")
    print("Validar un telefono: [t]")
    print("Validar una url: [u]")
    print("Salir de la aplicacion [s]")
    return input(f"Por favor indique que la opcion a validar [e], [t], [u],[s]: ").lower()



def main():

    while True:

        opcion = mostrar_menu()

        if opcion == "e":
            validar_email()
        
        elif opcion == "t":
            validar_telefono()
        
        elif opcion == "u":
            validar_url()

        elif opcion == "s":
            salir()
            break
        else:
            print("Opcion Invalida, intente de nuevo")


def validar_email():
    correo = input("indroduzca el email: ")
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.match(patron, correo):
        print("Correo válido")
    else:
        print("Correo inválido")

def validar_telefono():
    telefono = input("Introuzca el telefono (000)1234567: ")
    patron = r"^\(\d{3}\)\d{7}$"

    tel_validado = re.search(patron, telefono)
    if tel_validado:
        print("Telefono Valido:", tel_validado.group())
    else:
        print("Telefono no valido")

def validar_url():
    patron = re.compile(
    r'^(https?:\/\/)?'                   # Protocolo opcional (http o https)
    r'(([a-zA-Z0-9\-_]+\.)+[a-zA-Z]{2,6})'  # Dominio (ej. www.example.com)
    r'(:\d+)?'                           # Puerto opcional (ej. :80)
    r'(\/[a-zA-Z0-9\-_\.~\/]*)*'         # Rutas opcionales (ej. /path/to/resource)
    r'(\?[a-zA-Z0-9\-_=&]*)?$'           # Parámetros de consulta opcionales (ej. ?key=value)
    )
###hay muchas variaciones de las urls...para casos mas complejos python cuenta con validators o urllib.parse
    url = input(" Por favorintroduzca la url a validar: ")
    if re.match(patron, url):
        print("URL válida")
    else:
        print("URL inválida")
    
def salir():
    print("Salida del Programa")
           

main()


