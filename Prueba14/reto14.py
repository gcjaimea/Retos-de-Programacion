from datetime import datetime



#crear fecha especifica
fechaHora_nacimiento = datetime(1964, 9, 9, 15, 19, 44)
print(f"Fecha y hora de nacimiento:  {fechaHora_nacimiento}")    #formato: Y - M -  D - H - M - S


# Obtener fecha y hora actual
fechaHora_actual =datetime.now()
print (f"Fecha y Hora actual: {fechaHora_actual}") #formato: Y - M -  D - H - M - S

# Cambiar formato
fecha_formateada_nacimiento = fechaHora_nacimiento.strftime("%d-%m-%Y %H:%M:%S")
print(f"Fecha y Hora de nacimiento en nuevo formato: {fecha_formateada_nacimiento}")

fecha_formateada_actual = fechaHora_actual.strftime("%d-%m-%Y %H:%M:%S")
print(f"Fecha y Hora actual en nuevo formato: {fecha_formateada_actual}")


#Calculo de la edad:
edad_year = fechaHora_actual.year -fechaHora_nacimiento.year - ((fechaHora_actual.month, fechaHora_actual.day) < (fechaHora_nacimiento.month, fechaHora_nacimiento.day))
print(edad_year)


 