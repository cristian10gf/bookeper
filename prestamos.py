
from Libros.libro import *
from datetime import datetime
from datetime import date

class Prestamo:

    def __init__(self, usuario, libro: 'Libro', fecha: datetime, codigo: int, devuelto: bool = False, fecha_devolucion: date = None):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        self.devuelto = devuelto
        self.fecha_devolucion = fecha_devolucion
        self.codigo = codigo

    
    def __init__(self, usuario, libro: 'Libro', fecha: datetime, devuelto: bool = False, fecha_devolucion: date = None):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        self.devuelto = devuelto
        self.fecha_devolucion = fecha_devolucion
        self.codigo = random.randint(1, 1000)

    def __str__(self):
        return f"{self.usuario},{self.libro.codigo},{self.fecha},{self.devuelto},{self.fecha_devolucion},{self.codigo}"
    
    def __repr__(self):
        if self.devuelto == False:
            return f"{self.usuario} presto el libro {self.libro} el {self.fecha}, No devuelto"
        else:
            return f"{self.usuario} presto el libro {self.libro} el {self.fecha}, devuelto: {self.devuelto}, fecha de devolucion: {self.fecha_devolucion}"
    
    def devolver(self):
        self.devuelto = True
        self.fecha_devolucion = date.today()
        modificar_prestamo(self)


def almacenar_prestamo(prestamo: 'Prestamo') -> None:
    archivo = open('Datos\prestamos.txt', 'a')
    archivo.write(str(prestamo) + "\n")
    archivo.close()

def leer_prestamos() -> list['Prestamo']:
    prestamos = []
    archivo = open('Datos\prestamos.txt', 'r')
    for linea in archivo:
        datos = linea.strip().split(',')
        datos[2] = date.fromisoformat(datos[2])
        prestamos.append(Prestamo(datos[0], datos[1], datos[2]))
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
    archivo = open('Datos\prestamos.txt', 'w')
    for prestamo in prestamos:
        archivo.write(str(prestamo) + "\n")
    archivo.close()