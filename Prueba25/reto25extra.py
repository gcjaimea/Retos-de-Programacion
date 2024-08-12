import logging
import time

# Configurar el sistema de logging
# Crear un manejador para el archivo de log con codificación UTF-8
file_handler = logging.FileHandler('tareas.log', encoding='utf-8')

# Configurar el formato del log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Configurar el logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

class GestorDeTareas:
    def __init__(self):
        self.tareas = {}

    def añadir_tarea(self, nombre, descripcion):
        inicio = time.time()
        if nombre in self.tareas:
            logging.warning(f"La tarea '{nombre}' ya existe. No se ha añadido.")
        else:
            self.tareas[nombre] = descripcion
            logging.info(f"Tarea '{nombre}' añadida con éxito.")
        fin = time.time()
        logging.debug(f"Tiempo de ejecución de 'añadir_tarea': {fin - inicio:.4f} segundos.")

    def eliminar_tarea(self, nombre):
        inicio = time.time()
        if nombre in self.tareas:
            del self.tareas[nombre]
            logging.info(f"Tarea '{nombre}' eliminada con éxito.")
        else:
            logging.error(f"La tarea '{nombre}' no existe. No se pudo eliminar.")
        fin = time.time()
        logging.debug(f"Tiempo de ejecución de 'eliminar_tarea': {fin - inicio:.4f} segundos.")

    def listar_tareas(self):
        inicio = time.time()
        if self.tareas:
            for nombre, descripcion in self.tareas.items():
                print(f"Tarea: {nombre} - Descripción: {descripcion}")
            logging.info("Listado de tareas completado.")
        else:
            logging.warning("No hay tareas para listar.")
        fin = time.time()
        logging.debug(f"Tiempo de ejecución de 'listar_tareas': {fin - inicio:.4f} segundos.")

# Ejemplo de uso del GestorDeTareas
gestor = GestorDeTareas()

# Añadir tareas
gestor.añadir_tarea("Comprar carne", "Comprar carne en la carniceria mas cercana.")
gestor.añadir_tarea("Hacer comida", "Hacer comida en casa.")
gestor.añadir_tarea("Imprimir tarea", "Imprimir 3 trabajos de investigacion")

# Listar tareas
gestor.listar_tareas()

# Eliminar una tarea
gestor.eliminar_tarea("Hacer comida")

# Intentar eliminar una tarea inexistente
gestor.eliminar_tarea("Imprimir tarea")

# Listar tareas de nuevo
gestor.listar_tareas()