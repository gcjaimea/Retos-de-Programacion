# Muestra ejemplos de creación de todas las estructuras soportadas por defecto
# en tu lenguaje.


#  Estructura Lista: Es una coleccion de datos ordenada y mutable de elementos
#**************************************
lista1 = [1, 2, 3, 4, 5, 6, 7]
print(lista1)
print(type(lista1))
 #Incluir un elemento en una lista
lista1.append(8)
lista2 =lista1
print("Lista1 incluyendo un elemento:", lista2)
print(type(lista2))

# borrar un elemento
lista2.remove(4)
lista3 = lista2
print("lista2 con el elemento 4 eliminado", lista3)

# actualizar una lista
lista3[1] = 100
lista4 = lista3
print("lista 3 actualizada", lista4)

#ordenar una lista

lista4.sort()
lista5 = lista4
print("lista 4 ordenada", lista5)
### OTRA FORMA
lista4 = [1, 100, 3, 4, 5, 6, 7, 8]
lista6 = sorted(lista4)
print("lista 4 ordenada sin perder la lista4: ", lista6)
#***************************************



#Estructura Tupla es una coleccion ordenada e inmutable de elementos
#****************************************
tupla = (1, 7, 3, 6, 5, 4, 2)
print(tupla)
print(type(tupla))
#Incluir un elemento en una tupla. No se puede directamente, hay que convertirla a lista primero
tupla_lista = list(tupla)
print(tupla_lista)
print(type(tupla_lista))
tupla_lista.append(8)
tupla1 =tuple(tupla_lista)
print("tupla adicionada con un elemento usuando tupla_lista: ", tupla1)
print(type(tupla1))


#Borrado de un elemento de una tupla. No se puede directamente, hay que convertirla a lista primero
tupla = (1, 7, 3, 6, 5, 4, 2)
print(tupla)
print(type(tupla))
tupla_lista = list(tupla)
print(tupla_lista)
print(type(tupla_lista))
tupla_lista.remove(7)
tupla1 =tuple(tupla_lista)
print("tupla modificada con un elemento usuando tupla_lista: ", tupla1)
print(type(tupla1))

# Actualizacion de una tupla. No se puede directamente, hay que convertirla a lista primero
tupla = (1, 7, 3, 6, 5, 4, 2)
print(tupla)
print(type(tupla))
tupla_lista = list(tupla)
print(tupla_lista)
print(type(tupla_lista))
tupla_lista[2] =100
tupla1 =tuple(tupla_lista)
print("tupla actualizada con un elemento despues de un cambio  usuando tupla_lista: ", tupla1)
print(type(tupla1))

#ordenacion de una tupla. No se puede directamente, hay que convertirla a lista primero
#tupla = (1, 7, 3, 6, 5, 4, 2)
print(tupla)
print(type(tupla))
tupla_lista = list(tupla)
print(tupla_lista)
print(type(tupla_lista))
tupla_lista.sort()
tupla1 =tuple(tupla_lista)
print("tupla ordenada usuando tupla_lista", tupla1)
print(type(tupla1))
#*********************************************************************************************


#Estructura Conjunto (Set) son mutables, pero no se puede acceder a el por índice ya que no es ordenada
#*******************************************************************************************************
#Incluir un elemento en una tupla. No se puede directamente, hay que convertirla a lista primero
conjunto = {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto)
print(type(conjunto))
conjunto.add(100)
print("Conjunto con un elemento añadido",conjunto)

# Borrado de un elemento ehn un conjunto
conjunto = {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto)
print(type(conjunto))
conjunto.remove(4)
print("Conjunto con un elemento añadido",conjunto)

# actualizar un conjunto
conjunto = {1, 2, 3, 4, 5, 6, 7, 8}
print(conjunto)
print(type(conjunto))
conjunto.update([20,30,40])
print("Conjunto con un elemento añadido",conjunto)

#ordenacion de un conjunto. No es ordenable
conjunto = {1, 6, 7, 3, 5, 4, 8, 2}
print(conjunto)
print(type(conjunto))
conjunto_ordenado = sorted(conjunto)
print("Conjunto ordenado",conjunto_ordenado)
#*******************************************************************************************************


# estructura diccionadrio. Es una coleccion no ordenable y mutable de pares clave-valor. Cada Clave es unica
#********************************************************************************

#Incluir un elemento en un diccionario
diccionario = {'a': 1, 'b': 2, 'c':3}
print(diccionario)
print(type(diccionario))
diccionario["d"] = 4
print("Diccionario con adicion de un elemento",diccionario)

# Borrar un elemento de un diccionario
diccionario = {'a': 1, 'b': 2, 'c':3}
print(diccionario)
print(type(diccionario))
del diccionario["b"]
print("Diccionario con eliminacion de un elemento",diccionario)

# actualizar un elemento de un diccionario
diccionario = {'a': 1, 'b': 2, 'c':3}
print(diccionario)
print(type(diccionario))
diccionario.update({"b": 4, "n":100})
print("Diccionario actualizado ",diccionario)

#Ordenar un diccionario. Se pueden ordenar por claves o valor
diccionario = {'k':20, 'a': 1, 'd': 2, 'b':3}
print(diccionario)
print(type(diccionario))
diccionario_ordenado_por_clave =dict(sorted(diccionario.items()))
print("Diccionario ordenado por clave ",diccionario_ordenado_por_clave)
diccionario_ordenado_por_valor = dict(sorted(diccionario.items(), key=lambda item: item[1]))
print("Diccionario ordenado por valor ",diccionario_ordenado_por_clave)

#****************************************************************************************************


#Programa de Agenda de Contactos


def mostrar_menu():
    print("\n Agenda de Contactos")
    print("1 : Insetar Contacto")
    print("2 : Buscar contacto")
    print("3 : Actualizar contacto")
    print("4: eliminar contacto:")
    print("5 : Mostrar todos los contactos")
    print("6 : Salir")
    return input("Por favor indique una opcion [1] [2] [3] [4] [5] [6]:  ")

def es_valido_numero(numero):
    return numero.isdigit() and len(numero) <= 11

def insertar_contacto(agenda):
    nombre = input("Escribe tu nombre completo:  ")
    numero = input("Escribe tu numero de telefono, menor de 12 digitos:  ")

    if es_valido_numero(numero):
        agenda[nombre] = numero
        print (f"Contacto: {nombre} añadido correctamente")
    else:
        print("Numero de telefono incorrecto debe ser nuemrico y menor de 11 digitos")


def buscar_contacto(agenda):
    nombre = input("Por favor introduce el nombre a buscar: ")
    if nombre in agenda:
        print(f"{nombre}: {agenda.items()}")
    else: 
        print(f"Contacto {nombre} no encontrado")


def actualizar_contacto(agenda):
    nombre = input("Me indica el nombre del contacto a actualizar: ")
    if nombre in agenda:
        nuevo_numero = input( "Por favor me indica el nuevo número: ")
        if es_valido_numero(nuevo_numero):
            agenda[nombre] = nuevo_numero
            print(f"Contacto {nombre} actualizado correctamente")
        else:
            print("Número de telefono no valid, debe ser numerico menor de 11 digitoso")
    else: 
        print(print(f"Contacto {nombre} No encontrado"))

def eliminar_contacto(agenda):
    nombre = input("Por favor indique el nombre del contacto a eliminar:  ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado correctamente")
    else:
        print(f"Contacto No encontrado")

def mostrar_todos_contactos(agenda):
    if agenda:
        print("\nLista de Contactos:")
        for nombre, numero in agenda.items():
            print(f"{nombre} : {numero}")
    else:
        print("No hay contactos en Agenda")
        
def main():
    agenda = {}
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            insertar_contacto(agenda)
        elif opcion == "2":
            buscar_contacto(agenda)
        elif opcion == "3":
            actualizar_contacto(agenda)
        elif opcion == "4":
            eliminar_contacto(agenda)
        elif opcion == "5":
            mostrar_todos_contactos(agenda)
        elif opcion == "6":
            print("Saliendo del Programa")
            break
        else:
            print("Intorduce una opcion valida")
            





if __name__ == "__main__":
    main()

