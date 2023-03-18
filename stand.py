import random
from Libros.libro import Libro as libro
from multipledispatch import dispatch

class EstanteDeLibros:
    
    @dispatch(list or libro, str)
    def __init__(self, libros: list or libro, admin: str):
        if libros is None:
            self.libros = []
        else:
            self.libros = libros
        self.admin = admin
        self.codigo = random.randint(1, 100)

    @dispatch(list or libro, int, str)
    def __init__(self, libros: list or libro, codigo: int, admin: str):
        if libros is None:
            self.libros = []
        else:
            self.libros = libros
        self.admin = admin
        self.codigo = codigo

    
    def agregar_libro(self, libro: "libro") -> None:
        self.libros.append(libro)

    def quitar_libro(self, libro) -> None:
        self.libros.remove(libro)

    def buscar_libro_por_nombre(self, nombre) -> "libro":
        for libro in self.libros:
            if libro.nombre == nombre:
                return libro
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
        if len(self.libros) == 0:
            return f"Estante vacio,{self.codigo},{self.admin}"
        elif self.libros == "Estante vacio":
            return f"Estante vacio,{self.codigo},{self.admin}"
        else:
            libros_str = "\n".join([f" -{libro.codigo}" for libro in self.libros])
            return f"Estante con {len(self.libros)} libros:,\n{libros_str},{self.codigo},{self.admin}"
        
    def __repr__(self) -> str:
        if len(self.libros) == 0:
            return f"Estante vacio,{self.admin}"
        elif self.libros == "Estante vacio":
            return f"Estante vacio,{self.admin}"
        else:
            libros_str = "\n".join([f" -{libro}" for libro in self.libros])
            return f"Estante con {len(self.libros)} libros:,{libros_str},{self.admin}"
        
# crea un archivo para guardar los estantes
def almacenar_estante(estante: EstanteDeLibros) -> None:
    archivo = open("estante.txt", "a")
    archivo.write(str(estante) + "\n")
    archivo.close()

def leer_estantes() -> list:
    with open('estante.txt', 'r') as archivo:
        lista_estantes = []
        for linea in archivo:
            linea = linea.strip()
            estante = linea.split(',')
            if estante[0] == "Estante vacio":
                estante[0] = []
            estante[1] = int(estante[1])
            estante = EstanteDeLibros(estante[0], estante[1], estante[2])
            lista_estantes.append(estante)
    return lista_estantes

def borrar_estante() -> None:
    archivo = open("estante.txt", "w")
    archivo.write("")
    archivo.close()

def modificar_estante(libro: libro, codigo: int) -> None:
    act = False
    todos_los_estantes = leer_estantes()
    for estante_actual in todos_los_estantes:
        if estante_actual.codigo == codigo:
            estante_actual.agregar_libro(libro)
            act = True
            break
    if act == False: 
        "No se encontro el estante"
    else:
        borrar_estante()
        for estante in todos_los_estantes:
            almacenar_estante(estante)