

class Recomendacion:
    __id: int = 0

    @dispatch(int, 'Libro', 'Cliente', bool)
    def __init__(self, id: int, libro: 'Libro', usuario: 'Ciente', prestamo: bool = False):
        self.__id = id
        self.__libro = libro
        self.__usuario = usuario
        self.__usuario.agregar_recomendacion(self)
        self.__prestamo = prestamo

    @dispatch('Libro', 'Cliente', bool)
    def __init__(self, libro: 'Libro', usuario: 'Ciente', prestamo: bool = False):
        self.__id = Recomendacion.__id
        Recomendacion.__id += 1
        self.__libro = libro
        self.__usuario = usuario
        self.__prestamo = prestamo

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
    def prestamo(self):
        return self.__prestamo
    
