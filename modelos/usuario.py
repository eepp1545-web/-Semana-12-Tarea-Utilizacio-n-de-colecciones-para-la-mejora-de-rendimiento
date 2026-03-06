# Clase que representa un usuario de la biblioteca

class Usuario:

    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario

        # Lista para almacenar los libros prestados
        self._libros_prestados = []

    def obtener_id(self):
        return self._id_usuario

    def obtener_nombre(self):
        return self._nombre

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self._libros_prestados:
            if libro.obtener_isbn() == isbn:
                self._libros_prestados.remove(libro)
                return libro
        return None

    def obtener_libros(self):
        return self._libros_prestados