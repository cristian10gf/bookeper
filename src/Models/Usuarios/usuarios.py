from abc import ABC, abstractmethod
from multipledispatch import dispatch
import random


class Usuario(ABC):

    @dispatch(str, str)
    def __init__(self, nombre: str, contrasena: str) -> None:
        self._contrasena = contrasena
        self._nombre = nombre
        self._codigo_Usuario = random.randint(1000, 9999)

    @dispatch(str, str, int)
    def __init__(self, nombre: str, contrasena: str, codigo_Usuario: int) -> None:
        self._contrasena = contrasena
        self._nombre = nombre
        self._codigo_Usuario = codigo_Usuario

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def codigo_Usuario(self) -> int:
        return self._codigo_Usuario

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena: str) -> None:
        self._contrasena = contrasena

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @abstractmethod
    def buscar_libro_por_nombre(self, nombre):
        pass

    @abstractmethod
    def prestar_libro(self, libro):
        pass

    @abstractmethod
    def ver_libros_prestados(self):
        pass

    @abstractmethod
    def devolver_libro(self, libro):
        pass




