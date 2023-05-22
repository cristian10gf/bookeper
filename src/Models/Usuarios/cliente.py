from src.Models.core.prestamos import *
from src.Models.Usuarios.usuarios import Usuario
from multipledispatch import dispatch

class Cliente(Usuario):
    @dispatch(str, str)
    def __init__(self, nombre: str, contraseña: str):
        super().__init__(nombre, contraseña)
        self.__prestamos: list['Prestamo'] = []

    @dispatch(str, str, int)
    def __init__(self, nombre: str, contraseña: str, codigo_usuario: int):
        super().__init__(nombre, contraseña, codigo_usuario)
        self.__prestamos: list['Prestamo'] = []

    def prestar_libro(self, libro: 'Libro') -> None:
        for prestamo in self.__prestamos:
            if prestamo.libro.codigo == libro.codigo:
                print("Ya tienes este libro prestado.")
                return
        prestamo = Prestamo(self, libro)

    def devolver_libro(self, libro: 'Libro'):
        for prestamo in self.__prestamos:
            if prestamo.libro.codigo == libro.codigo:
                prestamo.devolver()
                self.__prestamos.remove(prestamo)
                return
        print("No tienes este libro prestado.")

    def ver_libros_prestados(self) -> list['Prestamo']:
        return self.__prestamos

    def buscar_libro_por_nombre(self, nombre: str) -> 'Libro':
        for estante in self.biblioteca.estantes:
            libro = estante.buscar_libro_por_nombre(nombre)
            if libro is not None:
                return libro
        return None

    @property
    def prestamos(self):
        return self.__prestamos

    @prestamos.setter
    def prestamos(self, prestamo):
        self.__prestamos.append(prestamo)
