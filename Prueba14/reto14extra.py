from datetime import datetime

fecha_cumpleaños = datetime(1964,9,9,18,30,0)


fecha_cumpleaños_formateada1 = fecha_cumpleaños.strftime("%d-%m-%Y %H:%M:%S")
fecha_cumpleaños_formateada2 = fecha_cumpleaños.strftime("%d-%m-%Y %I:%M:%S: %p")
fecha_cumpleaños_formateada3 = fecha_cumpleaños.strftime("%A-%d-%b-%Y %H:%M:%S")
fecha_cumpleaños_formateada4 = fecha_cumpleaños.strftime("%Y-%m-%A-%d %H:%M:%S")
fecha_cumpleaños_formateada5 = fecha_cumpleaños.strftime("%Y-%m-%A-%d %I:%M:%S: %p")
fecha_cumpleaños_formateada6 = fecha_cumpleaños.strftime("%d-%b-%Y %I:%M:%S: %p")
fecha_cumpleaños_formateada7 = fecha_cumpleaños.strftime("%d-%b-%Y %H:%M:%S")
fecha_cumpleaños_formateada8 = fecha_cumpleaños.strftime("%d/%m/%Y %I:%M:%S: %p")
fecha_cumpleaños_formateada9 = fecha_cumpleaños.strftime("%d/%m/%Y %H:%M:%S")
fecha_cumpleaños_formateada10 = fecha_cumpleaños.strftime("%d/%m/%Y %H:%M:%S.%f")

print(f"Fecha Cumpleaños sin formatear: {fecha_cumpleaños}") # 1964-09-09 18:30:00
print(f"Fecha Cumpleaños formateada1 : {fecha_cumpleaños_formateada1}") # 09-09-1964 18:30:00
print(f"Fecha Cumpleaños formateada2 : {fecha_cumpleaños_formateada2}") # 09-09-1964 06:30:00: PM
print(f"Fecha Cumpleaños formateada3 : {fecha_cumpleaños_formateada3}") # Wednesday-09-Sep-1964 18:30:00
print(f"Fecha Cumpleaños formateada4 : {fecha_cumpleaños_formateada4}") # 1964-09-Wednesday-09 18:30:00
print(f"Fecha Cumpleaños formateada5 : {fecha_cumpleaños_formateada5}") # 1964-09-Wednesday-09 06:30:00: PM
print(f"Fecha Cumpleaños formateada6 : {fecha_cumpleaños_formateada6}") # 09-Sep-1964 06:30:00: PM
print(f"Fecha Cumpleaños formateada7 : {fecha_cumpleaños_formateada7}") # 09-Sep-1964 18:30:00
print(f"Fecha Cumpleaños formateada8 : {fecha_cumpleaños_formateada8}") # 09/09/1964 06:30:00: PM
print(f"Fecha Cumpleaños formateada9 : {fecha_cumpleaños_formateada9}") # 09/09/1964 18:30:00
print(f"Fecha Cumpleaños formateada10 : {fecha_cumpleaños_formateada10}") # 09/09/1964 18:30:00.000000

