from src.Models.core.gestor import Bookeeper
from datetime import date, datetime

class ControlBookeeper:
    __bookeeper = Bookeeper()

    @staticmethod
    def verificar_admin(usuario: str, contrasena: str) -> bool:
        return ControlBookeeper.__bookeeper.verificar_admin(usuario, contrasena)

    @staticmethod
    def get_estante(id: int) -> 'Estante':
        return ControlBookeeper.__bookeeper.get_estante(id)

    @staticmethod
    def get_estantes() -> list['Estante']:
        return ControlBookeeper.__bookeeper.estantes

    @staticmethod
    def get_libros() -> list['Libro']:
        return ControlBookeeper.__bookeeper.get_libros()

    @staticmethod
    def get_libro(id: int) -> 'Libro':
        return ControlBookeeper.__bookeeper.get_libro(id)

    @staticmethod
    def get_prestamos(usuario: 'Usuario') -> list['Prestamo']:
        return ControlBookeeper.__bookeeper.get_prestamos(usuario)

    @staticmethod
    def get_prestamo(id: int) -> 'Prestamo':
        return ControlBookeeper.__bookeeper.get_prestamo(id)

    @staticmethod
    def get_clientes() -> list['Cliente']:
        return ControlBookeeper.__bookeeper.clientes

    @staticmethod
    def get_cliente(id) -> 'Cliente':
        return ControlBookeeper.__bookeeper.get_cliente(id)

    @staticmethod
    def get_admins() -> list['Administrador']:
        return ControlBookeeper.__bookeeper.administradores

    @staticmethod
    def get_libro_by_name(name: str) -> 'Libro':
        return ControlBookeeper.__bookeeper.bucar_libro_por_nombre(name)

    @staticmethod
    def new_prestamo(
            fecha: datetime,
            nombre_cliente: str,
            username_cliente: str,
            nombre: str,
            autores: str,
            fecha_lanzamiento: date,
            genero: str,
            editorial: str,
            ubicacion: int,
            codigo: int,
            estado: 'Prestamo' = None
    ) -> None:
        ControlBookeeper.__bookeeper.new_prestamo(
            fecha,
            nombre_cliente,
            username_cliente,
            nombre,
            autores,
            fecha_lanzamiento,
            genero,
            editorial,
            ubicacion,
            codigo,
            estado
        )

    @staticmethod
    def new_cliente(nombre: str, contraseña: str) -> None:
        ControlBookeeper.__bookeeper.new_cliente(nombre, contraseña)

    @staticmethod
    def new_libro(
            nombre: str,
            autores: str,
            fecha_lanzamiento: date,
            genero: str,
            editorial: str,
            ubicacion: int,
            codigo: int
    ) -> None:
        ControlBookeeper.__bookeeper.new_libro(
            nombre,
            autores,
            fecha_lanzamiento,
            genero,
            editorial,
            ubicacion,
            codigo
        )

    @staticmethod
    def new_estante() -> None:
        pass

    @staticmethod
    def new_admin(nombre: str, contraseña: str) -> None:
        ControlBookeeper.__bookeeper.new_admin(nombre, contraseña)


