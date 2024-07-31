#Programa de Agenda de Contactos

# Crear el menu de opciones
def mostrar_menu():
    print("[1] : Crear Contacto:")
    print("[2] : Buscar Contacto:")
    print("[3] : Actualizar Contacto:")
    print("[4] : Eliminar Contacto:")
    print("[5] : Mostrar Contacto:")
    print("[6] : Salir del Programa:")
    return input("Hola, Por favor selecciona una opción [1] [2] [3] [4] [5] [6]: ")
   


def main():
   
   agenda = {}
   while True:
        opcion = mostrar_menu()             
        if opcion == "1":
            crear_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            mostrar_contactos(agenda)
        elif opcion =="6":
            salir_programa()
        else:
            print("usted eligio una opción No válida")
        


def crear_contacto(agenda):
    nombre = input("Me indica su nombre completo: ")
    numero = input("Me indica su número de celular menor a 11 digitos y sólo números: ")
    if numero_valido(numero):
        agenda[nombre] = numero
        print(f"Contacto {nombre} agregado correctamente")
    else:
        print("ERROR!!!! Introdujo numero incorrecto ")



def numero_valido(numero):
    return numero.isdigit() and len(numero) <= 11



def buscar_contacto(agenda):
    nombre = input("Por favor me indica el nombre del contacto a buscar: ")
    if nombre in agenda:
        print(f"Contacto {nombre} : {agenda[nombre]}")
    else:
        print("Contacto no pertenece a esta agenda")


def actualizar_contacto(agenda):
    nombre = input ("Por favor me indica el nombre del contacto a actualizar:")
    if nombre in agenda:
        nombre = input("Por favor introduzca su nuevo nombre:")
        numero = input("Por favor introduzca su nuevo número: ")
        if numero_valido(numero):
            agenda[nombre] = numero
            print(f"Ha actualizado correctamente el contacto: {nombre} : {agenda[nombre]}")
        else:
            print("ERROR!!!! Introdujo numero incorrecto ")



def eliminar_contacto(agenda):
    nombre = input("Me indica el nombre del contacto a eliminar: ")
    del agenda[nombre]
    print("Contacto Borrado correctamente")



def mostrar_contactos(agenda):
    print("\n*************Listas de Contactos:*************")
    for nombre in agenda:

        print (f"{nombre} : {agenda[nombre]}")
    print("\n************************************************")

def salir_programa():
    print(" Saliendo del programa")
    exit()
    



if __name__ == "__main__":
    main()


