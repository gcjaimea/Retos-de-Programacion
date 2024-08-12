import time

def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()  # Registra el tiempo de inicio
        resultado = funcion(*args, **kwargs)  # Ejecuta la función original
        fin = time.time()  # Registra el tiempo de finalización
        print(f"Tiempo de ejecución de {funcion.__name__}: {fin - inicio:.4f} segundos")
        return resultado  # Devuelve el resultado de la función original
    return envoltura  # Devuelve la función envuelta

@medir_tiempo
def suma_lenta(a, b):
    time.sleep(1.5)  # Simula una operación lenta
    return a + b

@medir_tiempo
def restar(a, b):
    time.sleep(0.5)  # Simula una operación lenta
    return a * b

resultado_suma = suma_lenta(3, 4)
print(f"Resultado de la suma: {resultado_suma}")

resultado_resta = restar(5, 6)
print(f"Resultado de la resta: {resultado_resta}")


#  Otro decorador generico
print("************************************************")

print("OTRO DECORADOR GENERICO") 

print("************************************************")

def verificar_tipos(*tipos_esperados):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for (arg, tipo_esperado) in zip(args, tipos_esperados):
                if not isinstance(arg, tipo_esperado):
                    raise TypeError(f"El argumento {arg} no es del tipo {tipo_esperado}")
            return func(*args, **kwargs)  # Llama a la función original
        return envoltura
    return decorador

@verificar_tipos(int, int)
def sumar(a, b):
    return a + b

@verificar_tipos(str, str)
def concatenar(cadena1, cadena2):
    return cadena1 + cadena2

# Esta llamada será exitosa
resultado_suma = sumar(3, 4)
print(f"Resultado de la suma: {resultado_suma}")

# Esta llamada lanzará un TypeError
try:
    sumar(3, "4")
except TypeError as e:
    print(e)

# Esta llamada será exitosa
resultado_concatenacion = concatenar("Hola, ", "mundo!")
print(f"Resultado de la concatenación: {resultado_concatenacion}")

# Esta llamada lanzará un TypeError
try:
    concatenar("Hola, ", 5)
except TypeError as e:
    print(e)

