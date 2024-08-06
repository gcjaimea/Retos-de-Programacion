#Crear la superclase animal

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
        def hacer_sonido(self):
             return f"El perro {self.nombre} dice: Guau Guau"
        
class Gato(Animal):
     def hacer_sonido(self):
          return f"El gato {self.nombre} dice Miau Miau"
     


def imprimir_sonido(animal):
     print(animal.hacer_sonido())


perro = Perro("Ringo")
gato = Gato("Minino")

imprimir_sonido(perro)
imprimir_sonido(gato)

# Extra

class Empleados:
     def __init__(self, id,nombre):
        self.id = id
        self.nombre = nombre

        
class Gerente(Empleados):     
     def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.empleados_a_cargo = []

     def agregar_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)

     def mostrar_informacion(self):
        print(f"Gerente [ID: {self.id}, Nombre: {self.nombre}]")
        print("Empleados a cargo:")
        for empleado in self.empleados_a_cargo:
            print(f"  - {empleado.nombre} (ID: {empleado.id})")


class GerenteDeProyectos(Empleados):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        
        self.proyectos_a_cargo = []

    def agregar_proyecto(self, proyecto):
        self.proyectos_a_cargo.append(proyecto)

    def mostrar_informacion(self):
        print(f"Gerente de Proyectos [ID: {self.id}, Nombre: {self.nombre}]")
        print("Proyectos a cargo:")
        for proyecto in self.proyectos_a_cargo:
            print(f"  - Proyecto: {proyecto}")

class Programador(Empleados):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

        self.lenguajes_programacion = []

    def agregar_lenguaje(self, lenguaje):
        self.lenguajes_programacion.append(lenguaje)

    def mostrar_informacion(self):
        print(f"Programador [ID: {self.id}, Nombre: {self.nombre}]")
        print("Lenguajes de programación:")
        for lenguaje in self.lenguajes_programacion:
            print(f"  - {lenguaje}")


# Crear instancias de empleados
gerente = Gerente(1, "Jorge")
gerente_proyectos = GerenteDeProyectos(2, "Camila")
programador1 = Programador(3, "Jose")
programador2 = Programador(4, "Victor")

# Agregar lenguajes de programación a los programadores
programador1.agregar_lenguaje("Python")
programador1.agregar_lenguaje("JavaScript")
programador2.agregar_lenguaje("Java")
programador2.agregar_lenguaje("C++")

# Agregar proyectos al gerente de proyectos
gerente_proyectos.agregar_proyecto("Proyecto Mi Casa")
gerente_proyectos.agregar_proyecto("Proyecto Drogueria Exito")

# Agregar empleados al gerente
gerente.agregar_empleado(gerente_proyectos)
gerente.agregar_empleado(programador1)
gerente.agregar_empleado(programador2)

# Mostrar información de cada empleado
print("Información del Gerente:")
gerente.mostrar_informacion()
print("\nInformación del Gerente de Proyectos:")
gerente_proyectos.mostrar_informacion()
print("\nInformación del Programador 1:")
programador1.mostrar_informacion()
print("\nInformación del Programador 2:")
programador2.mostrar_informacion()