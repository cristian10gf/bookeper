from multipledispatch import dispatch
from src.Models.Libros.libro import Libro
from src.Models.Usuarios.cliente import Cliente

class Recomendacion:
    __id: int = 0

    def __init__(self, id: int = None, libro: 'Libro' = None, usuario: 'Cliente' = None, prestamo: bool = False):
        if id is None:
            self.__id = Recomendacion.__id
            Recomendacion.__id += 1
        else:
            self.__id = id
        self.__libro = libro
        self.__usuario = usuario
        self.__usuario.agregar_recomendacion(self)
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
    
