'''
Crea ejemplos de funciones básicas que representen las diferentes
*   posibilidades del lenguaje:
*   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
'''

# Funcion sin parametros ni retornos
def saludar():
    print("Hola")

saludar()


#Funcion con parametros:
def saludar_nombre(nombre):
    print("Hola ", nombre)

saludar_nombre("Jaime")

#Funcion con varios parametros y retorno
def saludar_completo(nombre, apellido): 
    return f"Hola {nombre} {apellido}"

saludo =saludar_completo("Jaime" , "Gonzalez")
print(saludo)


def sumar(n1,n2):
    return n1+n2

suma = sumar(1,2)
print(suma)



def operaciones_matematicas(t, n1, n2):
    if t.lower() == "s":
        def sumar(n1, n2):
            return n1 + n2
        return sumar(n1, n2)
    elif t.lower() == "r":
        def restar(n1, n2):
            return n1 - n2
        return restar(n1, n2)
    elif t.lower() == "m":
        def multiplicar(n1, n2):
            return n1 * n2
        return multiplicar(n1, n2)
    elif t.lower() == "d":
        def dividir(n1, n2):
            return n1 / n2
        return dividir(n1, n2)
    else:
        return None

operacion = operaciones_matematicas("M", 2, 3)

print(operacion)



#Ejemplo de variable local y Variable Global

variable_global = 5

def variable_local():
    variable_local1 = variable_global + 1
    print(variable_local1)
c = variable_local()

#nuevo_numero = variable_local + 3 Da error...no reconoce el valor de la variable local
print(variable_global)

#print(nuevo_numero)   # No es posible accesar a una variable local!!



# Dificultad Extra

# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.

cad1 = "Jaime"
cad2 = "Carlos"
            
print("aqui!!!!")
def retornar(cad1,cad2):
    count = 0
    for i in range (1,101):
        if i % 3 ==0 and i %5 == 0:
            print(cad1 + cad2)
        elif i % 3 == 0:
            print(cad1)
        elif i % 5 == 0:
            print(cad2)
        else:
            print(i)
            count +=1
    return count            
        

print(retornar(cad1,cad2))






