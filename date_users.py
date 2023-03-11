# crea un objeto de clase dato usuario que reciba un nombre de usuario, contraseña, tipo de usuario ademas de un codigo unico
class DatoUsuario:
    def __init__(self, nombre_usuario, contraseña, tipo_usuario, codigo):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario
        self.codigo = codigo

# ahora crea un metodo para almacenar un usuario en un archivo de texto


    def almacenar_usuario(self):
        with open('usuarios.txt', 'a') as archivo:
            archivo.write(f'{self.nombre_usuario},{self.contraseña},{self.tipo_usuario},{self.codigo}')


# crea un archivo de texto para almacenar los usuarios
with open('usuarios.txt', 'w') as archivo:
    archivo.write('nombre_usuario,contraseña,tipo_usuario,codigo')

# crea una funcion para leer los datos de un archivo de texto y guardarlos en un diccionario
def leer_archivo():
    with open('usuarios.txt', 'r') as archivo:
        for linea in archivo:
            usuarios = {}
            linea = linea.strip()
            nombre_usuario, contraseña, tipo_usuario, codigo = linea.split(',')
            usuarios[nombre_usuario] = DatoUsuario(nombre_usuario, contraseña, tipo_usuario, codigo)
    return usuarios

# crea una funcion para verificar si un usuario existe en el archivo de texto
def verificar_usuario(nombre_usuario):
    usuarios = leer_archivo()
    if nombre_usuario in usuarios:
        return True
    else:
        return False
    
# crea una funcion para verificar si la contraseña es correcta
def verificar_contraseña(nombre_usuario, contraseña):
    usuarios = leer_archivo()
    if usuarios[nombre_usuario].contraseña == contraseña:
        return True
    else:
        return False

# crea una funcion para verificar si el tipo de usuario es correcto
def verificar_tipo_usuario(nombre_usuario, tipo_usuario):
    usuarios = leer_archivo()
    if usuarios[nombre_usuario].tipo_usuario == tipo_usuario:
        return True
    else:
        return False


        