import copy

lista1 = ["naranja", "uva", "banana", "manzana"]
print(f"lista 1 original: {lista1}")

lista2 =["fresa", "tamarindo", "mango"]
print(f"lista 1 original: {lista2}")

# Agregar un elemento a final
lista1n = copy.copy(lista1)
lista1n.append("papaya")
print(f"lista1 con un elemento agregado al final: {lista1n}")

#Agregar un elemento al inicio
lista1n2 = copy.copy(lista1)
lista1n2.insert(0,"guanabana")
print(f"lista1 con un elemento agregado al inicio: {lista1n2}")

#Agregar varios elementos al final
lista1n3 = lista1 + lista2
print(f"lista1 con varios elementos agregados al final: {lista1n3}")
#otra forma
lista1n3a =copy.copy(lista1)
lista1n3a.extend(lista2)
print(f"lista1 con varios elementos agregados al finalusando extend() : {lista1n3a}")

# Agregar varios elementos al inicio
lista1n4 = lista2 + lista1
print(f"lista1 con varios elementos agregados al inicio: {lista1n4}")
#otra forma
lista1n4a = copy.copy(lista1)
lista1n4a[:0] = lista2
print(f"lista1 con varios elementos agregados al inicio usando slicing: {lista1n4a}")


