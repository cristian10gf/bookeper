from datetime import datetime
from typing import Optional
from src.Models.Constantes import Metodos_consulta
from src.Models.core.prestamos import Prestamo
from src.Models.Usuarios.cliente import Cliente
from src.Models.Usuarios.admin import administrador
from src.Models.Libros.libro import Libro
from src.Models.core.estante_libros import EstanteDeLibros

class Gestor:
    def __init__(self, administradores: list['administrador'] = [], clientes: list['Cliente'] = []) -> None:
        self.__administradores = administradores
        self.__clientes = clientes
        self.__estantes: list[EstanteDeLibros] = []   

        for admin in administradores:
            self.__estantes.extend(admin.estantes)

    def agregar_administrador(self, administrador: 'administrador') -> None:
        self.__administradores.append(administrador)

    def agregar_Cliente(self, cliente: 'Cliente'):
        self.__clientes.append(cliente)

    def agregar_estante(self, estante: 'EstanteDeLibros') -> None:
        self.__estantes.append(estante)

    def get_estante(self, codigo: int) -> EstanteDeLibros | None:
        for estante in self.__estantes:
            if estante.codigo == codigo:
                return estante
        return None

    def buscar_libro_por_autor(self, autor: str) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            libros_encontrados = estante.buscar_libros(autor, Metodos_consulta.AUTOR)
            if len(libros_encontrados) > 0:
                libros.extend(libros_encontrados)
        return libros

    def buscar_libro_por_nombre(self, nombre: str) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            libros_encontrados = estante.buscar_libros(nombre, Metodos_consulta.NOMBRE)
            if len(libros_encontrados) > 0:
                libros.extend(libros_encontrados)
        return libros

    def buscar_libro_por_genero(self, genero: str) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            libros_encontrados = estante.buscar_libros(genero, Metodos_consulta.GENERO)
            if len(libros_encontrados) > 0:
                libros.extend(libros_encontrados)
        return libros

    @property
    def administradores(self) -> list['administrador']:
        return self.__administradores

    @property
    def clientes(self) -> list['Cliente']:
        return self.__clientes

    @property
    def estantes(self) -> list['EstanteDeLibros']:
        return self.__estantes

    @estantes.setter
    def estantes(self, estante):
        self.__estantes.append(estante)

    def verificar_admin(self, username: str, password: str, metodo: int = 1) -> bool:
        for admin in self.__administradores:
            if admin.nombre == username and admin.contrasena == password and metodo == 1:
                return True
            elif admin.nombre == username and metodo == 2:
                return True
        return False

    def verificar_cliente(self, username: str, password: str, metodo: int = 1) -> bool:
        for cliente in self.__clientes:
            if cliente.nombre == username and cliente.contrasena == password and metodo == 1:
                return True
            elif cliente.nombre == username and metodo == 2:
                return True
        return False

    def get_libros(self) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            libros.extend(estante.libros)
        return libros

    def get_libro(self, codigo: int) -> Libro | None:
        for estante in self.__estantes:
            libro = estante.get_libro(codigo)
            if libro is not None:
                return libro
        return None

    def get_prestamos(self, usuario) -> list['Prestamo']:
        prestamos = []
        if self.verificar_cliente(usuario.nombre, usuario.contrasena, 1):
            for prestamo in usuario.prestamos:
                prestamos.append(prestamo)
        elif self.verificar_admin(usuario.nombre, usuario.contrasena, 1):
            for cliente in self.__clientes:
                for prestamo in cliente.prestamos:
                    prestamos.append(prestamo)
        return prestamos

    def get_prestamo(self, codigo: int) -> Prestamo | None:
        for cliente in self.__clientes:
            for prestamo in cliente.prestamos:
                if prestamo.codigo == codigo:
                    return prestamo
        return None

    def get_cliente(self, id: int) -> Cliente | None:
        for cliente in self.__clientes:
            if cliente.codigo_Usuario == id:
                return cliente
        return None

    def new_prestamo(self, fecha: datetime, id_cliente: Optional[int] = None, nombre: Optional[str] = None) -> None:
        if id_cliente is None or nombre is None:
            return

        libro = self.buscar_libro_por_nombre(nombre)
        cliente = self.get_cliente(id_cliente)

        if len(libro) == 0 or cliente is None:
            return

        prestamo = Prestamo(cliente, libro[0], fecha_devolucion=fecha)
        for admin in self.administradores:
            admin.prestamos_pendientes.append(prestamo)
    
    def new_cliente(self, nombre: str, password: str) -> None:
        cliente = Cliente(nombre, password)
        self.__clientes.append(cliente)

    def new_libro(self, nombre: str, autores: str, fecha_lanzamiento: int, genero: str, editorial: str, ubicacion: int) -> bool:
        estante = self.get_estante(ubicacion) 
        if estante is None:
            return False
        
        libro = Libro(nombre, autores, fecha_lanzamiento, genero, editorial, estante)
        for estante in self.__estantes:
            if estante.codigo == ubicacion:
                estante.libros.append(libro)
                return True

        return False

    def new_admin(self, nombre: str, password: str) -> None:
        self.__administradores.append(administrador(nombre, password))

    def new_estante(self, genero: str, numero: int, admin: 'administrador'):
        self.__estantes.append(EstanteDeLibros(admin, genero, numero))

    def verificar_genero(self, genero: str) -> bool:
        for estante in self.__estantes:
            if estante.genero == genero:
                return True
        return False

    def cambiar_info(self, nombre: str, password: str, nombre2: str) -> None:
        for cliente in self.__clientes:
            if cliente.nombre == nombre and cliente.contrasena == password:
                cliente.nombre = nombre2
        for admin in self.__administradores:
            if admin.nombre == nombre and admin.contrasena == password:
                admin.nombre = nombre2
    