from abc import ABC, abstractmethod

class Usuario(ABC):
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
    def prestar_libro(self, libro):
        pass

    @abstractmethod
    def devolver_libro(self, libro):
        pass