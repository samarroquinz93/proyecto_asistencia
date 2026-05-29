class Biblioteca:

    def __init__(self, nombre):

        self.nombre = nombre

        # Composición
        self.libros = []

        # Composición
        self.prestamos = []

    def agregar_libro(self, libro):

        self.libros.append(libro)

    def agregar_prestamo(self, prestamo):

        self.prestamos.append(prestamo)

    def mostrar_libros(self):

        print("\n===== LISTA DE LIBROS =====")

        for libro in self.libros:

            estado = "Disponible"

            if not libro.disponible:
                estado = "Prestado"

            print(f"{libro} | {estado}")