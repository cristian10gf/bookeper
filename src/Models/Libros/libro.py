from multipledispatch import dispatch
from src.Models.Files.file_manager import FileManager
from src.Models.core.prestamos import Prestamo
from datetime import date

class Libro:
    todos_libros = FileManager("libros.txt").generate_path()
    __codigo = 0
    @dispatch(str, str, int, str, str, str, int, Prestamo or None)
    def __init__(self,
                 nombre: str,
                 autores: str,
                 fecha_lanzamiento:int, 
                 genero: str,
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

    @dispatch(str, str, int, str, str, int,int,Prestamo or None)
    def __init__(self,
                 nombre: str,
                 autores: str,
                 fecha_lanzamiento: int,
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

    @dispatch(str, str, int, str, str, int, int)
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: int, genero: str, editorial: str, ubicacion: int,codigo: int):
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
    def prestar(self, prestamo: 'Prestamo'): self.__estado = prestamo
    def devolver(self): self.__estado = None 
    @property
    def codigo(self): return self.__codigo
    @property
    def autores(self): return self.__autores
    @property
    def fecha_lanzamiento(self): return self.__fecha_lanzamiento
    @property
    def genero(self): return self.__genero
    @property
    def editorial(self): return self.__editorial
    @property
    def estado(self): return self.__estado

    def guardar_autores(self) -> str:
        autores = ""
        for autor in self.__autores:
            autores += autor + ","
        return autores[:-1]


