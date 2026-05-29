from datetime import datetime, timedelta

class Prestamo:

    def __init__(self, socio, libro):

        self.socio = socio
        self.libro = libro

        self.fecha_prestamo = datetime.now()

        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=7)

    def realizar_prestamo(self):

        if not self.socio.puede_prestar():

            print("\nEl socio ya tiene el límite de 2 libros")

            return

        if self.libro.disponible:

            self.libro.disponible = False

            self.socio.libros_prestados += 1

            # Guardar libro en lista del socio
            self.socio.libros.append(self.libro)

            print(f"\nLibro prestado a {self.socio.nombre}")

            print("Fecha préstamo:", self.fecha_prestamo.strftime("%d/%m/%Y"))

            print("Fecha devolución:", self.fecha_devolucion.strftime("%d/%m/%Y"))

        else:

            print("\nEl libro no está disponible")

    def devolver_libro(self):

        self.libro.disponible = True

        self.socio.libros_prestados -= 1

        # Eliminar libro de la lista del socio
        if self.libro in self.socio.libros:

            self.socio.libros.remove(self.libro)

        fecha_actual = datetime.now()

        # Multa automática
        if fecha_actual > self.fecha_devolucion:

            dias_tarde = (fecha_actual - self.fecha_devolucion).days

            multa = dias_tarde * 5

            self.socio.agregar_multa(multa)

            print(f"\nLibro devuelto con retraso")
            print(f"Multa generada: Q{multa}")

        else:

            print("\nLibro devuelto correctamente")