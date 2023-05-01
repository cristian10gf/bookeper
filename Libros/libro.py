from multipledispatch import dispatch
from Files.file_manager import FileManager
from core.prestamos import Prestamo
from datetime import date

class Libro:
    todos_libros = FileManager("libros.txt").generate_path()
    __codigo = 0
    @dispatch(str, str, date, str, str, str, int, Prestamo or None)
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: date, genero: str, editorial:str, ubicacion: int, estado: 'Prestamo' = None):
        self.__nombre = nombre
        self.__autores = autores.split(",")
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__genero = genero
        self.__editorial = editorial
        self.__ubicacion = ubicacion
        self.__codigo = Libro.__codigo
        Libro.__codigo += 1
        self.__estado = estado

    @dispatch(str, str, date, str, str, int,int,Prestamo or None)
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: date, genero: str, editorial:str, ubicacion: int, codigo: int, estado: 'Prestamo' = None):
        self.__nombre = nombre
        self.__autores = autores.split(",")
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__genero = genero
        self.__editorial = editorial
        self.__ubicacion = ubicacion
        self.__codigo = codigo
        self.__estado = estado

    @dispatch(str, str, date, str, str, int, int)
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: date, genero: str, editorial: str, ubicacion: int,codigo: int):
        self.__nombre = nombre
        self.__autores = autores.split(",")
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__genero = genero
        self.__editorial = editorial
        self.__ubicacion = ubicacion
        self.__codigo = codigo
        self.__estado = None

    def __str__(self):
        return f"{self.__nombre}," \
               f"{self.__autores}," \
               f"{self.__fecha_lanzamiento}," \
               f"{self.__editorial}," \
               f"{self.__formato}," \
               f"{self.__genero}," \
               f"{self.__ubicacion}," \
               f"{self.__estado}," \
               f"{self.__codigo}"

    def __lt__(self, other: "Libro"):
        return self.__fecha_lanzamiento < other.fecha_lanzamiento

    @property
    def ubicacion(self): return self.__ubicacion
    @ubicacion.setter
    def ubicacion(self, ubicacion: 'EstanteDeLibros'): self.__ubicacion = ubicacion
    @property
    def nombre(self): return self.__nombre
    def prestar(self): self.__estado = "prestado"
    def devolver(self): self.__estado = "disponible"
    @property
    def codigo(self): return self.__codigo
    @property
    def autores(self): return self.__autores
    @property
    def fecha_lanzamiento(self): return self.__fecha_lanzamiento



# crea una funcion para almacenar un libro en un archivo de texto
def almacenar_libro(libro: Libro) -> None:
    with open('Datos\libros.txt', 'a') as archivo:
        archivo.write(f"{libro}\n")

# crea una funcion para leer los datos de un archivo de texto y guardarlos en un diccionario
def leer_archivo() -> list['Libro']:
    libros_del_archivo = []
    with open(Libro.todos_libros, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            nombre_libro, autor, fecha_publicacion, editoriales, formato, genero, ubicacion, estado, codigo = linea.split(',')
            libro = Libro(nombre_libro, autor, int(fecha_publicacion), editoriales, formato, genero, ubicacion, estado, int(codigo))
            libros_del_archivo.append(libro)
    return libros_del_archivo

# crea una funcion para verificar si un libro existe en el archivo de texto
def verificar_libro(nombre_libro: str) -> bool:
    libros = leer_archivo()
    for libro in libros:
        if libro.nombre == nombre_libro:
            return True
    return False

# cree una funcion que retorne ciertos libros segun un filtro
def libros_filtro(filtro) -> list:
    libros = leer_archivo()
    libros_filtro = []
    for libro in libros:
        if libro.filtro == filtro:
            libros_filtro.append(libro)
    return libros_filtro

def retornar_libro(codigo: int) -> Libro:
    libros = leer_archivo()
    for libro in libros:
        if libro.codigo == codigo:
            return libro

def reseteo_libros()-> None:
    with open(Libro.todos_libros, 'w') as archivo:
        archivo.write("")

def modificar_info_libro(codigo: int, nueva_info) -> None:
    act = False
    todos_los_libros = leer_archivo()
    for libro_lista in todos_los_libros:
        if libro_lista.codigo == codigo:
            act = True
            libro_lista.estado = nueva_info
            break
    if act == False: 
        "No se encontro el estante"
    else:
        reseteo_libros()
        for libro in todos_los_libros:
            almacenar_libro(libro)