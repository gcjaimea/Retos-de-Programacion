#Excepciones con try y except
try:
    # Código que puede causar una excepción es la division por cero ya que da indeterminado
    resultado = 10 / 0
except ZeroDivisionError as error:
    # Código que se ejecuta si ocurre una excepción
    print(f"Error: {error}")

print("El programa continúa ejecutándose.")


# excepciones con else
try:
    resultado = 10 / 2
except ZeroDivisionError as error: # esto no se ejecuta porque no hay error!!
    print(f"Error: {error}")
else:
    print(f"Resultado: {resultado}") # el comando else se ejecuta si  try no va a generar una excepcion 

print("El programa continúa ejecutándose.")

# Excepciones con finally

try:
    resultado = 10 / 0
except ZeroDivisionError as error:  # No se ejecuta porque no hay excepcion
    print(f"Error: {error}")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Este bloque se ejecuta siempre.") # se ejecuta haya o no haya excepcion

print("El programa continúa ejecutándose.")

#************Extra*****************

def procesar_parametros(n1, n2):
    
    if type(n1) == str or type(n2) == str:
        raise TypeError ("Los parametros deben ser numeros") # Verifica si hay string
    elif n2 == 0:
        raise ZeroDivisionError("Division por cero!!!")  #Verifica si hay division por cero
    elif n1 /  n2 < 0:
        raise ValueError("No puede ser negtivo el resultado!!!") # Verifica si la division es negativa
    
    else:
        resultado = n1 / n2
        print(f"El resultado de la operacion es igal a : {resultado}")

    #resultado = n1/n2
    #print(f"resultado)



try:
    procesar_parametros(5,2)
except TypeError as e_type:
    print(f"TypeError: {e_type}")
except ZeroDivisionError as e_zero:
    print(f"ZeroDivisionError: {e_zero}")
except ValueError as e_value:
    print(f"ValueError: {e_value}")
else:
    print(f"El programa no ha dado errores!!!")
finally:
    print("Programa concluye sin detenerse!!!")
    
    