def realizar_operacion(operacion, x, y):
    return operacion(x, y)

# Ejemplos de funciones que podemos pasar como argumentos
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b



# Uso de la función de orden superior
resultado_suma = realizar_operacion(suma, 10, 2)  # suma = 12
resultado_resta = realizar_operacion(resta, 10, 2)  # resta = 8
resultado_multiplicacion = realizar_operacion(multiplicacion, 10, 2) # multiplicacion = 20
resultado_division = realizar_operacion(division, 10, 2) # Division = 5

print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la resta: {resultado_resta}")
print(f"Resultado de la multiplicacion: {resultado_multiplicacion}")
print(f"Resultado de la division: {resultado_division}")

print("***********************************************************************")


# Uso de la función de orden superior que devuelve otra funcion

def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

duplicar = crear_multiplicador(2)  # Crea una función que duplica el valor
cuadruplicar = crear_multiplicador(4)  # Crea una función que triplica el valor

resultado_duplicar = duplicar(10)  # duplicar =  20
resultado_triplicar = cuadruplicar(10)  # cuadruplicar = 40

print("Resultado de duplicar 10:", resultado_duplicar)
print("Resultado de cuadruplicar 10:", resultado_triplicar)



print("***********************************************************************")
# Uso de map para aplicar una función a cada elemento de una lista
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))

# Uso de filter para filtrar elementos de una lista
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Cuadrados:", cuadrados)  # Debería devolver [1, 4, 9, 16, 25]
print("Números pares:", numeros_pares)  # Debería devolver [2, 4]