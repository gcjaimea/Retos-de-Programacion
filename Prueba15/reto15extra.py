import asyncio
from datetime import datetime

# Definir las funciones asíncronas A, B, C, y D
async def funcion_C():
    print(f"Inicio de la función C a las {datetime.now().strftime('%H:%M:%S')}")
    await asyncio.sleep(3)
    print(f"Final de la función C a las {datetime.now().strftime('%H:%M:%S')}")

async def funcion_B():
    print(f"Inicio de la función B a las {datetime.now().strftime('%H:%M:%S')}")
    await asyncio.sleep(2)
    print(f"Final de la función B a las {datetime.now().strftime('%H:%M:%S')}")

async def funcion_A():
    print(f"Inicio de la funcion A a las {datetime.now().strftime('%H:%M:%S')}")
    await asyncio.sleep(1)
    print(f"Final de la función A a las {datetime.now().strftime('%H:%M:%S')}")

async def funcion_D():
    print(f"Inicio de la función D a las {datetime.now().strftime('%H:%M:%S')}")
    await asyncio.sleep(1)
    print(f"Final de la función D a las {datetime.now().strftime('%H:%M:%S')}")

async def main():
    # Ejecutar las funciones C, B y A en paralelo
    tareas = [
        funcion_C(),
        funcion_B(),
        funcion_A()
    ]
    
    # Esperar a que las funciones C, B y A se completen
    await asyncio.gather(*tareas)
    
    # Ejecutar la función D después de que C, B y A hayan terminado
    await funcion_D()

# Ejecutar el evento principal
asyncio.run(main())