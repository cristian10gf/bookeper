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
            fecha_devolucion: datetime = None
    ) -> None:
        self.__cliente = cliente
        self.__cliente.prestamos.append(self)
        self.__libro = libro
        self.__libro.estado = self
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
        self.__codigo = Prestamo.__id
        Prestamo.__id += 1

    @property
    def libro(self) -> 'Libro':
        return self.__libro

    @property
    def fecha_devolucion(self) -> datetime:
        return self.__fecha_devolucion

    @property
    def codigo(self) -> int:
        return self.__codigo

    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion: datetime) -> None:
        self.__fecha_devolucion = fecha_devolucion

    def devolver(self) -> None:
        self.__libro.estado = None
        self.__fecha_devolucion = datetime.now()




def almacenar_prestamo(prestamo: 'Prestamo') -> None:
    archivo = open('../Datos/prestamos.txt', 'a')
    archivo.write(str(prestamo) + "\n")
    archivo.close()

def leer_prestamos() -> list['Prestamo']:
    prestamos = []
    archivo = open('../Datos/prestamos.txt', 'r')
    for linea in archivo:
        datos = linea.strip().split(',')
        datos[2] = datetime.fromisoformat(datos[2])
        datos[1] = retornar_libro(int(datos[1]))
        datos[0] = int(datos[0])
        if datos[3] == "False":
            datos[3] = False
        else:
            datos[3] = True
        if datos[4] == "None":
            datos[4] = None
        else:
            datos[4] = datetime.fromisoformat(datos[4])
        datos[5] = int(datos[5])
        prestamos.append(Prestamo(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5]))
    archivo.close()
    return prestamos

def buscar_prestamo(codigo: int) -> 'Prestamo':
    prestamos = leer_prestamos()
    for prestamo in prestamos:
        if prestamo.codigo == codigo:
            return prestamo
    return None

def modificar_prestamo(prestamo: 'Prestamo') -> None:
    prestamos = leer_prestamos()
    for i in range(len(prestamos)):
        if prestamos[i].codigo == prestamo.codigo:
            prestamos[i] = prestamo
            break
    archivo = open('../Datos/prestamos.txt', 'w')
    for prestamo in prestamos:
        archivo.write(str(prestamo) + "\n")
    archivo.close()