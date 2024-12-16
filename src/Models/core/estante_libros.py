from src.Models.Constantes import Metodos_consulta
from src.Models.Libros.libro import Libro
from src.Models.Usuarios.admin import administrador
import random

class EstanteDeLibros:
    def __init__(self, admin: 'administrador', genero: str, tamano: int, codigo: int = random.randint(1000, 9999), libros: list['Libro'] = []):
        self.__admin = admin
        self.__admin.estantes.append(self)
        self.__codigo = codigo
        self.__genero = genero
        self.__tamano = tamano

        self.__libros = libros
        for libro in self.__libros:
            libro.ubicacion = self

    def agregar_libro(self, libro: "Libro") -> str:
        if len(self.__libros) == self.__tamano:
            return "No se pueden agregar mas libros"
        
        self.__libros.append(libro)
        libro.ubicacion = self
        return "Libro agregado"

    def quitar_libro(self, libro: 'Libro') -> str:
        if libro not in self.__libros:
            return "No se puede quitar un libro que no esta en el estante"
            
        self.__libros.remove(libro)
        libro.eliminar()
        return "Libro eliminado"

    def buscar_libros(self, valor: str, metodo: Metodos_consulta) -> set['Libro']:
        if len(self.__libros) == 0:
            return set()

        libros_encontrados = set()
        for libro in self.__libros:
            nm = ""
            if metodo == Metodos_consulta.NOMBRE:
                nm = libro.nombre.upper()
            elif metodo == Metodos_consulta.GENERO:
                nm = libro.genero.upper()
            elif metodo == Metodos_consulta.CODIGO:
                nm = str(libro.codigo)
            elif metodo == Metodos_consulta.AUTOR:
                encontro = libro.buscar_por_autor(valor)
                if encontro: libros_encontrados.add(libro)
                continue

            nn = valor.upper()
            if nm.find(nn) != -1: libros_encontrados.add(libro)
        return libros_encontrados

    def get_libro(self, codigo: int):
        for libro in self.__libros:
            if libro.codigo == codigo:
                return libro
        return None
    
    def get_libro_por_nombre(self, nombre: str):
        for libro in self.__libros:
            if libro.nombre == nombre:
                return libro
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