from persona import Persona

class Socio(Persona):

    def __init__(self, nombre, carnet):

        super().__init__(nombre)

        self.carnet = carnet

        # Encapsulación
        self.__multas = 0

        self.libros_prestados = 0

        # Lista de libros prestados
        self.libros = []

    def agregar_multa(self, cantidad):

        self.__multas += cantidad

    def ver_multas(self):

        return self.__multas

    def puede_prestar(self):

        return self.libros_prestados < 2

    # Override
    def mostrar_info(self):

        print(f"\n===== INFORMACIÓN DEL SOCIO =====")

        print(f"Nombre: {self.nombre}")
        print(f"Carnet: {self.carnet}")
        print(f"Libros prestados: {self.libros_prestados}")
        print(f"Multas pendientes: Q{self.__multas}")

        print("\nLibros prestados:")

        if len(self.libros) == 0:

            print("No tiene libros prestados")

        else:

            for libro in self.libros:

                print(f"- {libro.titulo}")