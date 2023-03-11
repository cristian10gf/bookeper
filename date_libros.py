from libro import Libro

# crea un archivo donde se almacenaran los libros
with open('libros.txt', 'w') as archivo:
    archivo.write('nombre_libro,autor,editorial,genero,fecha_publicacion')

# crea una funcion para leer los datos de un archivo de texto y guardarlos en un diccionario
def leer_archivo():
    with open('libros.txt', 'r') as archivo:
        for linea in archivo:
            libros = {}
            linea = linea.strip()
            nombre_libro, autor, editorial, genero, fecha_publicacion = linea.split(',')
            libros[nombre_libro] = Libro(nombre_libro, autor, editorial, genero, fecha_publicacion)
    return libros

# crea una funcion para verificar si un libro existe en el archivo de texto
def verificar_libro(nombre_libro):
    libros = leer_archivo()
    if nombre_libro in libros:
        return True
    else:
        return False

# una funcion que retorne todos los libros de un autor
def libros_autor(autor):
    libros = leer_archivo()
    libros_autor = []
    for libro in libros:
        if libros[libro].autor == autor:
            libros_autor.append(libros[libro])
    return libros_autor

# una funcion que retorne todos los libros de un genero
def libros_genero(genero):
    libros = leer_archivo()
    libros_genero = []
    for libro in libros:
        if libros[libro].genero == genero:
            libros_genero.append(libros[libro])
    return libros_genero

# una funcion que retorne todos los libros de una editorial
def libros_editorial(editorial):
    libros = leer_archivo()
    libros_editorial = []
    for libro in libros:
        if libros[libro].editorial == editorial:
            libros_editorial.append(libros[libro])
    return libros_editorial

# cree una funcion que retorne ciertos libros segun un filtro
def libros_filtro(filtro):
    libros = leer_archivo()
    libros_filtro = []
    for libro in libros:
        if libros[libro].filtro == filtro:
            libros_filtro.append(libros[libro])
    return libros_filtro

