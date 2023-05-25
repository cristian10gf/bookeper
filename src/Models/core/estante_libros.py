from src.Models.Libros.libro import *
from src.Models.Usuarios.admin import administrador


class EstanteDeLibros:
    __id = 0

    @dispatch(list, administrador, str, int)
    def __init__(self, libros: list['libro'], admin: 'administrador', genero: str, tamano: int):
        self.__codigo = EstanteDeLibros.__id
        EstanteDeLibros.__id += 1
        if libros is None or len(libros) == 0:
            self.__libros = []
        else:
            self.__libros = libros
            for libro in self.__libros:
                libro.ubicacion = self
        self.__admin = admin
        self.__admin.estantes.append(self)
        self.__genero = genero
        self.__tamano = tamano

    @dispatch(list, int, administrador, str, int)
    def __init__(self, libros: list, codigo: int, admin: 'administrador', genero: str, tamano: int):
        if libros is None or len(libros) == 0:
            self.__libros = []
        else:
            self.__libros = libros
            for libro in self.__libros:
                libro.ubicacion = self
        self.__admin = admin
        self.__admin.estantes.append(self)
        self.__codigo = codigo
        self.__genero = genero
        self.__tamano = tamano

    def agregar_libro(self, libro: "Libro") -> None:
        if len(self.__libros) == self.__tamano:
            print("No se pueden agregar mas libros")
        else:
            self.__libros.append(libro)

    def quitar_libro(self, libro: 'Libro') -> None:
        if libro not in self.__libros:
            print("No se puede quitar un libro que no esta en el estante")
        else:
            self.__libros.remove(libro)

    def buscar_libros_por_nombre(self, nombre: str) -> list['Libro']:
        if len(self.__libros) == 0:
            libros_encontrados = []
            return libros_encontrados

        else:
            libros_encontrados = []
            for libro in self.__libros:
                if nombre in libro.nombre:
                    libros_encontrados.append(libro)
            return libros_encontrados

    def buscar_libros_por_autor(self, autor) -> list['Libro']:
        libros_encontrados = []
        for libro in self.libros:
            for nautor in libro.autores:
                if autor in nautor:
                    libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_libros_por_genero(self, genero) -> list['Libro']:
        libros_encontrados = []
        for libro in self.libros:
            if genero in libro.genero:
                libros_encontrados.append(libro)
        return libros_encontrados

    def get_libro(self, codigo: int) -> 'Libro':
        for libro in self.__libros:
            if libro.codigo == codigo:
                return libro
        return None
    def get_nombre_libro(self, codigo: int) -> str:
        for libro in self.__libros:
            if libro.codigo == codigo:
                return libro.nombre
        return None
    @property
    def libros(self):
        return self.__libros

    @property
    def codigo(self):
        return self.__codigo

    @property
    def genero(self):
        return self.__genero

    @property
    def tamano(self):
        return self.__tamano

    @property
    def admin(self):
        return self.__admin

    @libros.setter
    def libros(self, libros: list['Libro']):
        self.__libros = libros
