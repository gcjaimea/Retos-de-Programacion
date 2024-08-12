# Definimos una función callback que simplemente imprime un mensaje
def my_callback():
    print("Callback ejecutado!")

# Definimos una función que recibe otra función como argumento
def perform_task(task, callback):
    print("Ejecutando tarea...")
    task()
    # Llamamos al callback después de completar la tarea
    callback()

# Definimos la tarea que queremos realizar
def my_task():
    print("Tarea realizada.")

# Llamamos a perform_task pasando la tarea y el callback
perform_task(my_task, my_callback)