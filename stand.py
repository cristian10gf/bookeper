import random, Libros.libro as libro
class EstanteDeLibros:
    def __init__(self, libros = None or libro.Libro, admin = None):
        if libros is None:
            self.libros = []
        else:
            self.libros = libros
        self.admin = admin
        self.codigo = random.randint(1, 100)

    def agregar_libro(self, libro: "libro"):
        self.libros.append(libro)

    def quitar_libro(self, libro):
        self.libros.remove(libro)

    def buscar_libro_por_nombre(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre:
                return libro
        return None

    def buscar_libros_por_autor(self, autor):
        libros_encontrados = []
        for libro in self.libros:
            if autor in libro.autores:
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar(self, criterios):
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

    def __str__(self):
        if len(self.libros) == 0:
            return "Estante vacío"
        else:
            libros_str = "\n".join([f" - {libro}" for libro in self.libros])
            return f"Estante con {len(self.libros)} libros:\n{libros_str}"
        
