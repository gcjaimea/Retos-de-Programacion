### Refactorizando cumpliendo con el SRP
class Libro:
    def __init__(self, titulo, autor, copias_disponibles,):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles


class Usuario:
    def __init__(self, nombre, id_usuario, email):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.email = email


class RegistroLibros:
    def __init__(self):
        self.libros = {}

    def registrar_libro(self, titulo, autor, copias_disponibles):
        if titulo not in self.libros:
            self.libros[titulo] = Libro(titulo, autor, copias_disponibles)
            print(f"Libro '{titulo}' registrado con éxito.")
        else:
            print(f"El libro '{titulo}' ya está registrado.")

    def obtener_libro(self, titulo):
        return self.libros.get(titulo, None)


class RegistroUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre, id_usuario, email):
        if id_usuario not in self.usuarios:
            self.usuarios[id_usuario] = Usuario(nombre, id_usuario, email)
            print(f"Usuario '{nombre}' registrado con éxito.")
        else:
            print(f"El usuario con identificación '{id_usuario}' ya está registrado.")

    def obtener_usuario(self, id_usuario):
        return self.usuarios.get(id_usuario, None)


class ProcesamientoPrestamos:
    def __init__(self, registro_libros, registro_usuarios):
        self.registro_libros = registro_libros
        self.registro_usuarios = registro_usuarios
        self.prestamos = {}

    def prestar_libro(self, identificacion_usuario, titulo_libro):
        usuario = self.registro_usuarios.obtener_usuario(identificacion_usuario)
        libro = self.registro_libros.obtener_libro(titulo_libro)

        if usuario is None:
            print("Usuario no registrado.")
            return

        if libro is None:
            print("Libro no disponible.")
            return

        if libro.copias_disponibles > 0:
            libro.copias_disponibles -= 1
            self.prestamos.setdefault(identificacion_usuario, []).append(titulo_libro)
            print(f"Libro '{titulo_libro}' prestado a {usuario.nombre}.")
        else:
            print("No hay copias disponibles.")

    def devolver_libro(self, identificacion_usuario, titulo_libro):
        if identificacion_usuario in self.prestamos and titulo_libro in self.prestamos[identificacion_usuario]:
            self.prestamos[identificacion_usuario].remove(titulo_libro)
            libro = self.registro_libros.obtener_libro(titulo_libro)
            if libro:
                libro.copias_disponibles += 1
            print(f"Libro '{titulo_libro}' devuelto por {self.registro_usuarios.obtener_usuario(identificacion_usuario).nombre}.")
        else:
            print("Devolución no válida.")


# Uso del sistema refactorizado
registro_libros = RegistroLibros()
registro_usuarios = RegistroUsuarios()
procesamiento_prestamos = ProcesamientoPrestamos(registro_libros, registro_usuarios)

# Registrar libros
registro_libros.registrar_libro("La Rebelion de las ratas", "fernando Soto Aparicio", 5)
registro_libros.registrar_libro("El Coronel no tiene quien le escriba", "Gabriel Garcia Marquez", 3)

# Registrar usuarios
registro_usuarios.registrar_usuario("Jose Pérez", "12345", "jose.perez@example.com")
registro_usuarios.registrar_usuario("María Lopez", "6789", "maria.lopez@example.com")

# Prestar libros
procesamiento_prestamos.prestar_libro("12345", "La Rebelion de las ratas")
procesamiento_prestamos.prestar_libro("6789", "El Coronel no tiene quien le escriba")

# Devolver libros
procesamiento_prestamos.devolver_libro("12345", "La Rebelion de las ratas")