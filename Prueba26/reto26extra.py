class Library:
    def __init__(self):
        self.reg_libros = {}
        self.reg_usuarios = {}
        self.prest_libros = {}

    #Registrar Libros
    def registrar_libros(self, titulo_libro, autor, copias_disponibles):
        self.reg_libros[titulo_libro] = {
            "autor": autor,
            "Número de copias disponibles": copias_disponibles
        }

    #Registrar usuario
    def registrar_usuarios(self, nombre, id_usuario, email):
        self.reg_usuarios[id_usuario] ={
            "Nombre completo": nombre,
            "Correo": email
        }

    #Realizar Operacones
    def prestar_libros(self, id_usuario, titulo_libro):
        if id_usuario not in self.reg_usuarios:
            print("Usuario No registrado")
            return
        
        if self.reg_libros[titulo_libro]["Número de copias disponibles"] > 0:
            self.reg_libros[titulo_libro]["Número de copias disponibles"] -= 1
            self.prest_libros.setdefault(id_usuario, []).append(titulo_libro)
            print(f"Libro '{titulo_libro}' prestado a {self.reg_usuarios[id_usuario]['Nombre completo']}.")
        else:
            print("No hay copias disponibles.")

    # Procesar retorno de libros
    def devolver_libro(self, id_usuario, titulo_libro):
        if id_usuario in self.prest_libros and titulo_libro in self.prest_libros[id_usuario]:
            self.prest_libros[id_usuario].remove(titulo_libro)
            self.reg_libros[titulo_libro]["Número de copias disponibles"] += 1
            print(f"Libro '{titulo_libro}' devuelto por {self.reg_usuarios[id_usuario]['Nombre completo']}.")
        else:
            print("Devolución no válida.")

# Crear una instancia de la biblioteca
biblioteca = Library()

# Registrar un usuario
biblioteca.registrar_usuarios("Jorge Cruz", "12345", "jorgecruz@gmail.com")

# Registrar un libro
biblioteca.registrar_libros("Cien años de Soledad", "Gabriel Garcia Marquez", 5)

# Prestar un libro
biblioteca.prestar_libros("12345", "Cien años de Soledad")

# Devolver un libro
biblioteca.devolver_libro("12345", "Cien años de Soledad")