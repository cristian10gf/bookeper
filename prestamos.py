
from Libros.libro import *
from datetime import datetime
from datetime import date

class Prestamo:

    def __init__(self, usuario, libro: 'Libro', fecha: datetime, devuelto: bool = False, fecha_devolucion: date = None):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        self.devuelto = devuelto
        self.fecha_devolucion = fecha_devolucion
        self.codigo = random.randint(1000, 9999)

    
    def __init__(self, usuario, libro: 'Libro', fecha: datetime, devuelto: bool = False, fecha_devolucion: date = None, codigo: int = None):
        self.usuario = usuario
        self.libro = libro
        self.fecha = fecha
        self.devuelto = devuelto
        self.fecha_devolucion = fecha_devolucion
        self.codigo = codigo

    def __str__(self):
        return f"{self.usuario},{self.libro.codigo},{self.fecha},{self.devuelto},{self.fecha_devolucion},{self.codigo}"
    
    def __repr__(self):
        if self.devuelto == False:
            return f"{self.usuario} presto el libro {self.libro.nombre} -({self.libro.fecha_lanzamiento}) el {self.fecha}, No devuelto"
        else:
            return f"{self.usuario} presto el libro {self.libro.nombre} -({self.libro.fecha_lanzamiento}) el {self.fecha}, devuelto: {self.devuelto}, fecha de devolucion: {self.fecha_devolucion}"
    
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
    archivo = open('Datos\prestamos.txt', 'w')
    for prestamo in prestamos:
        archivo.write(str(prestamo) + "\n")
    archivo.close()