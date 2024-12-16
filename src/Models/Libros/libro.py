import random

class Libro:
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: int, genero: str, editorial: str, ubicacion,codigo: int = random.randint(1000, 9999), estado = None):
        self.__nombre = nombre
        self.__autores = autores.split(",")
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__genero = genero
        self.__editorial = editorial
        self.__ubicacion = ubicacion
        self.__codigo = codigo
        self.__estado = estado

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

    def prestar(self, prestamo): self.__estado = prestamo
    
    def devolver(self): self.__estado = None 

    def get_autores(self) -> str: return ",".join(self.__autores)
    
    def eliminar(self):
        self.__estado = None
        self.__ubicacion = None
        
    
    def buscar_por_autor(self, autor: str) -> bool:
        for a in self.__autores:
            if autor in a:
                return True
        return False

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

    @property
    def ubicacion(self): return self.__ubicacion

    @property
    def nombre(self): return self.__nombre
    
    @ubicacion.setter
    def ubicacion(self, ubicacion): self.__ubicacion = ubicacion.codigo