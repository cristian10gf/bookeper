from src.Models.config.config import *
from src.Models.Libros.recomendacio import Recomendacion
import random
info = db()

def traer_datos() -> dict:
    #info = db()
    todo = {
        'administradores': info.get_admins(),
        'clientes': info.get_clientes(),
        'estantes': info.get_estantes(),
        'recomendaciones': info.get_recomendaciones(),
        'prestamos': info.get_prestamos()
    }
    return todo


def guardar_datos(self: 'Bookeeper') -> None:
    #info = db()
    todos_datos = {
        'admins': self.administradores,
        'estantes': self.estantes,
        'libros': [libro for estante in self.estantes for libro in estante.libros],
        'prestamos': [prestamo for cliente in self.clientes for prestamo in cliente.prestamos],
        'clientes': self.clientes,
        'recomendaciones': self.recomendaciones
    }
    info.actualizar(todos_datos)


class Bookeeper:

    def __init__(
            self,
            administradores: list['administrador'] = [],
            clientes: list['Cliente'] = [],
            estantes: list['EstanteDeLibros'] = []
    ) -> None:
        todos_los_datos = traer_datos()
        self.__administradores = administradores
        self.__clientes = clientes
        self.__estantes = estantes
        self.__recomendaciones = todos_los_datos['recomendaciones']

        self.__administradores.extend(todos_los_datos['administradores'])

        self.__clientes.extend(todos_los_datos['clientes'])
        for cliente in self.__clientes:
            for prestamo in todos_los_datos['prestamos']:
                if prestamo.cliente.codigo_Usuario == cliente.codigo_Usuario and prestamo.devuelto == False:
                    cliente.prestamos.append(prestamo)

        self.__estantes = todos_los_datos['estantes']

        prestamos_pendientes = todos_los_datos['prestamos']

        for admin in self.__administradores:
            admin.prestamos_pendientes.extend(prestamos_pendientes)

    def agregar_administrador(self, administrador: 'administrador') -> None:
        self.__administradores.append(administrador)

    def agregar_Cliente(self, cliente: 'Cliente'):
        self.__clientes.append(cliente)

    def agregar_estante(self, estante: 'EstanteDeLibros') -> None:
        self.__estantes.append(estante)

    def get_estante(self, codigo: int) -> 'EstanteDeLibros':
        for estante in self.__estantes:
            if estante.codigo == codigo:
                return estante
        return None

    def buscar_libro_por_autor(self, autor: str) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            if len(estante.buscar_libros_por_autor(autor)) > 0:
                libros.extend(estante.buscar_libros_por_autor(autor))
        return libros

    def buscar_libro_por_nombre(self, nombre: str) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            if len(estante.buscar_libros_por_nombre(nombre)) > 0:
                libros.extend(estante.buscar_libros_por_nombre(nombre))
        return libros

    def buscar_libro_por_genero(self, genero: str) -> list['Libro']:
        libros = []
        for estante in self.__estantes:
            if len(estante.buscar_libros_por_genero(genero)) > 0:
                libros.extend(estante.buscar_libros_por_genero(genero))
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

    @administradores.setter
    def administradores(self, administrador):
        self.__administradores.append(administrador)

    @clientes.setter
    def clientes(self, cliente):
        self.__clientes.append(cliente)

    @estantes.setter
    def estantes(self, estante):
        self.__estantes.append(estante)

    @property
    def recomendaciones(self) -> list['Recomendacion']:
        return self.__recomendaciones

    def verificar_admin(self, username: str, password: str, metodo: int = 1) -> bool:
        for admin in self.__administradores:
            if admin.nombre == username and admin.contrasena == password and metodo == 1:
                return True
            elif admin.nombre == username and metodo == 2:
                return True
        return False

    def verificar_cliente(self, username: str, password: str, metodo: int == 1) -> bool:
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

    def get_libro(self, codigo: int) -> 'Libro':
        for estante in self.__estantes:
            libro = estante.get_libro(codigo)
            if libro is not None:
                return libro
        return None

    def get_prestamos(self, usuario: 'Usuario') -> list['Prestamo']:
        prestamos = []
        if self.verificar_cliente(usuario.nombre, usuario.contrasena, 1):
            for prestamo in usuario.prestamos:
                prestamos.append(prestamo)
        elif self.verificar_admin(usuario.nombre, usuario.contrasena, 1):
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
            if cliente.codigo_Usuario == id:
                return cliente
        return None

    def new_prestamo(
            self,
            fecha: datetime,
            id_cliente: int = None,
            nombre: str = None
    ) -> None:
        libro = self.buscar_libro_por_nombre(nombre)
        cliente = self.get_cliente(id_cliente)
        if libro[0] is not None and cliente is not None:
            prestamo = Prestamo(cliente, libro[0], fecha)
            for admin in self.administradores:
                admin.prestamos_pendientes.append(prestamo)
    
    def new_cliente(self, nombre: str, password: str) -> None:
        cliente = Cliente(nombre, password)
        self.__clientes.append(cliente)
        guardar_datos(self)

    def new_libro(self, nombre: str, autores: str, fecha_lanzamiento: date, genero: str, editorial: str, ubicacion: int) -> bool:
        libro = Libro(nombre, autores, fecha_lanzamiento, genero, editorial, ubicacion)
        for estante in self.__estantes:
            if estante.codigo == ubicacion:
                estante.libros.append(libro)
                return True
                break
        return False
        

    def generate_recomendacion(self, cliente: Cliente) -> bool:
        if len(traer_datos()['prestamos']) > 4:
            libros_prestados = []
            for prestamo in traer_datos()['prestamos']:
                if prestamo.cliente.id == cliente.id:
                    libros_prestados.append(prestamo.libro)
            genero = random.choice(libros_prestados)
            libros_genero = [libro for libro in self.get_libros() if libro.genero == genero.genero]
            libro = random.choice(libros_genero)
            while libro in genero:
                libro = random.choice(libros_genero)
            else:
                pass
            recomendacion = Recomendacion(libro, cliente)
            self.__recomendaciones.append(recomendacion)
            return True
        else:
            return False

    def new_admin(self, nombre: str, password: str) -> None:
        admin = administrador(nombre, password)
        self.__administradores.append(admin)
        guardar_datos(self)

    def new_estante(self, genero: str, numero: int, admin: 'administrador'):
        estante = EstanteDeLibros([], admin, genero, numero)
        self.__estantes.append(estante)

    def verificar_genero(self, genero: str) -> bool:
        for estante in self.__estantes:
            if estante.genero == genero:
                return True
        return False

    def cambiar_info(self, nombre: str, password: str, nombre2: str) -> None:
        if self.verificar_admin(nombre, password, 2) == True and self.verificar_admin(nombre2, None, 2) == False:
            for admin in self.__administradores:
                if password == None:
                    if admin.nombre == nombre:
                        admin.nombre = nombre2
                elif nombre == None:
                    if admin.contrasena == password:
                        admin.contrasena = nombre2
                else:
                    if admin.nombre == nombre:
                        admin.nombre = nombre2
                        admin.contrasena = password
        elif self.verificar_cliente(nombre, password, 2) == True and self.verificar_cliente(nombre2, None, 2) == False:
            for cliente in self.__clientes:
                if password == None:
                    if cliente.nombre == nombre:
                        cliente.nombre = nombre2
                elif nombre == None:
                    if cliente.contrasena == password:
                        cliente.contrasena = nombre2
                else:
                    if cliente.nombre == nombre:
                        cliente.nombre = nombre2
                        cliente.contrasena = password
        guardar_datos(self)

    def uptade_todo(self):
        guardar_datos(self)

    def libros_prestatos(self) -> list['Prestamo']:
        return self.administradores[0].ver_libros_prestados()
    