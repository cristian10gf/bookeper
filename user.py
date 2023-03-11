class Usuario:
    def __init__(self, nombre, correo_electronico):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro in self.libros_prestados:
            print("Ya tienes este libro prestado.")
        else:
            self.libros_prestados.append(libro)
            libro.prestar()
            print(f"{self.nombre} ha prestado el libro {libro.titulo}.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            libro.devolver()
        else:
            print("No tienes este libro prestado.")

    def tiene_libro_prestado(self, libro):
        return libro in self.libros_prestados

    def imprimir_libros_prestados(self):
        if len(self.libros_prestados) == 0:
            print(f"{self.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:
                print(f"- {libro.titulo}")

    @staticmethod
    def libros_prestados(usuarios):
        libros_prestados = []
        for usuario in usuarios:
            libros_prestados.extend(usuario.libros_prestados)
        return libros_prestados

    def __str__(self):
        libros_prestados_str = ", ".join([libro.titulo for libro in self.libros_prestados])
        return f"{self.nombre} ({self.correo_electronico}): {libros_prestados_str}"