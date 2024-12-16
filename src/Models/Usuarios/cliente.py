import random
from src.Models.Libros.libro import Libro
from src.Models.Libros.recomendacio import Recomendacion
from src.Models.core.prestamos import Prestamo
from src.Models.Usuarios.usuarios import Usuario

class Cliente(Usuario):
    def __init__(self, nombre: str, contraseña: str, codigo_usuario: int = random.randint(1000, 9999)):
        super().__init__(nombre, contraseña, codigo_usuario)
        self.__prestamos: list['Prestamo'] = []
        self.__recomendaciones: list['Recomendacion'] = []

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
                return
        print("No tienes este libro prestado.")
    
    def add_prestamo(self, prestamo: 'Prestamo'):
        self.__prestamos.append(prestamo)
    
    def eliminar_recomendacion(self, recomendacion: 'Recomendacion') -> None:
        self.__recomendaciones.remove(recomendacion)

    def agregar_recomendacion(self, recomendacion: 'Recomendacion') -> None:
        self.__recomendaciones.append(recomendacion)
        
    @property
    def prestamos(self) -> list['Prestamo']:
        return self.__prestamos

    @prestamos.setter
    def prestamos(self, prestamo):
        self.__prestamos.append(prestamo)

    @property
    def recomendaciones(self):
        return self.__recomendaciones