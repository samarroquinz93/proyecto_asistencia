from libro import Libro
from socio import Socio
from prestamo import Prestamo
from biblioteca import Biblioteca

# Crear biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# =========================
# CREAR LIBROS
# =========================

libro1 = Libro("Harry Potter", "Rowling")
libro2 = Libro("Caperucita", "Hermanos Grimm")
libro3 = Libro("Dracula", "Bram Stoker")
libro4 = Libro("Pinocho", "Carlo Collodi")
libro5 = Libro("Moby Dick", "Melville")
libro6 = Libro("Hamlet", "Shakespeare")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)
biblioteca.agregar_libro(libro6)

# Crear socio
socio1 = Socio("Saul", "2026-01")

# =========================
# MENÚ
# =========================

while True:

    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Ver libros")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Ver multas")
    print("5. Ver información del socio")
    print("6. Salir")

    opcion = input("\nSeleccione una opción: ")

    # VER LIBROS
    if opcion == "1":

        biblioteca.mostrar_libros()

    # PRESTAR LIBRO
    elif opcion == "2":

        biblioteca.mostrar_libros()

        titulo = input("\nIngrese el título del libro: ")

        encontrado = False

        for libro in biblioteca.libros:

            if libro.titulo.lower() == titulo.lower():

                prestamo = Prestamo(socio1, libro)

                prestamo.realizar_prestamo()

                if not libro.disponible:
                    biblioteca.agregar_prestamo(prestamo)

                encontrado = True

                break

        if not encontrado:
            print("\nLibro no encontrado")

    # DEVOLVER LIBRO
    elif opcion == "3":

        titulo = input("\nIngrese el título del libro a devolver: ")

        encontrado = False

        for prestamo in biblioteca.prestamos:

            if prestamo.libro.titulo.lower() == titulo.lower():

                if prestamo.libro.disponible == False:

                    prestamo.devolver_libro()

                    encontrado = True

                    break

        if not encontrado:
            print("\nEse libro no está prestado")

    # VER MULTAS
    elif opcion == "4":

        print(f"\nMultas pendientes: Q{socio1.ver_multas()}")

    # VER INFORMACIÓN
    elif opcion == "5":

        socio1.mostrar_info()

    # SALIR
    elif opcion == "6":

        print("\nSaliendo del sistema...")

        break

    else:

        print("\nOpción inválida")