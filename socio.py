from persona import Persona

class Socio(Persona):

    def __init__(self, nombre, carnet):

        super().__init__(nombre)

        self.carnet = carnet

        # Encapsulación
        self.__multas = 0

        self.libros_prestados = 0

    def agregar_multa(self, cantidad):

        self.__multas += cantidad

    def ver_multas(self):

        return self.__multas

    def puede_prestar(self):

        return self.libros_prestados < 2

    def mostrar_info(self):

        print(f"\nSocio: {self.nombre}")
        print(f"Carnet: {self.carnet}")
        print(f"Libros prestados: {self.libros_prestados}")
        print(f"Multas pendientes: Q{self.__multas}")