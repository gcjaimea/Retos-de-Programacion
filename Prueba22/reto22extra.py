import math
lista_estudiantes = [["Jesus Suarez","1984-09-03",[10,9,8,8.5]],
                   ["Jose Perez","1975-12-25", [9,6,8,6.5]],
                   ["Carlos Garcia", "1999-4-12",[10,10,10,8.5]]]

# Promedio de calificaciones por estudiante
promedios_estudiantes = list(map(lambda estudiante: (estudiante[0], sum(estudiante[2]) / len(estudiante[2])), lista_estudiantes))
print("Promedios de calificaciones:", promedios_estudiantes)

# Estudiantes con promedio >= 9
mejores_estudiantes = list(filter(lambda estudiante: (sum(estudiante[2]) / len(estudiante[2])) >= 9, lista_estudiantes))
mejores_estudiantes = list(map(lambda estudiante: estudiante[0], mejores_estudiantes))
print("Mejores estudiantes:", mejores_estudiantes)

# Estudiantes ordenados por fecha de nacimiento (más joven primero)
nacimientos_ordenados = sorted(lista_estudiantes, key=lambda estudiante: estudiante[1], reverse=True)
nacimientos_ordenados = list(map(lambda estudiante: estudiante[0], nacimientos_ordenados))
print("Estudiantes ordenados por nacimiento (más joven primero):", nacimientos_ordenados)

# Mayor calificación entre todos los estudiantes
mayor_calificacion = max(map(lambda estudiante: max(estudiante[2]), lista_estudiantes))
print("Mayor calificación entre todos los estudiantes:", mayor_calificacion)

# Verificar que todas las calificaciones estén entre 0 y 10
calificaciones_validas = all(map(lambda estudiante: all(0 <= calificacion <= 10 for calificacion in estudiante[2]), lista_estudiantes))
print("¿Todas las calificaciones son válidas?", calificaciones_validas)