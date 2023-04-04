import random
from multipledispatch import dispatch
from Files.file_manager import FileManager

class Libro:
    todos_libros = FileManager("libros.txt").generate_path()
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
        return f"{self.nombre} de {self.autores} ({self.fecha_lanzamiento}) - {self.editorial}, {self.formato}, {self.genero}, estante: {self.ubicacion}, {self.estado}"
    
    def __eq__(self, other: "Libro"):
        if other is None:
            return False
        return self.nombre == other.nombre and self.autores == other.autores and self.fecha_lanzamiento == other.fecha_lanzamiento and self.editorial == other.editorial and self.formato == other.formato and self.genero == other.genero and self.ubicacion == other.ubicacion
    
    def __lt__(self, other: "Libro"):
        return self.fecha_lanzamiento < other.fecha_lanzamiento
    
    def asignar_estante(self, ubicacion):
        self.ubicacion = ubicacion
    
    def prestar(self):
        self.estado = "prestado"
        modificar_info_libro(self.codigo, "prestado")

    def devolver(self):
        self.estado = "disponible"
        modificar_info_libro(self.codigo, "disponible")


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