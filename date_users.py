# crea un objeto de clase dato usuario que reciba un nombre de usuario, contraseña, tipo de usuario ademas de un codigo unico
class DatoUsuario:
    def __init__(self, nombre_usuario, contraseña, tipo_usuario, codigo):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario
        self.codigo = codigo
    
    def __str__(self):
        return f'{self.nombre_usuario},{self.contraseña},{self.tipo_usuario},{self.codigo}'

    # ahora crea un metodo para almacenar un usuario en un archivo de texto
    def almacenar_usuario(self):
        with open('usuarios.txt', 'a') as archivo:
            archivo.write(f'{self.nombre_usuario},{self.contraseña},{self.tipo_usuario},{self.codigo}\n')

# crea una funcion para leer los datos de un archivo de texto y guardarlos en un diccionario
def leer_archivo():
    lista_usuarios = []
    with open('usuarios.txt', 'r') as archivo:
        for linea in archivo:
            usuarios = {
                "nombre_usuario": "",
                "contraseña": "",
                "tipo_usuario": "",
                "codigo": ""
            }
            linea = linea.strip()
            nombre_usuario, contraseña, tipo_usuario, codigo = linea.split(',')
            user = DatoUsuario(nombre_usuario, contraseña, tipo_usuario, codigo)
            usuarios["nombre_usuario"] = user.nombre_usuario
            usuarios["contraseña"] = user.contraseña
            usuarios["tipo_usuario"] = user.tipo_usuario
            usuarios["codigo"] = user.codigo
            lista_usuarios.append(usuarios)
    return lista_usuarios

# crea una funcion para verificar si un usuario existe en el archivo de texto
def verificar_usuario(nombre_usuario):
    usuarios = leer_archivo()
    for usuario in usuarios:
        if usuario["nombre_usuario"] == nombre_usuario:
            return True
            break
    return False
    
# crea una funcion para verificar si la contraseña es correcta
def verificar_contraseña(nombre_usuario, contraseña):
    usuarios = leer_archivo()
    for usuario in usuarios:
        if usuario["nombre_usuario"] == nombre_usuario:
            if usuario["contraseña"] == contraseña:
                return True
                break
    return False

# crea una funcion para verificar si el tipo de usuario es correcto
def verificar_tipo_usuario(nombre_usuario, tipo_usuario):
    usuarios = leer_archivo()
    for usuario in usuarios:
        if usuario["nombre_usuario"] == nombre_usuario:
            if usuario["tipo_usuario"] == tipo_usuario:
                return True
    return False

def agregar_usuario():
    nombre_usuario = input('Ingrese el nombre de usuario: ')
    contraseña = input('Ingrese la contraseña: ')
    tipo_usuario = input('Ingrese el tipo de usuario: ')
    codigo = input('Ingrese el codigo: ')
    usuario = DatoUsuario(nombre_usuario, contraseña, tipo_usuario, codigo)
    usuario.almacenar_usuario()
    print('Usuario agregado con exito')
        