

class Recomendacion:
    def __init__(self, id: int, libro: 'Libro', usuario: 'Ciente', fecha: 'datetime', descripcion: str):
        self.__id = id
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha = fecha
        self.__descripcion = descripcion

    @property
    def id(self):
        return self.__id
    
    @property
    def libro(self):
        return self.__libro
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def fecha(self):
        return self.__fecha
    
