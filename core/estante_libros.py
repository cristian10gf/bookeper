from Libros.libro import *
from Usuarios.admin import administrador

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

    def buscar_libro_por_nombre(self, nombre: str) -> "Libro":
        if len(self.__libros) == 0:
            return None
        else:
            for libro in self.__libros:
                if libro.nombre == nombre:
                    return libro
            return None

    def buscar_libros_por_autor(self, autor) -> list['Libro']:
        libros_encontrados = []
        for libro in self.libros:
            if autor in libro.autores:
                libros_encontrados.append(libro)
        return libros_encontrados

    @property
    def libros(self):
        return self.__libros

    @property
    def codigo(self):
        return self.__codigo

    @property
    def genero(self):
        return self.__genero


        
# crea un archivo para guardar los estantes
def almacenar_estante(estante: EstanteDeLibros) -> None:
    archivo = open("../Datos/estante.txt", "a")
    archivo.write(str(estante) + "\n")
    archivo.close()

@dispatch()
def leer_estantes() -> list['EstanteDeLibros']:
    with open('../Datos/estante.txt', 'r') as archivo:
        lista_estantes = []
        for linea in archivo:
            linea = linea.strip()
            estante = linea.split(',')
            if estante[0] == "[]":
                estante[0] = []
            else:
                estante[0] = estante[0].split('-')
                estante[0].pop(0)
            estante[1] = int(estante[1])
            codigos = []
            for codigo in estante[0]:
                codigos.append(int(codigo))
            estante = EstanteDeLibros(codigos, estante[1], estante[2])
            lista_estantes.append(estante)
    return lista_estantes

@dispatch(str)
def leer_estantes(nombre: str) -> list['EstanteDeLibros']:
    with open('../Datos/estante.txt', 'r') as archivo:
        mis_estantes = []
        for linea in archivo:
            linea = linea.strip()
            estante = linea.split(',')
            if estante[0] == "[]":
                estante[0] = []
            else:
                estante[0] = estante[0].split('-')
                estante[0].pop(0)
            estante[1] = int(estante[1])
            for codigo in estante[0]:
                codigo = int(codigo)
            estante = EstanteDeLibros(estante[0], estante[1], estante[2])
            if estante.admin == nombre:
                mis_estantes.append(estante)
    return mis_estantes

def borrar_estantes() -> None:
    archivo = open("../Datos/estante.txt", "w")
    archivo.write("")
    archivo.close()

def borrar_un_estante(codigo: int) -> None:
    todos_los_estantes = leer_estantes()
    for estante in todos_los_estantes:
        if estante.codigo == codigo:
            todos_los_estantes.remove(estante)
            break
    borrar_estantes()
    for estante in todos_los_estantes:
        almacenar_estante(estante)

def modificar_estante(libro: Libro, codigo: int) -> None:
    act = False
    todos_los_estantes = leer_estantes()
    for estante_actual in todos_los_estantes:
        if estante_actual.codigo == codigo:
            act = True
            break
    if act == False: 
        "No se encontro el estante"
    else:
        borrar_estantes()
        for estante in todos_los_estantes:
            almacenar_estante(estante)