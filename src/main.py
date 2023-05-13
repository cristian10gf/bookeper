from Models.Usuarios.cliente import *
import Libros.libro as libro
from core import estante_libros
from Usuarios.admin import administrador

def buscar_libro_general(nombre_libro: str) -> libro.Libro:
    estantes = estante_libros.leer_estantes()
    for estante in estantes:
        libro_encontrado = estante.buscar_libro_por_nombre(nombre_libro)
        if libro_encontrado == None:
            continue
        elif libro_encontrado.nombre == nombre_libro:
            return libro_encontrado
    return None

def main() -> None:
    bloqueo = False
    with open("Datos\sesion.txt", "r") as archivo:
        for linea in archivo:
            if linea != "":
                bloqueo = True
    act = True
    print("inicio app")
    print("bienvenido a bookeeper")
    while act:
        if bloqueo == False:
            print("que desea hacer?")
            print("1. acceder \n2. crear cuenta \n3. salir")
            opcion = input("ingrese una opcion: ")
            sesion_activa = False
        else: opcion = "1"
        if opcion == "1":
            # verificar si hay una sesion activa
            archivo = open("Datos\sesion.txt", "r")
            sesion = archivo.read()
            archivo.close()
            if sesion != "":
                sesion = sesion.split(",")
                nombre_usuario = sesion[0]
                contraseña = sesion[1]
                tipo_usuario = sesion[2]
                sesion_activa = True
                bloqueo = True
            if sesion_activa == False:
                nombre_usuario = input("ingrese su nombre de usuario: ")
                contraseña = input("ingrese su contraseña: ")
                tipo_usuario = input("ingrese su tipo de usuario: admin o usuario: ")
            if verificar_usuario(nombre_usuario) and verificar_contraseña(nombre_usuario, contraseña) and verificar_tipo_usuario(nombre_usuario, tipo_usuario):
                print("acceso concedido")
                # guardar la lista en un archivo
                sesion = [nombre_usuario, contraseña, tipo_usuario]
                with open("Datos\sesion.txt", "w") as archivo:
                    archivo.write(str(sesion[0])+ "," + str(sesion[1]) + "," + str(sesion[2]))
                if tipo_usuario == "admin":
                    mis_estantes = estante_libros.leer_estantes(nombre_usuario)
                    usuario_admin = administrador(nombre_usuario,mis_estantes)
                    print("bienvenido administrador,", usuario_admin)
                    print("que desea hacer?")
                    opc = 0
                    while opc != 9:
                        opc = int(input("1. agregar estante \n2. agregar libro \n3. eliminar estante \n4. prestar libro \n5. ver libros prestados \n6. cerrar sesion \n7. ver todos los libros \n8. ver todos los estantes \n9. salir\n"))
                        if opc == 1:
                            libros = []	
                            estante_nuevo = estante_libros.EstanteDeLibros(libros, usuario_admin.nombre)
                            print(estante_nuevo)
                            usuario_admin.agregar_estante(estante_nuevo)
                        elif opc == 2:
                            nombre_libro = input("ingrese el nombre del libro: ")
                            autor_libro = input("ingrese el autor o los autores del libro: ")
                            año_libro = int(input("ingrese el año de lanzamiento del libro: "))
                            formato_libro = input("ingrese el formato del libro: ")
                            editorial_libro = input("ingrese la editorial del libro: ")
                            ubicacion_libro = int(input("ingrese la ubicacion del libro(estante en el que se desea ingresar): "))
                            genero_libro = input("ingrese el genero del libro: ")
                            estado_libro = "disponible"
                            libro_nuevo = libro.Libro(nombre_libro, autor_libro, año_libro, genero_libro, editorial_libro, formato_libro,ubicacion_libro, estado_libro)
                            for estante in usuario_admin.estantes:
                                if estante.codigo == ubicacion_libro:
                                    estante.agregar_libro(libro_nuevo)
                        elif opc == 3:
                            print("eliminar estante")
                            codigo_estante = int(input("escriba el codigo del estante que desea eliminar: "))
                            for estante in usuario_admin.estantes:
                                if estante.codigo == codigo_estante:
                                    usuario_admin.quitar_estante(estante)
                        elif opc == 4:
                            print("prestar libro")
                            nombre_libro = input("ingrese el nombre del libro que desea prestar: ")
                            libro_a_prestar = buscar_libro_general(nombre_libro)
                            usuario_a_prestar = input("ingrese el nombre del usuario al que desea prestar el libro: ")
                            codigo_usuario = get_condigo_usuario(usuario_a_prestar)
                            if codigo_usuario == None:
                                print("el usuario no existe")
                                break
                            elif libro_a_prestar == None:
                                print("el libro no existe")
                                break
                            elif libro_a_prestar.estado == "prestado":
                                print("el libro ya esta prestado")
                                break
                            else:
                                prestamo_nuevo = Prestamo(codigo_usuario, libro_a_prestar, datetime.datetime.now(), False, None, random.randint(1000, 9999))
                                almacenar_prestamo(prestamo_nuevo)
                                libro_a_prestar.prestar()
                                print("prestamo realizado")
                        elif opc == 5:
                            print("ver libros prestados")
                            prestamos_totales = leer_prestamos()
                            print(prestamos_totales)
                        elif opc == 6:
                            sesion_activa = False
                            print("adios")
                            bloqueo = False
                            # crea un archivo en blanco llamado sesion.txt
                            archivo = open("Datos\sesion.txt", "w")
                            archivo.write("")
                            archivo.close()
                            break
                        elif opc == 7:
                            print("ver todos los libros")
                            todos = libro.leer_archivo()
                            print(todos)
                        elif opc == 8:
                            print("ver todos los estantes")
                            todos = estante_libros.leer_estantes()
                            print(todos)
                        elif opc == 9:
                            act = False
                        else:
                            print("opcion invalida")
                elif tipo_usuario == "usuario":
                    codigo_usuario = get_condigo_usuario(nombre_usuario)
                    usuario = Usuario(nombre_usuario, "correo", codigo_usuario)
                    print("bienvenido usuario")
                    print("que desea hacer?")
                    opc = 0
                    while opc != 8:
                        opc = int(input("1. buscar libro \n2. ver libros prestados \n3. devolver libro \n4. ver estantes \n5. ver libros \n6. cerrar sesion \n7. prestar libro\n8. salir\n"))
                        if opc == 1:
                            print("buscar libro")
                            busqueda = input("ingrese el nombre del libro que desea buscar: ")
                            buscar = buscar_libro_general(busqueda)
                            print(buscar.__repr__())
                        elif opc == 2:
                            print("ver libros prestados")
                            usuario.imprimir_libros_prestados()
                        elif opc == 3:
                            print("devolver libro")
                            nombre_libro = input("ingrese el nombre del libro que desea devolver: ")
                            libro_a_devolver = buscar_libro_general(nombre_libro)
                            usuario.devolver_libro(libro_a_devolver)
                            estantes = estante_libros.leer_estantes()
                            for estante in estantes:
                                if estante.codigo == libro_a_devolver.ubicacion:
                                    estante.agregar_libro(libro_a_devolver ,False)
                        elif opc == 4:
                            print("ver estantes")
                            print("estos son todos los estantes con sus libros")
                            print(estante_libros.leer_estantes())
                        elif opc == 5:
                            print("ver libros")
                            print("estos son todos los libros")
                            for estante in estante_libros.leer_estantes():
                                for libro in estante.libros:
                                    print(retornar_libro(libro).__repr__())
                        elif opc == 6:
                            sesion_activa = False
                            print("adios")
                            bloqueo = False
                            # crea un archivo en blanco llamado sesion.txt
                            archivo = open("Datos\sesion.txt", "w")
                            archivo.write("")
                            archivo.close()
                            break
                        elif opc == 7:
                            print("prestar libro")
                            nombre_libro = input("ingrese el nombre del libro que desea prestar: ")
                            libro_a_prestar = buscar_libro_general(nombre_libro)
                            usuario.prestar_libro(libro_a_prestar)
                            estantes = estante_libros.leer_estantes()
                            for estante in estantes:
                                if estante.codigo == libro_a_prestar.ubicacion:
                                    estante.quitar_libro(libro_a_prestar)
                            print("el libro ha sido prestado")
                        elif opc == 8:
                            act = False
                        else:
                            print("opcion invalida")
            else:
                print("acceso denegado")
        elif opcion == "2":
            print("crear cuenta")
            nombre_usuario = input("ingrese su nombre de usuario: ")
            contraseña = input("ingrese su contraseña: ")
            tipo_usuario = input("ingrese su tipo de usuario: amdmin o usuario: ")
            usuario_nuevo = DatoUsuario(nombre_usuario, contraseña, tipo_usuario)
            usuario_nuevo.almacenar_usuario()
        elif opcion == "3":
            print("adios")
            act = False
        else:
            print("opcion invalida")
            
if __name__ == "__main__":
    main()