from datetime import date
import random
from multipledispatch import dispatch
from Files.file_manager import FileManager

class Libro:
    @dispatch(str, str, int, str, str, str, int, str)
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: int, genero: str, editorial:str, formato: str, ubicacion: int, estado: str):
        self.nombre = nombre
        self.autores = autores
        self.fecha_lanzamiento = fecha_lanzamiento
        self.genero = genero
        self.editorial = editorial
        self.formato = formato
        self.ubicacion = ubicacion
        self.codigo = random.randint(1, 1000)
        self.estado = estado

    @dispatch(str, str, int, str, str, str, str, str, int)
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: int, genero: str, editorial:str, formato: str, ubicacion: str, estado: str, codigo: int):
        self.nombre = nombre
        self.autores = autores
        self.fecha_lanzamiento = fecha_lanzamiento
        self.genero = genero
        self.editorial = editorial
        self.formato = formato
        self.ubicacion = ubicacion
        self.codigo = codigo
        self.estado = estado

    def __str__(self):
        return f"{self.nombre},{self.autores},{self.fecha_lanzamiento},{self.editorial},{self.formato},{self.genero},{self.ubicacion},{self.estado},{self.codigo}"
    
    def __repr__(self):
        return f"{self.nombre} de {', '.join(self.autores)} ({self.fecha_lanzamiento}) - {self.editorial}, {self.formato}, {self.genero}, {self.ubicacion}, {self.estado}"
    
    def __eq__(self, other: "Libro"):
        return self.nombre == other.nombre and self.autores == other.autores and self.fecha_lanzamiento == other.fecha_lanzamiento and self.editorial == other.editorial and self.formato == other.formato and self.genero == other.genero and self.ubicacion == other.ubicacion
    
    def __lt__(self, other: "Libro"):
        return self.fecha_lanzamiento < other.fecha_lanzamiento
    
    def asignar_estante(self, ubicacion):
        self.ubicacion = ubicacion

print(FileManager.DATA_PATH)
#direccion_todos_libros = FileManeger('libros.txt')
# crea una funcion para almacenar un libro en un archivo de texto
def almacenar_libro(libro: Libro):
    with open('Datos\libros.txt', 'a') as archivo:
        archivo.write(f"{libro}\n")

# crea una funcion para leer los datos de un archivo de texto y guardarlos en un diccionario
def leer_archivo() -> list:
    libros_del_archivo = []
    with open('Datos\libros.txt', 'r') as archivo:
        for linea in archivo:
            libros = {}
            linea = linea.strip()
            nombre_libro, autor, fecha_publicacion, editoriales, formato, genero, ubicacion, estado, codigo = linea.split(',')
            libro = Libro(nombre_libro, autor, int(fecha_publicacion), editoriales, formato, genero, ubicacion, estado, int(codigo))
            libros["nombre_libro"] = libro.nombre
            libros["autor"] = libro.autores
            libros["editorial"] = libro.editorial
            libros["formato"] = libro.formato
            libros["fecha_publicacion"] = libro.fecha_lanzamiento
            libros["codigo"] = libro.codigo
            libros["genero"] = libro.genero
            libros["estado"] = libro.estado
            libros["ubicacion"] = libro.ubicacion
            libros_del_archivo.append(libros)
    return libros_del_archivo

# crea una funcion para verificar si un libro existe en el archivo de texto
def verificar_libro(nombre_libro) -> bool:
    libros = leer_archivo()
    if nombre_libro in libros:
        return True
    else:
        return False

# una funcion que retorne todos los libros de un autor
def libros_autor(autor) -> list:
    libros = leer_archivo()
    libros_autor = []
    for libro in libros:
        if libros[libro].autor == autor:
            libros_autor.append(libros[libro])
    return libros_autor

# una funcion que retorne todos los libros de un genero
def libros_genero(genero) -> list:
    libros = leer_archivo()
    libros_genero = []
    for libro in libros:
        if libros[libro].genero == genero:
            libros_genero.append(libros[libro])
    return libros_genero

# una funcion que retorne todos los libros de una editorial
def libros_editorial(editorial) -> list:
    libros = leer_archivo()
    libros_editorial = []
    for libro in libros:
        if libros[libro].editorial == editorial:
            libros_editorial.append(libros[libro])
    return libros_editorial

# cree una funcion que retorne ciertos libros segun un filtro
def libros_filtro(filtro) -> list:
    libros = leer_archivo()
    libros_filtro = []
    for libro in libros:
        if libros[libro].filtro == filtro:
            libros_filtro.append(libros[libro])
    return libros_filtro

def retornar_libro(codigo) -> Libro:
    libros = leer_archivo()
    for libro in libros:
        if libro["codigo"] == codigo:
            pos = libros.index(libro)
            return Libro(libros[pos]["nombre_libro"], libros[pos]["autor"], libros[pos]["fecha_publicacion"], libros[pos]["editorial"], libros[pos]["formato"], libros[pos]["genero"], libros[pos]["ubicacion"], libros[pos]["estado"], libros[pos]["codigo"])
            #return libros[pos]