import random
from src.Models.Constantes import Metodos_consulta
from src.Models.Libros.libro import Libro
from src.Models.Usuarios.cliente import Cliente
from src.Models.Usuarios.usuarios import Usuario
from src.Models.core.estante_libros import EstanteDeLibros
from src.Models.core.prestamos import Prestamo

class administrador(Usuario):
    def __init__(self, nombre: str, contrasena: str, estantes: list['EstanteDeLibros'] = [], codigo_usuario: int = random.randint(1000, 9999)) -> None:
        super().__init__(nombre, contrasena, codigo_usuario)
        self.__estantes = estantes
        self.__prestamos_pendientes: list[Prestamo] = []

    def agregar_estante(self, estante: 'EstanteDeLibros'):
        self.__estantes.append(estante)

    def quitar_estante(self, estante: 'EstanteDeLibros'):
        self.__estantes.remove(estante)

    def buscar_libro(self, nombre: str) -> Libro | None:
        for estante in self.__estantes:
            libro = estante.get_libro_por_nombre(nombre)
            if libro is not None:
                return libro
        return None

    def buscar_libros_por_autor(self, autor) -> list['Libro']:
        libros_encontrados = []
        for estante in self.estantes:
            libros_en_estante = estante.buscar_libros(autor, Metodos_consulta.AUTOR)
            libros_encontrados.extend(libros_en_estante)
        return libros_encontrados

    def prestar_libro(self, libro: 'Libro', Cliente: 'Cliente') -> None:
        prestamo = Prestamo(Cliente, libro)
        self.__prestamos_pendientes.append(prestamo)

    def devolver_libro(self, libro: 'Libro', Cliente: 'Cliente') -> str:
        Cliente.devolver_libro(libro)
        for prestamo in self.__prestamos_pendientes:
            if prestamo.libro.codigo == libro.codigo:
                self.__prestamos_pendientes.remove(prestamo)
                return "Libro devuelto por el administrador"
        return "No se encontro el prestamo"

    def verificar_libro_prestado(self, libro: 'Libro') -> bool:
        for prestamo in self.__prestamos_pendientes:
            if prestamo.libro.codigo == libro.codigo:
                return True
        return False

    def get_estante(self,id: int) -> EstanteDeLibros | None:
        for estante in self.__estantes:
            if estante.codigo == id:
                return estante
        return None

    @property
    def estantes(self):
        return self.__estantes

    @property
    def prestamos_pendientes(self):
        return self.__prestamos_pendientes