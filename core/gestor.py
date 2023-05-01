from config.config import *


def traer_datos() -> dict:
    info = db()
    todo = {
        'administradores': info.get_admins(),
        'clientes': info.get_clientes(),
        'estantes': info.get_estantes()
    }
    return todo

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
            cl = Cliente(cliente[1], cliente[2], cliente[0])
            self.__clientes.append(cl)

        es = traer_datos()['estantes']
        self.__estantes.append(es)


    def agregar_administrador(self, administrador: 'administrador') -> None:
        self.__administradores.append(administrador)

    def agregar_Cliente(self, cliente: 'Cliente'):
        self.__clientes.append(cliente)

    def agregar_estante(self, estante: 'EstanteDeLibros') -> None:
        self.__estantes.append(estante)

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

book = Bookeeper()
print(book.administradores[0].estantes[0].libros[1].nombre)

