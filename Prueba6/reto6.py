
#Funcion recursiva para imprimir numeros del 100 al 0


def imprimir_descendente(n):
    if n < 0:        # condicion base: cuando n < 0 se detiene la recursion
        return
    print(n)
     # llamada recursiva
    imprimir_descendente(n-1) # llamada recursiva

imprimir_descendente(100)   


#Factorial de un  numero

def factorial(n):
    if n == 0:        
        return 1
    else:
        return n * factorial(n-1)
numero = 5    
print (f"factorial de {numero} es igual a: {factorial(numero)}") # 5*4*3*2*1 = 120

####  Extra!!!

#Sucesion de Fibonacci

def fibonacci(n):
    
    #Caso base: n + 0 y n+1
    if n == 0:
        return 0
    elif n== 1:
        return 1
    #Caso recursivo
    else:
        return fibonacci(n-1) + fibonacci (n-2)

posicion = 5

print(f"El elemento de la posicion {posicion} es igual a : {fibonacci(posicion)}") # 0,1,1,2,3,5
