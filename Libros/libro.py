from datetime import date
import random

class Libro:
    def __init__(self, nombre: str, autores: str, fecha_lanzamiento: date, genero: str, editorial:str, formato: str, ubicacion: str, estado: str):
        self.nombre = nombre
        self.autores = autores
        self.fecha_lanzamiento = fecha_lanzamiento
        self.genero = genero
        self.editorial = editorial
        self.formato = formato
        self.ubicacion = ubicacion
        self.codigo = random.randint(1, 1000)
        self.estado = estado

    def __str__(self):
        return f"{self.nombre}, {self.autores}, ({self.fecha_lanzamiento}), {self.editorial}, {self.formato}, {self.genero}, {self.ubicacion}, {self.estado}"
    
    def __repr__(self):
        return f"{self.nombre} de {', '.join(self.autores)} ({self.fecha_lanzamiento}) - {self.editorial}, {self.formato}, {self.genero}, {self.ubicacion}, {self.estado}"
    
    def __eq__(self, other: "Libro"):
        return self.nombre == other.nombre and self.autores == other.autores and self.fecha_lanzamiento == other.fecha_lanzamiento and self.editorial == other.editorial and self.formato == other.formato and self.genero == other.genero and self.ubicacion == other.ubicacion
    
    def __lt__(self, other: "Libro"):
        return self.fecha_lanzamiento < other.fecha_lanzamiento
    

