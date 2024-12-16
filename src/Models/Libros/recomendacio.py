from typing import Optional
from src.Models.Libros.libro import Libro

class Recomendacion:
    __id: int = 0

    def __init__(self, id: Optional[int] = None, libro: Optional['Libro'] = None, usuario = None, prestamo: bool = False):
        if id is None:
            self.__id = Recomendacion.__id
            Recomendacion.__id += 1
        else:
            self.__id = id
        self.__libro = libro if libro is not None else None
        self.__usuario = usuario if usuario is not None else None
        self.__usuario.agregar_recomendacion(self) if self.__usuario is not None else None
        self.__prestamo = prestamo

    @property
    def id(self):
        return self.__id
    
    @property
    def libro(self):
        return self.__libro
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def prestamo(self):
        return self.__prestamo
    
