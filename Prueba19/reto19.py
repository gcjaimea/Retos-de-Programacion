from enum import Enum

class  Semana(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7



def mostrar_dia(d):
    
   try:
    dia_semana = Semana(d)
    print(f"Dia de la Semana: {dia_semana.name}")
   except ValueError:
      print("Error!!! Numero no valido ( 1 al 7)")


mostrar_dia(9)
