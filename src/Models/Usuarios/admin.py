from multipledispatch import dispatch
from src.Models.Usuarios.usuarios import Usuario
from src.Models.core.prestamos import Prestamo

class administrador(Usuario):
    @dispatch(str, str)
    def __init__(self, nombre: str, contrasena: str) -> None:
        super().__init__(nombre, contrasena)
        self.__estantes = []
        self.__prestamos_pendientes = []

    @dispatch(str, str, list, int)
    def __init__(self, nombre:str, contrasena: str, estantes: list['EstanteDeLibros'], codigo_usuario: int) -> None:
        super().__init__(nombre, contrasena, codigo_usuario)
        self.__estantes = estantes
        self.__prestamos_pendientes = []

    def agregar_estante(self, estante: 'EstanteDeLibros'):
        self.__estantes.append(estante)

    def quitar_estante(self, estante: 'EstanteDeLibros'):
        self.__estantes.remove(estante)

    def buscar_libro_por_nombre(self, nombre: str) -> 'Libro':
        for estante in self.__estantes:
            libro = estante.buscar_libro_por_nombre(nombre)
            if libro is not None:
                return libro
        return None

    def buscar_libros_por_autor(self, autor) -> list['Libro']:
        libros_encontrados = []
        for estante in self.estantes:
            libros_en_estante = estante.buscar_libros_por_autor(autor)
            libros_encontrados.extend(libros_en_estante)
        return libros_encontrados

    def prestar_libro(self, libro: 'Libro', Cliente: 'Cliente') -> None:
        prestamo = Prestamo(Cliente, libro)
        self.__prestamos_pendientes.append(prestamo)

    def devolver_libro(self, libro: 'Libro', Cliente: 'Cliente') -> None:
        Cliente.devolver_libro(libro)
        for prestamo in self.__prestamos_pendientes:
            if prestamo.libro.codigo == libro.codigo:
                self.__prestamos_pendientes.remove(prestamo)
                return
        print("No se encontro el prestamo")

    def ver_libros_prestados(self) -> list['Prestamo']:
        return self.__prestamos_pendientes

    def verificar_libro_prestado(self, libro: 'Libro') -> bool:
        return libro in self.__prestamos_pendientes

    @property
    def estantes(self):
        return self.__estantes

    @estantes.setter
    def estantes(self, estante):
        self.__estantes.append(estante)

    @property
    def prestamos_pendientes(self):
        return self.__prestamos_pendientes

    @prestamos_pendientes.setter
    def prestamos_pendientes(self, prestamo):
        self.__prestamos_pendientes.append(prestamo)

    def get_estante(self,id: int) -> 'EstanteDeLibros':
        for estante in self.__estantes:
            if estante.codigo == id:
                return estante
        return None

