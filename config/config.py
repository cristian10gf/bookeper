import pyodbc
from Usuarios.admin import administrador, Prestamo
from Usuarios.cliente import Cliente
from core.estante_libros import EstanteDeLibros, Libro

{
    'server': 'proyecto-bookeeper.database.windows.net',
    'database': 'bookeeper',
    'username': 'cristian',
    'password': 'Franco14*',
}

class db:
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=proyecto-bookeeper.database.windows.net;'
            'DATABASE=bookeeper;'
            'UID=cristian;'
            'PWD=Franco14*'
        )
        print("Connection to Azure SQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")

    def __init__(self):
        self.cursor = self.conn.cursor()

    def get_admin(self, id) -> 'administrador':
        self.cursor.execute('SELECT * FROM dbo.Table_admin WHERE id_admin = ?', id)
        admin = self.cursor.fetchone()
        admid = administrador(admin[1], admin[2], [], admin[0])
        self.cursor.execute('SELECT * FROM dbo.Table_estantes WHERE administrador = ?', (admin[0],))
        estantes = self.cursor.fetchall()
        for estante in estantes:
            estante_admin = EstanteDeLibros([],estante[0], admid, estante[1], estante[2])
            self.cursor.execute('SELECT * FROM dbo.Table_libros WHERE ubicacion = ?',str(estante[0]))
            libros = self.cursor.fetchall()
            for libro in libros:
                self.cursor.execute('SELECT * FROM dbo.Table_prestamo WHERE libro = ?',libro[0])
                prestamos = self.cursor.fetchall()
                libro = Libro(
                    libro[-1],
                    libro[4],
                    libro[2],
                    libro[1],
                    libro[-2],
                    libro[3],
                    libro[0]
                )
                for prestamo in prestamos:
                    prestamo = Prestamo(prestamo[1], prestamo[2], prestamo[3], prestamo[0])
                    libro.agregar_prestamo(prestamo)
                estante_admin.agregar_libro(libro)
            admid.agregar_estante(estante_admin)

        return admid

    def get_estante(self, id) -> 'EstanteDeLibros':
        self.cursor.execute('SELECT * FROM dbo.Table_estantes WHERE id_estante = ?', id)
        estante = self.cursor.fetchone()
        return estante

    def get_libro(self, id) -> 'Libro':
        self.cursor.execute('SELECT * FROM dbo.Table_libros WHERE id_libro = ?', id)
        libro = self.cursor.fetchone()
        return libro

    def get_prestamo(self, id) -> 'Prestamo':
        self.cursor.execute('SELECT * FROM dbo.Table_prestamo WHERE id = ?', id)
        prestamo = self.cursor.fetchone()
        return prestamo

    def get_cliente(self, id) -> 'Usuario':
        self.cursor.execute('SELECT * FROM dbo.Table_cliente WHERE id_cliente = ?', id)
        cliente = self.cursor.fetchone()
        return cliente

    def get_admins(self) -> list['administrador']:
        self.cursor.execute('SELECT * FROM dbo.Table_admin')
        all = []
        admins = self.cursor.fetchall()
        for admin in admins:
            administrador = self.get_admin(admin[0])
            all.append(administrador)
        return all

    def get_estantes(self) -> list['EstanteDeLibros']:
        self.cursor.execute('SELECT * FROM dbo.Table_estantes')
        estantes = self.cursor.fetchall()
        all = {}
        for estante in estantes:
            administrador = self.get_admin(estante[3])
            for estante_admin in administrador.estantes:
                if estante_admin.codigo == estante[0]:
                    all[estante[0]] = estante_admin
        return all

    def get_libros(self) -> list['Libro']:
        self.cursor.execute('SELECT * FROM dbo.Table_libros')
        libros = self.cursor.fetchall()
        return libros

    def get_prestamos(self) -> list['Prestamo']:
        self.cursor.execute('SELECT * FROM dbo.Table_prestamo')
        prestamos = self.cursor.fetchall()
        return prestamos

    def get_clientes(self) -> list['Usuario']:
        self.cursor.execute('SELECT * FROM dbo.Table_cliente')
        clientes = self.cursor.fetchall()
        return clientes

