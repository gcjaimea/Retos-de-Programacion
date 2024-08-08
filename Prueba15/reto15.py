import asyncio
from datetime import datetime

async def tarea_asincrona(nombre, duracion):
    # Imprimir cuándo empieza
    inicio = datetime.now().strftime("%H:%M:%S")
    print(f"Inicio de '{nombre}' a las {inicio}. Duración estimada: {duracion} segundos.")
    
    # Esperar el tiempo especificado
    await asyncio.sleep(duracion)
    
    # Imprimir cuándo termina
    fin = datetime.now().strftime("%H:%M:%S")
    print(f"Fin de '{nombre}' a las {fin}.")

async def main():
    # Ejecutar múltiples tareas asíncronas
    tareas = [
        tarea_asincrona("Tarea 1", 5),
        tarea_asincrona("Tarea 2", 10),
        tarea_asincrona("Tarea 3", 15)
    ]
    
    # Esperar a que todas las tareas se completen
    await asyncio.gather(*tareas)

# Ejecutar el evento principal
asyncio.run(main())