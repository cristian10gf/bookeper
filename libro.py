from datetime import date

class Libro:
    def __init__(self, nombre: str, autores, fecha_lanzamiento: date, editorial:str, formato, ubicacion: str, codigo: int):
        self.nombre = nombre
        self.autores = autores
        self.fecha_lanzamiento = fecha_lanzamiento
        self.editorial = editorial
        self.formato = formato
        self.ubicacion = ubicacion
        self.codigo = codigo

    def __str__(self):
        return f"{self.nombre} de {', '.join(self.autores)} ({self.fecha_lanzamiento}) - {self.editorial}, {self.formato}"