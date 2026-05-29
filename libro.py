class Libro:

    def __init__(self, titulo, autor):

        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}')"