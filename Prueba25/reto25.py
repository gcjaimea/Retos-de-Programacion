import logging

# Configurar el sistema de logging
logging.basicConfig(level=logging.DEBUG,  # Establece el nivel mínimo de severidad
                    format='%(asctime)s - %(levelname)s - %(message)s')  # Formato del mensaje
# Mensajes de logging en diferentes niveles de severidad
logging.debug("Este es un mensaje de depuración (DEBUG)")
logging.info("Este es un mensaje informativo (INFO)")
logging.warning("Este es un mensaje de advertencia (WARNING)")
logging.error("Este es un mensaje de error (ERROR)")
logging.critical("Este es un mensaje crítico (CRITICAL)")

logging.basicConfig(filename='app.log', 
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Mensajes de logging en diferentes niveles de severidad
logging.debug("Este es un mensaje de depuración (DEBUG)")
logging.info("Este es un mensaje informativo (INFO)")
logging.warning("Este es un mensaje de advertencia (WARNING)")
logging.error("Este es un mensaje de error (ERROR)")
logging.critical("Este es un mensaje crítico (CRITICAL)")