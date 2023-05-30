from src.Models.core.gestor import Bookeeper
from datetime import date, datetime

class ControlBookeeper:
    __bookeeper = Bookeeper()

    @staticmethod
    def verificar_admin(usuario: str, contrasena: str, metodo: int = 1) -> bool:
        return ControlBookeeper.__bookeeper.verificar_admin(usuario, contrasena, metodo)

    @staticmethod
    def verificar_cliente(usuario: str, contrasena: str, metodo: int = 1) -> bool:
        return ControlBookeeper.__bookeeper.verificar_cliente(usuario, contrasena, metodo)
    
    @staticmethod
    def get_estante(id: int) -> 'EstanteDeLibros':
        return ControlBookeeper.__bookeeper.get_estante(id)
    
    @staticmethod
    def get_estante_by_genero(genero: str) -> 'EstanteDeLibros':
        for estante in ControlBookeeper.__bookeeper.estantes:
            if estante.genero == genero:
                return estante

    @staticmethod
    def get_estantes() -> list['EstanteDeLibros']:
        return ControlBookeeper.__bookeeper.estantes

    @staticmethod
    def get_libros() -> list['Libro']:
        libros_info = {}
        libros =  ControlBookeeper.__bookeeper.get_libros()
        print(type(libros))
        for libro in libros:
            libros_info[libro.codigo] = {
                "nombre": libro.nombre,
                "autores": libro.autores,
                "fecha_lanzamiento": libro.fecha_lanzamiento,
                "genero": libro.genero,
                "editorial": libro.editorial,
                "ubicacion": libro.ubicacion,
                "estado": libro.estado
            }
        return libros

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
    def get_admin_by_name(name: str) -> 'administrador':
        for admin in ControlBookeeper.__bookeeper.administradores:
            if admin.nombre == name:
                return admin

    @staticmethod
    def get_cliente(id, name = None) -> 'Cliente':
        if name is not None:
            for cliente in ControlBookeeper.__bookeeper.clientes:
                if cliente.nombre == name:
                    return cliente
        else:
            return ControlBookeeper.__bookeeper.get_cliente(id)

    @staticmethod
    def get_admins() -> list['administrador']:
        return ControlBookeeper.__bookeeper.administradores

    @staticmethod
    def get_libro_by_name(name: str) -> {'Libro'}:
        return ControlBookeeper.__bookeeper.buscar_libro_por_nombre(name)

    @staticmethod
    def get_libro_by_author(author: str) -> {'Libro'}:
        return ControlBookeeper.__bookeeper.buscar_libro_por_autor(author)
    @staticmethod
    def get_libro_by_genre(genre: str) -> {'Libro'}:
        return ControlBookeeper.__bookeeper.buscar_libro_por_genero(genre)

    @staticmethod
    def new_prestamo(
            fecha: datetime = None,
            id_cliente: int = None,
            nombre: str = None
    ) -> None:
        ControlBookeeper.__bookeeper.new_prestamo(
            fecha,
            id_cliente,
            nombre,
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
    ) -> None:
        ControlBookeeper.__bookeeper.new_libro(
            nombre,
            autores,
            fecha_lanzamiento,
            genero,
            editorial,
            ubicacion
        )

    @staticmethod
    def new_estante(genero: str, max: int, admin: 'administrador') -> None:
        ControlBookeeper.__bookeeper.new_estante(genero, max, admin)

    @staticmethod
    def new_admin(nombre: str, contraseña: str) -> None:
        ControlBookeeper.__bookeeper.new_admin(nombre, contraseña)

    @staticmethod
    def verificar_genero(nombre: str) -> bool:
        return ControlBookeeper.__bookeeper.verificar_genero(nombre)

    @staticmethod
    def cambiar_info(nombre: str = None, password: str = None, segundo: str = None) -> None:
        ControlBookeeper.__bookeeper.cambiar_info(nombre, password, segundo)

    @staticmethod
    def actualizar_todo() -> None:
        ControlBookeeper.__bookeeper.uptade_todo()

    @staticmethod
    def devolder_libro(name_libro: str, name_cliente) -> None:
        libro = ControlBookeeper.__bookeeper.buscar_libro_por_nombre(name_libro) 
        clientes = ControlBookeeper.__bookeeper.clientes
        for cliente in clientes:
            if cliente.nombre == name_cliente:
                cliente.devolver_libro(libro[0])
                break

    @staticmethod
    def get_libros_prestados() -> list['Libro']:
        libros_prestados = []
        for libro in ControlBookeeper.__bookeeper.libros_prestatos():
            libros_prestados.append(libro.libro)
        return libros_prestados
