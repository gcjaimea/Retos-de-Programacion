class Libro:
    def __init__(self, titulo, autor, contenido, paginas):
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
        self.paginas = paginas

    def imprimir_detalles(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nPaginas: {self.paginas}")

    def guardar_libro(self, nombre_archivo):
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(self.titulo + '\n')
            archivo.write(self.autor + '\n')
            archivo.write(self.contenido + '\n')
            archivo.write(self.paginas)

# Uso incorrecto
libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Contenido del libro...","400 paginas")
libro.imprimir_detalles()
libro.guardar_libro("libro.txt")


print("*************************************************************")
print(" Uso correcto")
print("*************************************************************")

class Libro:
    def __init__(self, titulo, autor, contenido, paginas):
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
        self.paginas = paginas

    def imprimir_detalles(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nPaginas: {self.paginas}")


class LibroPersistence:
    @staticmethod
    def guardar(libro, nombre_archivo):
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(libro.titulo + '\n')
            archivo.write(libro.autor + '\n')
            archivo.write(libro.contenido + '\n')
            archivo.write(libro.paginas)

# Uso correcto
libro = Libro("La Rebelion de las ratas", "Fernando Soto Aparicio", "Contenido del libro...","300 paginas")
libro.imprimir_detalles()

# Uso de una clase separada para la persistencia
LibroPersistence.guardar(libro, "libro1.txt")
