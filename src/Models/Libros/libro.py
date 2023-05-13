from multipledispatch import dispatch
from Files.file_manager import FileManager
from core.prestamos import Prestamo
from datetime import date

class Libro:
    todos_libros = FileManager("libros.txt").generate_path()
    __codigo = 0
    @dispatch(str, str, date, str, str, str, int, Prestamo or None)
    def __init__(self,
                 nombre: str,
                 autores: str,
                 fecha_lanzamiento:
                 date, genero: str,
                 editorial:str,
                 ubicacion: int,
                 estado: 'Prestamo' = None
    ) -> None:
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
    def __init__(self,
                 nombre: str,
                 autores: str,
                 fecha_lanzamiento: date,
                 genero: str,
                 editorial:str,
                 ubicacion: int,
                 codigo: int,
                 estado: 'Prestamo' = None
    ) -> None:
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

