import unittest
import datetime
from src.Models.config.config import db
from src.Models.core.gestor import Bookeeper
from src.Models.Usuarios.admin import administrador
from src.Models.Usuarios.cliente import Cliente
from src.Models.core.estante_libros import EstanteDeLibros
from src.Models.Libros.libro import Libro, Prestamo
from src.Models.Libros.recomendacio import Recomendacion
from src.Controllers.control_bookeeper import ControlBookeeper


# todas son pruebas unitarias o de integracion
class Test_db(unittest.TestCase):
    def test_database_connection(self):
        self.db = db()
        self.assertTrue(self.db is not None)
    
    def test_db_get_cliente(self):
        self.db = db()
        self.assertTrue(type(self.db.get_cliente(1)), 'Cliente')

    def test_db_get_libro(self):
        self.db = db()
        self.assertTrue(type(self.db.get_estantes()[-1].libros[-1]), 'Libro' )

    def test_db_get_estante(self):
        self.db = db()
        self.assertTrue(type(self.db.get_estantes()[-1]), 'EstanteDeLibros')

    def test_db_get_estantes(self):
        self.db = db()
        self.assertTrue(type(self.db.get_estantes()), 'list[EstanteDeLibros]')

    def test_db_get_libros(self):
        self.db = db()
        self.assertTrue(type(self.db.get_libros()), 'list[Libro]')

    def test_db_get_admin(self):
        self.db = db()
        self.assertTrue(type(self.db.get_admin(1)), 'administrador')

    def test_db_get_admins(self):
        self.db = db()
        self.assertTrue(type(self.db.get_admins()), 'list[administrador]')

    def test_db_get_prestamos(self):
        self.db = db()
        self.assertTrue(type(self.db.get_prestamos()), 'list[Prestamo]')


    def test_db_get_prestamo(self):
        self.db = db()
        self.assertIsNotNone(type(self.db.get_prestamo(0)))  
        self.assertTrue(type(self.db.get_prestamo(1751)), 'Prestamo')

    def test_db_get_recomendaciones(self):
        self.db = db()
        self.assertTrue(type(self.db.get_recomendaciones()), 'list[Recomendacion]')

    def test_db_get_recomendacion(self):
        self.db = db()
        self.assertIsNotNone(type(self.db.get_recomendacion(-1)))
        self.assertTrue(type(self.db.get_recomendacion(-1)), 'Recomendacion')
    


# todas son pruebas de integracion  
class Test_gestor(unittest.TestCase):
    def test_gestor_get_cliente(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.get_cliente(1)), 'Cliente')

    def test_gestor_get_libro(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.estantes[-1].libros[-1]), 'Libro')


    def test_gestor_get_estante(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.estantes[-1]), 'EstanteDeLibros')

    def test_gestor_verificar(self):
        self.gestor = Bookeeper()
        self.assertFalse(self.gestor.verificar_admin('admin', 'admin', 1))
        self.assertFalse(self.gestor.verificar_admin('admin', 'admin', 2))
        self.assertFalse(self.gestor.verificar_cliente('cliente', 'cliente', 1))
        self.assertFalse(self.gestor.verificar_cliente('cliente', 'cliente', 2))
    
    def test_gestor_get_estantes(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.estantes), 'list[EstanteDeLibros]')

    def test_gestor_get_libros(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.get_libros()), 'list[Libro]')

    def test_gestor_get_admin(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.administradores[-1]), 'administrador')

    def test_gestor_get_admins(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.administradores), 'list[administrador]')

    
    def test_gestor_get_prestamos(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.get_prestamos(self.gestor.clientes[-1])), 'list[Prestamo]')

    def test_gestor_get_prestamo(self):
        self.gestor = Bookeeper()
        self.assertIsNotNone(type(self.gestor.get_prestamo(0)))  
        self.assertTrue(type(self.gestor.get_prestamo(1751)), 'Prestamo')

    def test_gestor_buscar(self):
        self.gestor = Bookeeper()
        self.assertTrue(type(self.gestor.buscar_libro_por_autor), 'set[Libro]')
        self.assertTrue(type(self.gestor.buscar_libro_por_nombre), 'set[Libro]')
        self.assertTrue(type(self.gestor.buscar_libro_por_genero), 'set[Libro]')
    
    def test_gestor_generate_recomendacion(self):
        self.gestor = Bookeeper()
        self.gestor.agregar_Cliente(Cliente('usuario', 'contrasena', 1))
        self.assertFalse(self.gestor.generate_recomendacion(self.gestor.clientes[-1]))


# pruebas unitarias
class Test_libro(unittest.TestCase):
    def test_libro(self):
        self.libro = Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1)
        self.assertTrue(type(self.libro), 'Libro')

    def test_libro_guardar_autores(self):
        self.libro = Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1)
        self.assertTrue(type(self.libro.guardar_autores()), 'None')


# pruebas unitarias
class Test_cliente(unittest.TestCase):
    def test_cliente(self):
        self.cliente = Cliente('usuario', 'contrasena', 1)
        self.assertTrue(type(self.cliente), 'cliente')

    def test_cliente_prestar_libro(self):
        self.cliente = Cliente('usuario', 'contrasena', 1)
        self.assertTrue(type(self.cliente.prestar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1))), 'None')

    def test_cliente_devolver_libro(self):
        self.cliente = Cliente('usuario', 'contrasena', 1)
        self.assertTrue(type(self.cliente.devolver_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1))), 'None')

    def test_cliente_ver_libros_prestados(self):
        self.cliente = Cliente('usuario', 'contrasena', 1)
        self.assertTrue(type(self.cliente.ver_libros_prestados()), 'list[Prestamo]')

    '''def test_cliente_buscar_libro_por_nombre(self):
        self.cliente = Cliente('usuario', 'contrasena', 1)
        self.assertTrue(type(self.cliente.buscar_libro_por_nombre('titulo')), 'Libro')'''

    

# pruebas unitarias y talvez algunas de integracion
class Test_admin(unittest.TestCase):
    def test_admin(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.assertTrue(type(self.admin), 'administrador')

    def test_admin_ver_libros_prestados(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.assertTrue(type(self.admin.ver_libros_prestados()), 'list[Prestamo]')
    
    def test_admin_verificar_libro_prestado(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.admin.prestar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1), Cliente('usuario', 'contrasena', 1))
        self.assertTrue(type(self.admin.verificar_libro_prestado(self.admin.ver_libros_prestados()[-1].libro)), 'bool')

    def test_admin_buscar_libro_por_nombre(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.assertTrue(type(self.admin.buscar_libro_por_nombre('titulo')), 'Libro')
    
    def test_admin_buscar_libros_por_autor(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.assertTrue(type(self.admin.buscar_libros_por_autor('autor')), 'list[Libro]')

    def test_admin_prestar_libro(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.admin.prestar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1), Cliente('usuario', 'contrasena', 1))
        self.assertTrue(type(self.admin.prestar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1), Cliente('usuario', 'contrasena', 1))), 'None')
        self.assertTrue(type(self.admin.prestar_libro(self.admin.ver_libros_prestados()[-1].libro, Cliente('nombre', 'conra', 87876))), 'None')

    def test_admin_devolver_libro(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.admin.prestar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1), Cliente('usuario', 'contrasena', 1))
        self.assertTrue(type(self.admin.devolver_libro(self.admin.ver_libros_prestados()[-1].libro, Cliente('usuario', 'contrasena', 1))), 'None')

    def test_admin_agregar_estante(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.assertTrue(type(self.admin.agregar_estante(EstanteDeLibros([], 20, self.admin,  'genero', 1))), 'None')

    def test_admin_quitar_estante(self):
        self.admin = administrador( 'usuario', 'contrasena',[], 1)
        self.admin.agregar_estante(EstanteDeLibros([], 20, self.admin,  'genero', 1))
        self.assertTrue(type(self.admin.quitar_estante(self.admin.estantes[-1])), 'None')



# pruebas unitarias
class Test_estante(unittest.TestCase):
    def test_estante(self):
        self.estante = EstanteDeLibros([], 20, administrador( 'usuario', 'contrasena'),  'genero', 1)
        self.assertTrue(type(self.estante), 'EstanteDeLibros')

    def test_estante_agregar_libro(self):
        self.estante = EstanteDeLibros([], 20, administrador( 'usuario', 'contrasena'),  'genero', 1)
        self.assertTrue(type(self.estante.agregar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1))), 'None')

    def test_estante_quitar_libro(self):
        self.estante = EstanteDeLibros([], 20, administrador( 'usuario', 'contrasena'),  'genero', 1)
        self.estante.agregar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1))
        self.assertTrue(type(self.estante.quitar_libro(self.estante.libros[-1])), 'None')

    def test_estante_buscar_libro_por_nombre(self):
        self.estante = EstanteDeLibros([], 20, administrador( 'usuario', 'contrasena'),  'genero', 1)
        self.estante.agregar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1))
        self.assertTrue(type(self.estante.buscar_libros_por_nombre('titulo')), 'set[Libro]')

    def test_estante_buscar_libros_por_autor(self):
        self.estante = EstanteDeLibros([], 20, administrador( 'usuario', 'contrasena'),  'genero', 1)
        self.estante.agregar_libro(Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1))
        self.assertTrue(type(self.estante.buscar_libros_por_autor('autor')), 'set[Libro]')


# pruebas unitarias
class Test_prestamo(unittest.TestCase):
    def test_prestamo(self):
        self.prestamo = Prestamo(Cliente('usuario', 'contrasena', 1), Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1), datetime.datetime.now(), datetime.datetime.now(), True, 432)
        self.assertTrue(type(self.prestamo), 'Prestamo')

    def test_prestamo_devolver(self):
        self.prestamo = Prestamo(Cliente('usuario', 'contrasena', 1), Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1), datetime.datetime.now(), datetime.datetime.now(), True, 432)
        self.assertTrue(type(self.prestamo.devolver()), 'None')


# pruebas unitarias
class Test_recomendacion(unittest.TestCase):
    def test_recomendacion(self):
        self.recomendacion = Recomendacion(id = 20, usuario= Cliente('usuario', 'contrasena', 1), libro = Libro('titulo', 'autor',2020,  'genero', 'editorial', 1, 1) )
        self.assertTrue(type(self.recomendacion), 'Recomendacion')


# prueba funcional
class Test_control_bookeeper(unittest.TestCase):
    def test_cb_busqueda_de_libros(self):
        self.cb = ControlBookeeper()
        self.assertTrue(type(self.cb.get_libro_by_name('titulo')), 'set[Libro]')