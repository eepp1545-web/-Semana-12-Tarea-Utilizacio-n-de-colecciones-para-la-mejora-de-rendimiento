### Descripción
- **modelos/**  
  Contiene las clases que representan las entidades del sistema.
- **servicios/**  
  Contiene la lógica del negocio de la biblioteca.
- **main.py**  
  Punto de arranque del programa y menú interactivo.

---
# Clases del sistema
## 📖 Libro
Representa un libro dentro del sistema.
Atributos:
- Título y autor (almacenados como **tupla**)
- Categoría
- ISBN (identificador único)
---
## Usuario
Representa un usuario registrado en la biblioteca.
Atributos:
- Nombre
- ID de usuario
- Lista de libros prestados (**lista**)
---
## BibliotecaServicio
Gestiona la lógica principal del sistema.
Utiliza:
- **Diccionario** → para almacenar libros disponibles  
- **Set (conjunto)** → para IDs únicos de usuarios  
- **Lista** → para libros prestados de cada usuario
---
# Funcionalidades del sistema
El sistema permite:
- Añadir libros
- Quitar libros
- Registrar usuarios
- Eliminar usuarios
- Prestar libros
- Devolver libros
- Buscar libros por:
  - título
  - autor
  - categoría
- Listar libros prestados a un usuario
- Ver catálogo de libros disponibles
---
