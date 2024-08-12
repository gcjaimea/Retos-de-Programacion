class Singleton:
    _instance = None  # Atributo de clase para almacenar la instancia única

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Si no existe una instancia, se crea y se almacena
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, 'initialized'):  # Verifica si ya ha sido inicializado
            self.value = value
            self.initialized = True

    def display_value(self):
        print(f"The value is: {self.value}")

# Uso del Singleton
singleton1 = Singleton("agua")
singleton2 = Singleton("agua")

singleton1.display_value()  # Imprime: The value is: agua
singleton2.display_value()  # Imprime: The value is: agua

# Verificación de que ambas variables apuntan a la misma instancia
print(singleton1 is singleton2)  # Imprime: True