#Iteracion utilizando bucle "for"

print("Iteracion usando el bucle for:")
for i in range(1,11):   
    print(i)


#Iteracion usando bucle "while"

n = 1
print("Iteracion usando el bucle while:")
while n < 11:    
    print(n)
    n += 1 

#list comprehension con bucle "for" 
print("Iteracion usando  list comprehension:")
[print(k) for k in range(1,11)]


# Imprimir números del 1 al 10 usando una funcion generadora

print("Iteracion usando funcion generadora: ")
def generar_numeros(limite):
    i = 1
    while i <= limite:
        yield i
        i += 1

for numero in generar_numeros(10):   
    print(numero)

# Imprimir números del 1 al 10 usando la funcion map()
print("Iteracion usando funcion map: ")
list(map(lambda x: print(x), range(1, 11)))


# Imprimir números del 1 al 10 en una línea usando join
print("Iteracion usando funcion join: ")
print(" ".join(str(i) for i in range(1, 11)))


import itertools

# Imprimir números del 1 al 10 usando funcion itertools, se usa para iteraciona indefinidas
print("Iteracion usando funcion intertools: ")
for i in itertools.count(1):
    if i > 10:
        break
    print(i)