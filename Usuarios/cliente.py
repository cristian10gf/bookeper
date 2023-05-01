from core.prestamos import *
from Usuarios.usuarios import Usuario
from Files.file_manager import FileManager
from multipledispatch import dispatch

class Cliente(Usuario):
    def __init__(self, nombre: str, contraseña: str):
        super().__init__(nombre, contraseña)
        self.__prestamos: list['Prestamo'] = []

    def prestar_libro(self, libro: 'Libro') -> None:
        for prestamo in self.__prestamos:
            if prestamo.libro.codigo == libro.codigo:
                print("Ya tienes este libro prestado.")
                return
        prestamo = Prestamo(self, libro)

    def devolver_libro(self, libro: 'Libro'):
        for prestamo in self.__prestamos:
            if prestamo.libro.codigo == libro.codigo:
                prestamo.devolver()
                self.__prestamos.remove(prestamo)
                return
        print("No tienes este libro prestado.")

    def ver_libros_prestados(self) -> list['Prestamo']:
        return self.__prestamos

    def buscar_libro_por_nombre(self, nombre: str) -> 'Libro':
        for estante in self.biblioteca.estantes:
            libro = estante.buscar_libro_por_nombre(nombre)
            if libro is not None:
                return libro
        return None

    @property
    def prestamos(self):
        return self.__prestamos

    @prestamos.setter
    def prestamos(self, prestamo):
        self.__prestamos.append(prestamo)


todos_usuarios = FileManager("usuarios.txt").generate_path()


# crea un objeto de clase dato usuario que reciba un nombre de usuario, contraseña, tipo de usuario ademas de un codigo unico
class DatoUsuario:
    @dispatch(str, str, str, int)
    def __init__(self, nombre_usuario, contraseña, tipo_usuario, codigo):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario
        self.codigo = codigo

    @dispatch(str, str, str)
    def __init__(self, nombre_usuario, contraseña, tipo_usuario):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario
        self.codigo = random.randint(1000, 9999)

    def __str__(self):
        return f'{self.nombre_usuario},{self.contraseña},{self.tipo_usuario},{self.codigo}'

    # ahora crea un metodo para almacenar un usuario en un archivo de texto
    def almacenar_usuario(self):
        with open(todos_usuarios, 'a') as archivo:
            archivo.write(f'{self}\n')


# crea una funcion para leer los datos de un archivo de texto y guardarlos en un diccionario
def leer_archivo() -> list['DatoUsuario']:
    lista_usuarios = []
    with open(todos_usuarios, 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            nombre_usuario, contraseña, tipo_usuario, codigo = linea.split(',')
            user = DatoUsuario(nombre_usuario, contraseña, tipo_usuario, int(codigo))
            lista_usuarios.append(user)
    return lista_usuarios


# crea una funcion para verificar si un usuario existe en el archivo de texto
def verificar_usuario(nombre_usuario: str) -> bool:
    usuarios = leer_archivo()
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario:
            return True
            break
    return False


# crea una funcion para verificar si la contraseña es correcta
def verificar_contraseña(nombre_usuario, contraseña) -> bool:
    usuarios = leer_archivo()
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario:
            if usuario.contraseña == contraseña:
                return True
                break
    return False


# crea una funcion para verificar si el tipo de usuario es correcto
def verificar_tipo_usuario(nombre_usuario, tipo_usuario) -> bool:
    usuarios = leer_archivo()
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario:
            if usuario.tipo_usuario == tipo_usuario:
                return True
    return False


def get_condigo_usuario(nombre_usuario) -> int:
    usuarios = leer_archivo()
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario:
            return usuario.codigo


def agregar_usuario() -> None:
    nombre_usuario = input('Ingrese el nombre de usuario: ')
    contraseña = input('Ingrese la contraseña: ')
    tipo_usuario = input('Ingrese el tipo de usuario: ')
    codigo = input('Ingrese el codigo: ')
    usuario = DatoUsuario(nombre_usuario, contraseña, tipo_usuario, codigo)
    usuario.almacenar_usuario()
    print('Usuario agregado con exito')
