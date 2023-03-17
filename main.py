"""import gui
import gui1"""
from date_users import *
import  user, stand, libro, random, date_users
from admin import administrador

def main():
    act = True
    print("inicio app")
    print("bienvenido a bookeeper")
    while act: 
        print("que desea hacer?")
        print("1. acceder \n2. crear cuenta \n3. salir")
        opcion = input("ingrese una opcion: ")
        if opcion == "1":
            nombre_usuario = input("ingrese su nombre de usuario: ")
            contraseña = input("ingrese su contraseña: ")
            tipo_usuario = input("ingrese su tipo de usuario: amdmin o usuario: ")
            if verificar_usuario(nombre_usuario) and verificar_contraseña(nombre_usuario, contraseña) and verificar_tipo_usuario(nombre_usuario, tipo_usuario):
                print("acceso concedido")
                if tipo_usuario == "admin":
                    usuario_admin = administrador(nombre_usuario)
                    print("bienvenido administrador")
                    print("que desea hacer?")
                    opc = 0
                    while opc != 6:
                        opc = int(input("1. agregar estante \n2. agregar libro \n3. eliminar estante \n4. prestar libro \n5. ver libros prestados \n6. salir \n"))
                        if opc == 1:
                            libros = None
                            admin = nombre_usuario
                            estante_nuevo = stand.EstanteDeLibros(libros, admin)
                            usuario_admin.agregar_estante(estante_nuevo)
                        elif opc == 2:
                            nombre_libro = input("ingrese el nombre del libro: ")
                            autor_libro = input("ingrese el autor del libro: ")
                            año_libro = input("ingrese el año de lanzamiento del libro: ")
                            formato_libro = input("ingrese el formato del libro: ")
                            editorial_libro = input("ingrese la editorial del libro: ")
                            codigo_libro = random.randint(1000, 9999)
                            ubicacion_libro = None
                            libro_nuevo = libro.Libro(nombre_libro, autor_libro, año_libro, formato_libro, editorial_libro, codigo_libro, ubicacion_libro)
                            libro_nuevo.agregar_stand(usuario_admin.estantes[0].codigo)
                            usuario_admin.estantes.agregar_libro(libro_nuevo)
                        elif opc == 3:
                            
                            usuario_admin.quitar_estante()
                        elif opc == 4:
                            print("prestar libro")
                        elif opc == 5:
                            print("ver libros prestados")
                        elif opc == 6:
                            print("adios")
                        else:
                            print("opcion invalida")
                elif tipo_usuario == "usuario":
                        usuario = user.Usuario(nombre_usuario, "correo")
                        print("bienvenido usuario")
                        print("que desea hacer?")
                        opc = 0
                        while opc != 6:
                            opc = int(input("1. buscar libro \n2. ver libros prestados \n3. devolver libro \n4. ver estantes \n5. ver libros \n6. salir \n"))
                            if opc == 1:
                                print("buscar libro")
                                busqueda = input("ingrese el nombre del libro que desea buscar: ")
                                libro_encontrado = stand.EstanteDeLibros.buscar_libro_por_nombre(busqueda)
                                print(libro_encontrado)
                            elif opc == 2:
                                print("ver libros prestados")
                                libros_prestados = usuario.imprimir_libros_prestados()
                                print(libros_prestados)
                            elif opc == 3:
                                print("devolver libro")
                                nombre_libro = input("ingrese el nombre del libro que desea devolver: ")
                                libros_prestado = usuario.devolver_libro(nombre_libro)
                                print("el libro ha sido devuelto")
                            elif opc == 4:
                                print("ver estantes")
                            elif opc == 5:
                                print("ver libros")
                            elif opc == 6:
                                print("adios")
                            else:
                                print("opcion invalida")
            else:
                print("acceso denegado")
        elif opcion == "2":
            print("crear cuenta")
            nombre_usuario = input("ingrese su nombre de usuario: ")
            contraseña = input("ingrese su contraseña: ")
            tipo_usuario = input("ingrese su tipo de usuario: amdmin o usuario: ")
            codigo = random.randint(1000, 9999)
            usuario_nuevo = date_users.DatoUsuario(nombre_usuario, contraseña, tipo_usuario, codigo)
            usuario_nuevo.almacenar_usuario()
        elif opcion == "3":
            print("adios")
            act = False
        else:
            print("opcion invalida")
            
if __name__ == "__main__":
    main()
    #gui.window.mainloop()
    #gui1.window.mainloop()