from src.Models.config.config import *
from src.Models.Libros.recomendacio import Recomendacion

def traer_datos() -> dict:
    info = db()
    todo = {
        'administradores': info.get_admins(),
        'clientes': info.get_clientes(),
        'estantes': info.get_estantes()
    }
    return todo

def guardar_datos(self: 'Bookeeper') -> None:
    info = db()
    todos_datos = {
        'admins': self.administradores,
        'estantes': self.estantes,
        'libros': [libro for estante in self.estantes for libro in estante.libros],
        'prestamos': [prestamo for cliente in self.clientes for prestamo in cliente.prestamos],
        'clientes': self.clientes
    }
    info.actualizar( todos_datos )
class Bookeeper:

    def __init__(
            self,
            administradores: list['administrador'] = [],
            clientes: list['Cliente'] = [],
            estantes: list['EstanteDeLibros'] = []
    )-> None:
        self.__administradores = administradores
        self.__clientes = clientes
        self.__estantes = estantes

        for admin in traer_datos()['administradores']:
            self.__administradores.append(admin)

        for cliente in traer_datos()['clientes']:
            self.__clientes.append(cliente)

        for admin in self.__administradores:
            self.__estantes.extend(admin.estantes)


    def agregar_administrador(self, administrador: 'administrador') -> None:
        self.__administradores.append(administrador)
        guardar_datos()

    def agregar_Cliente(self, cliente: 'Cliente'):
        self.__clientes.append(cliente)
        guardar_datos()

    def agregar_estante(self, estante: 'EstanteDeLibros') -> None:
        self.__estantes.append(estante)
        guardar_datos()

    def get_estante(self, codigo: int) -> 'EstanteDeLibros':
        for estante in self.__estantes:
            if estante.codigo == codigo:
                return estante
        return None

    def buscar_libro_por_nombre(self, nombre: str) -> 'Libro':
        for estante in self.__estantes:
            libro = estante.buscar_libro_por_nombre(nombre)
            if libro is not None:
                return libro
        return None

    @property
    def administradores(self):
        return self.__administradores

    @property
    def clientes(self):
        return self.__clientes

    @property
    def estantes(self):
        return self.__estantes

    @administradores.setter
    def administradores(self, administrador):
        self.__administradores.append(administrador)

    @clientes.setter
    def clientes(self, cliente):
        self.__clientes.append(cliente)

    @estantes.setter
    def estantes(self, estante):
        self.__estantes.append(estante)

    def verificar_admin(self, username: str, password: str) -> bool:
        for admin in self.__administradores:
            if admin.nombre == username and admin.contrasena == password:
                return True
        return False

    def verificar_cliente(self, username: str, password: str) -> bool:
        for cliente in self.__clientes:
            if cliente.nombre == username and cliente.contrasena == password:
                return True
        return False

    def get_libros(self) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            libros += estante.libros
        return libros

    def get_libro(self, codigo: int) -> 'Libro':
        for estante in self.__estantes:
            libro = estante.get_libro(codigo)
            if libro is not None:
                return libro
        return None

    def get_prestamos(self, usuario: 'Usuario') -> list['Prestamo']:
        prestamos = []
        if isinstance(usuario, 'Cliente'):
            for prestamo in usuario.prestamos:
                prestamos.append(prestamo)
        elif isinstance(usuario, 'Administrador'):
            for cliente in self.__clientes:
                for prestamo in cliente.prestamos:
                    prestamos.append(prestamo)
        return prestamos

    def get_prestamo(self, codigo: int) -> 'Prestamo':
        for cliente in self.__clientes:
            for prestamo in cliente.prestamos:
                if prestamo.codigo == codigo:
                    return prestamo
        return None

    def get_cliente(self, id: int) -> 'Cliente':
        for cliente in self.__clientes:
            if cliente.id == id:
                return cliente
        return None

    def new_prestamo(
            fecha: datetime,
            nombre_cliente: str,
            username_cliente: str,
            id_cliente: int,
            nombre: str,
            autores: str,
            fecha_lanzamiento: date,
            genero: str,
            editorial: str,
            ubicacion: int,
            codigo: int,
            estado: 'Prestamo' = None
    ) -> None:
        libro = book.buscar_libro_por_nombre(nombre)
        cliente = book.get_cliente(id_cliente)
        if libro is not None and cliente is not None:
            prestamo = Prestamo(cliente, libro, fecha)
            guardar_datos(self)

    def new_cliente(self, nombre: str, password: str) -> None:
        cliente = Cliente(nombre, password)
        self.__clientes.append(cliente)
        guardar_datos(self)

    def new_libro(self, nombre: str, autores: str, fecha_lanzamiento: date, genero: str, editorial: str, ubicacion: int, codigo: int) -> None:
        libro = Libro(nombre, autores, fecha_lanzamiento, genero, editorial, ubicacion, codigo)
        for estante in self.__estantes:
            if estante.codigo == ubicacion:
                estante.libros.append(libro)
                break
        guardar_datos(self)

    def generate_recomendacion(self, libro: int, cliente: Cliente) -> None:
        recomendacion = Recomendacion(1, libro, cliente, datetime.now())
        guardar_datos(self)

    def new_admin(self, nombre: str, password: str) -> None:
        admin = administrador(nombre, password)
        self.__administradores.append(admin)
        guardar_datos(self)