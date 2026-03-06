# Clase que representa un libro dentro del sistema

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa una tupla para almacenar título y autor (inmutable)
        self._titulo_autor = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    # Getters para acceder a los atributos
    def obtener_titulo(self):
        return self._titulo_autor[0]

    def obtener_autor(self):
        return self._titulo_autor[1]

    def obtener_categoria(self):
        return self._categoria

    def obtener_isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self.obtener_titulo()} - {self.obtener_autor()} | Categoría: {self._categoria} | ISBN: {self._isbn}"