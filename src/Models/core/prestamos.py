#from Libros.libro import Libro
from datetime import datetime
from datetime import date

class Prestamo:
    __id = 1
    def __init__(
            self,
            cliente: 'Cliente',
            libro: 'Libro',
            fecha_prestamo: datetime = datetime.now(),
            fecha_devolucion: datetime = None,
            codigo:int = None,
            devuelto: bool = False
    ) -> None:
        self.__cliente = cliente
        self.__cliente.prestamos.append(self)
        self.__libro = libro
        self.__libro.estado = self
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
        self.__codigo = codigo
        self.__devuelto = devuelto


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
    
    @property
    def devuelto(self) -> bool:
        return self.__devuelto
    
    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion: datetime) -> None:
        self.__fecha_devolucion = fecha_devolucion

    def devolver(self) -> None:
        self.__libro.estado = None
        self.__fecha_devolucion = datetime.now()
