
#from Libros.libro import Libro
from datetime import datetime
from datetime import date
import random

class Prestamo:

    def __init__(
            self,
            cliente: 'Cliente',
            libro: 'Libro',
            fecha_prestamo: datetime,
            fecha_devolucion: datetime = None,
            devuelto: bool = False,
            codigo: int = None
    ) -> None:
        self.__cliente = cliente
        self.__cliente.add_prestamo(self)
        self.__libro = libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
        if codigo is None:
            self.__codigo = random.randint(1000, 9999)
        else:
            self.__codigo = codigo
        self.__devuelto = devuelto
        self.libro.prestar(self)


    @property
    def libro(self) -> 'Libro':
        return self.__libro
    
    @property
    def cliente(self) -> 'Cliente':
        return self.__cliente

    @property
    def fecha_devolucion(self) -> datetime:
        return self.__fecha_devolucion

    @property
    def codigo(self) -> int:
        return self.__codigo
    
    @property
    def fecha_prestamo(self) -> datetime:
        return self.__fecha_prestamo
    
    @fecha_prestamo.setter
    def fecha_prestamo(self,fecha: datetime):
        self.__fecha_prestamo = fecha
    
    @property
    def devuelto(self) -> bool:
        return self.__devuelto

    @devuelto.setter
    def devuelto(self, devuelto: bool) -> None:
        self.__devuelto = devuelto
    
    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion: datetime) -> None:
        self.__fecha_devolucion = fecha_devolucion

    def devolver(self) -> None:
        self.__cliente.prestamos.remove(self)
        self.__libro.devolver()
        self.__fecha_devolucion = datetime.now()
        self.__devuelto = True
