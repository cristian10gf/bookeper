import random
from Libros.libro import *
from multipledispatch import dispatch

class EstanteDeLibros:
    @dispatch(list, str)
    def __init__(self, libros: list, admin: str):
        if libros is None or len(libros) == 0:
            self.libros = []
        else:
            self.libros = libros
        self.admin = admin
        self.codigo = random.randint(1, 100)

    @dispatch(list, int, str)
    def __init__(self, libros: list, codigo: int, admin: str):
        if libros is None or len(libros) == 0:
            self.libros = []
        else:
            self.libros = libros
        self.admin = admin
        self.codigo = codigo

    def agregar_libro(self, libro: "Libro", tipo: bool) -> None:
        # tipo = True si es un libro nuevo, False si es un libro que ya existe
        self.libros.append(libro.codigo)
        if tipo:
            almacenar_libro(libro)
        modificar_estante(libro, libro.ubicacion)

    def quitar_libro(self, libro) -> None:
        self.libros.remove(libro)
        modificar_estante(libro, libro.ubicacion)

    def buscar_libro_por_nombre(self, nombre: str) -> "Libro":
        if len(self.libros) == 0:
            return None
        else: 
            for libro in self.libros:
                libro_a_buscar = retornar_libro(int(libro))
                if libro_a_buscar.nombre == nombre:
                    return libro_a_buscar
            return None

    def buscar_libros_por_autor(self, autor) -> list:
        libros_encontrados = []
        for libro in self.libros:
            if autor in libro.autores:
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar(self, criterios) -> list:
        libros_encontrados = []
        for libro in self.libros:
            cumple_criterios = True
            for clave, valor in criterios.items():
                if getattr(libro, clave, None) != valor:
                    cumple_criterios = False
                    break
            if cumple_criterios:
                libros_encontrados.append(libro)
        return libros_encontrados

    def __str__(self) -> str:
        if len(self.libros) == 0 or self.libros == []:
            return f"[],{self.codigo},{self.admin}"
        else:
            libros_str = ""
            for libro in self.libros:
                libros_str = libros_str + f"-{libro}"
            return f"{libros_str},{self.codigo},{self.admin}"
        
    def __repr__(self) -> str:
        if len(self.libros) == 0 or self.libros == []:
            return f"Estante vacio, admim:{self.admin}"
        else:
            libros_str = ""
            for libro in self.libros:
                libros_str = libros_str + f"-{libro}"
            return f"Estante con {len(self.libros)} libros:{libros_str}, admin:{self.admin}"
        
# crea un archivo para guardar los estantes
def almacenar_estante(estante: EstanteDeLibros) -> None:
    archivo = open("Datos\estante.txt", "a")
    archivo.write(str(estante) + "\n")
    archivo.close()

@dispatch()
def leer_estantes() -> list['EstanteDeLibros']:
    with open('Datos\estante.txt', 'r') as archivo:
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
    with open('Datos\estante.txt', 'r') as archivo:
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
    archivo = open("Datos\estante.txt", "w")
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