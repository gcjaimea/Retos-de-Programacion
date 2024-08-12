
#Creacion del Decorador
def contar_llamadas(func):
    func.contador = 0  # Inicializa un contador en la función

    def envoltura(*args, **kwargs):
        func.contador += 1  # Incrementa el contador cada vez que se llama a la función
        print(f"La función '{func.__name__}' ha sido llamada {func.contador} veces.")
        return func(*args, **kwargs)  # Llama a la función original

    return envoltura
@contar_llamadas
def saludar(nombre):
    print(f"Hola, {nombre}!")

@contar_llamadas
def sumar(a,b):
    return a+b

# Llamadas a la función decorada
saludar("Jesus")
saludar("Pedro")
saludar("Luis")
sumar(3,2)
sumar(8,10)