from estante_libros import *

class administrador:
    @dispatch(str)
    def __init__(self, nombre: str):
        self.estantes = []
        self.nombre = nombre
        self.prestamos_pendientes = []

    @dispatch(str, list)
    def __init__(self, nombre:str, estantes: list):
        self.estantes = estantes
        self.nombre = nombre
        self.prestamos_pendientes = []

    def agregar_estante(self, estante: 'EstanteDeLibros'):
        self.estantes.append(estante)
        almacenar_estante(estante)

    def quitar_estante(self, estante: 'EstanteDeLibros'):
        self.estantes.remove(estante)
        borrar_un_estante(estante.codigo)

    def buscar_libro_por_nombre(self, nombre):
        for estante in self.estantes:
            libro = estante.buscar_libro_por_nombre(nombre)
            if libro is not None:
                return libro
        return None

    def buscar_libros_por_autor(self, autor):
        libros_encontrados = []
        for estante in self.estantes:
            libros_en_estante = estante.buscar_libros_por_autor(autor)
            libros_encontrados.extend(libros_en_estante)
        return libros_encontrados

    def buscar_libros(self, criterios):
        libros_encontrados = []
        for estante in self.estantes:
            libros_en_estante = estante.buscar(criterios)
            libros_encontrados.extend(libros_en_estante)
        return libros_encontrados

    def __str__(self):
        if len(self.estantes) == 0:
            return "No hay estantes disponibles"
        else:
            estantes_str = "\n".join([f" - {estante.__repr__()}" for estante in self.estantes])
            return f"{self.nombre} con {len(self.estantes)} estantes:\n{estantes_str}"

    def registrar_prestamo(self, usuario, libro):
        if usuario.tiene_libro_prestado(libro):
            print("El usuario ya tiene este libro prestado.")
        else:
            self.prestamos_pendientes.append((usuario, libro))
            print(f"{usuario.nombre} ha prestado el libro {libro.titulo}.")
        
    def registrar_devolucion(self, usuario, libro):
        if not usuario.tiene_libro_prestado(libro):
            print("El usuario no tiene este libro prestado.")
        else:
            self.prestamos_pendientes.remove((usuario, libro))
            print(f"{usuario.nombre} ha devuelto el libro {libro.titulo}.")
    
    def imprimir_prestamos_pendientes(self):
        if len(self.prestamos_pendientes) == 0:
            print("No hay préstamos pendientes.")
        else:
            print("Préstamos pendientes:")
            for (usuario, libro) in self.prestamos_pendientes:
                print(f"- {usuario.nombre} ha prestado el libro {libro.titulo}.")