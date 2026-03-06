from modelos.libro import Libro
from modelos.usuario import Usuario


# Clase que gestiona toda la lógica del sistema
class BibliotecaServicio:

    def __init__(self):

        # Diccionario para almacenar libros disponibles
        # Clave: ISBN
        # Valor: objeto Libro
        self.libros = {}

        # Diccionario de usuarios registrados
        self.usuarios = {}

        # Conjunto para mantener IDs únicos de usuarios
        self.ids_usuarios = set()

    # ---------------- LIBROS ----------------

    def añadir_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro
        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ---------------- USUARIOS ----------------

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El usuario ya existe.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado correctamente.")

    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ---------------- PRÉSTAMOS ----------------

    def prestar_libro(self, id_usuario, isbn):

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        libro = self.libros.pop(isbn)
        usuario = self.usuarios[id_usuario]

        usuario.prestar_libro(libro)

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        libro = usuario.devolver_libro(isbn)

        if libro:
            self.libros[isbn] = libro
            print("Libro devuelto correctamente.")
        else:
            print("El usuario no tiene ese libro.")

    # ---------------- BÚSQUEDAS ----------------

    def buscar_por_titulo(self, titulo):

        for libro in self.libros.values():
            if libro.obtener_titulo().lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self.libros.values():
            if libro.obtener_autor().lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():
            if libro.obtener_categoria().lower() == categoria.lower():
                print(libro)

    # ---------------- LISTAR ----------------

    def listar_libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        libros = usuario.obtener_libros()

        if not libros:
            print("No tiene libros prestados.")
            return

        for libro in libros:
            print(libro)

    def mostrar_catalogo(self):

        if not self.libros:
            print("No hay libros disponibles.")
            return

        for libro in self.libros.values():
            print(libro)