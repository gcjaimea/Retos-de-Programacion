# Asignación de variables "por valor", se aplican a 
#tipo de datos inmutables (enteros, flotantes, cadenas y tuplas)

x = 10
y = x
y = 100
print(f"x = {x}   y = {y}") # asignación por valor   x= 10,  y = 100

cadena1 = "Jaime"
cadena2 = cadena1
cadena2 =  "Carlos"
print(f"cadena1 = {cadena1}   cadena2 = {cadena2}") # asignación por valor   cadena1 = "Jaime",  cadena2 = "Carlos"


#Asignación "por Referencia", se aplican a tipos de 
#datos mutables ( listas, diccionarios y conjuntos)

lista1 = [5, 6, 7, 8]
lista2 = lista1
lista2.append(9)
print(f"lista1 = {lista1}   lista2 = {lista2}") # asignación por valor   lista1 =[5,6,7,8,9] ,  lista2 = [5,6,7,8,9]


#Forma para evitar la signacion por referencia
#se debe usar 'copy()' iportarla desde python

import copy
lista3 = [1, 2, 3, 4]
lista4 = copy.copy(lista3)
lista4.append(9)
print(f"lista3 = {lista3}   lista3 = {lista4}") # asignación por valor   lista3 =[1,2,3,4] ,  lista2 = [1,2,3,4,9]



#Dificultad Extra

nume,numf = asignacion_por_valor(numc,numd)
print(f"{numc}, {numd}")
print(f"{nume}, {numf}")
