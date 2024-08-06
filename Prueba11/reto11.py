import os
def craer_fichero(nombre):
    with open(nombre, "w",encoding='utf-8') as escr:
        escr.write("Jaime Antonio Gonzalez Castellanos\n 59 años\n Python\n")
        print(f"Fichero: {nombre} creado")
       

def main():
    nombre_fichero = "gcjaimea.txt"
    craer_fichero(nombre_fichero)


FICHERO = 'ventas_productos.txt'

def mostrar_menu():
    print("\nMenú de Gestión de Ventas")
    print("1. Añadir producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Calcular venta total")
    print("6. Calcular venta por producto")
    print("7. Salir")

def añadir_producto():
    nombre_producto = input("Nombre del producto: ")
    cantidad_vendida = int(input("Cantidad vendida: "))
    precio = float(input("Precio del producto: "))
    with open(FICHERO, 'a', encoding='utf-8') as file:
        file.write(f"{nombre_producto}, {cantidad_vendida}, {precio}\n")
    print("Producto añadido.")

def consultar_productos():
    if not os.path.exists(FICHERO):
        print("No hay productos registrados.")
        return

    with open(FICHERO, 'r', encoding='utf-8') as file:
        productos = file.readlines()
        if not productos:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print(producto.strip())

def actualizar_producto():
    if not os.path.exists(FICHERO):
        print("No hay productos registrados.")
        return

    nombre = input("Nombre del producto a actualizar: ")
    with open(FICHERO, 'r', encoding='utf-8') as file:
        productos = file.readlines()

    actualizado = False
    with open(FICHERO, 'w', encoding='utf-8') as file:
        for producto in productos:
            datos = producto.strip().split(", ")
            if datos[0] == nombre:
                cantidad = int(input("Nueva cantidad vendida: "))
                precio = float(input("Nuevo precio: "))
                file.write(f"{nombre}, {cantidad}, {precio}\n")
                actualizado = True
            else:
                file.write(producto)
    
    if actualizado:
        print("Producto actualizado.")
    else:
        print("Producto no encontrado.")

def eliminar_producto():
    if not os.path.exists(FICHERO):
        print("No hay productos registrados.")
        return

    nombre_producto = input("Nombre del producto a eliminar: ")
    with open(FICHERO, 'r', encoding='utf-8') as file:
        productos = file.readlines()

    eliminado = False
    with open(FICHERO, 'w', encoding='utf-8') as file:
        for producto in productos:
            datos = producto.strip().split(", ")
            if datos[0] != nombre_producto:
                file.write(producto)
            else:
                eliminado = True
    
    if eliminado:
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def calcular_venta_total():
    if not os.path.exists(FICHERO):
        print("No hay productos registrados.")
        return

    total = 0
    with open(FICHERO, 'r', encoding='utf-8') as file:
        for producto in file:
            datos = producto.strip().split(", ")
            cantidad_vendida = int(datos[1])
            precio = float(datos[2])
            total += cantidad_vendida * precio

    print(f"Venta total: {total:.2f}")

def calcular_venta_por_producto():
    if not os.path.exists(FICHERO):
        print("No hay productos registrados.")
        return

    ventas_por_producto = {}
    with open(FICHERO, 'r', encoding='utf-8') as file:
        for producto in file:
            datos = producto.strip().split(", ")
            nombre_producto = datos[0]
            cantidad_vendida = int(datos[1])
            precio = float(datos[2])
            ventas_por_producto[nombre_producto] = cantidad_vendida * precio

    for nombre_producto, venta in ventas_por_producto.items():
        print(f"{nombre_producto}: {venta:.2f}")

def salir():
    if os.path.exists(FICHERO):
        os.remove(FICHERO)
    print("Archivo de ventas borrado. Saliendo del programa.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            calcular_venta_total()
        elif opcion == '6':
            calcular_venta_por_producto()
        elif opcion == '7':
            salir()
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()





