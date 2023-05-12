import pyodbc
from .Usuarios.admin import administrador, Prestamo
from Usuarios.cliente import Cliente
from core.estante_libros import EstanteDeLibros, Libro

info = {
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
        self.cursor.execute('SELECT * FROM dbo.Table_estantes WHERE administrador = ?', (admin[0]))
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
        return admid

    def get_estante(self, id) -> 'EstanteDeLibros':
        self.cursor.execute('SELECT * FROM dbo.Table_estantes WHERE id_estante = ?', id)
        estante = self.cursor.fetchone()
        if estante is None:
            return None
        elif estante[4] is None:
            estante = EstanteDeLibros([], estante[0], estante[1], estante[2], estante[3])
        else:
            estante = EstanteDeLibros([], estante[0], estante[1], estante[2], estante[3], estante[4])
        return estante

    def get_libro(self, id) -> 'Libro':
        self.cursor.execute('SELECT * FROM dbo.Table_libros WHERE id_libro = ?', id)
        libro = self.cursor.fetchone()
        neolibro = Libro(
            libro[-1],
            libro[4],
            libro[2],
            libro[1],
            libro[-2],
            libro[3],
            libro[0]
        )
        return neolibro

    def get_prestamo(self, id) -> 'Prestamo':
        self.cursor.execute('SELECT * FROM dbo.Table_prestamo WHERE id = ?', id)
        prestamo = self.cursor.fetchone()
        nuevo_prestamo = Prestamo(prestamo[1], prestamo[2], prestamo[3], prestamo[0])
        return nuevo_prestamo

    def get_cliente(self, id: int) -> 'Cliente':
        self.cursor.execute('SELECT * FROM dbo.Table_cliente WHERE id_cliente = ?', id)
        cliente = self.cursor.fetchone()
        nuevo_cliente = Cliente(cliente[1], cliente[2], cliente[3], cliente[4], cliente[5], cliente[6], cliente[0])
        return nuevo_cliente

    def get_admins(self) -> list['administrador']:
        self.cursor.execute('SELECT * FROM dbo.Table_admin')
        all = {}
        admins = self.cursor.fetchall()
        for admin in admins:
            if admin[0] not in all:
                all[admin[0]] = self.get_admin(admin[0])
        return all.values()

    def get_estantes(self) -> list['EstanteDeLibros']:
        self.cursor.execute('SELECT * FROM dbo.Table_estantes')
        estantes = []
        for admin in self.get_admins():
            estantes.extend(admin.estantes)
        return estantes

    def get_libros(self) -> list['Libro']:
        self.cursor.execute('SELECT * FROM dbo.Table_libros')
        libros = self.cursor.fetchall()
        libros_convertidos = []
        for libro in libros:
            libro_nuevo = Libro(
                libro[-1],
                libro[4],
                libro[2],
                libro[1],
                libro[-2],
                libro[3],
                libro[0]
            )
            libros_convertidos.append(libro_nuevo)
        return libros_convertidos

    def get_prestamos(self) -> list['Prestamo']:
        self.cursor.execute('SELECT * FROM dbo.Table_prestamo')
        prestamos = self.cursor.fetchall()
        return prestamos

    def get_clientes(self) -> list['Cliente']:
        self.cursor.execute('SELECT * FROM dbo.Table_cliente')
        clientes = self.cursor.fetchall()
        return clientes

    def actualizar_admin(self, admin: 'administrador'):
        self.cursor.execute('SELECT * FROM dbo.Table_admin WHERE id_admin = ?', admin.id)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_admin VALUES(?, ?, ?)', (admin.nombre, admin.contraseña, admin.id))
        else:
            self.cursor.execute('UPDATE dbo.Table_admin SET nombre = ?, contraseña = ? WHERE id_admin = ?', (admin.nombre, admin.contraseña, admin.id))
        self.conn.commit()

    def actualizar_estante(self, estante: 'EstanteDeLibros'):
        self.cursor.execute('SELECT * FROM dbo.Table_estantes WHERE id_estante = ?', estante.id)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_estantes VALUES(?, ?, ?, ?, ?)', (estante.id, estante.admin.id, estante.cantidad, estante.categoria, estante.ubicacion))
        else:
            self.cursor.execute('UPDATE dbo.Table_estantes SET cantidad = ?, categoria = ?, ubicacion = ? WHERE id_estante = ?', (estante.cantidad, estante.categoria, estante.ubicacion, estante.id))
        self.conn.commit()

    def actualizar_libro(self, libro: 'Libro'):
        self.cursor.execute('SELECT * FROM dbo.Table_libros WHERE id_libro = ?', libro.id)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_libros VALUES(?, ?, ?, ?, ?, ?, ?)', (libro.id, libro.nombre, libro.autor, libro.categoria, libro.estante.id, libro.cantidad, libro.disponibles))
        else:
            self.cursor.execute('UPDATE dbo.Table_libros SET nombre = ?, autor = ?, categoria = ?, estante = ?, cantidad = ?, disponibles = ? WHERE id_libro = ?', (libro.nombre, libro.autor, libro.categoria, libro.estante.id, libro.cantidad, libro.disponibles, libro.id))
        self.conn.commit()

    def actualizar_prestamo(self, prestamo: 'Prestamo'):
        self.cursor.execute('SELECT * FROM dbo.Table_prestamo WHERE id = ?', prestamo.id)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_prestamo VALUES(?, ?, ?, ?)', (prestamo.id, prestamo.cliente.id, prestamo.libro.id, prestamo.fecha))
        else:
            self.cursor.execute('UPDATE dbo.Table_prestamo SET cliente = ?, libro = ?, fecha = ? WHERE id = ?', (prestamo.cliente.id, prestamo.libro.id, prestamo.fecha, prestamo.id))
        self.conn.commit()

    def actualizar_cliente(self, cliente: 'Cliente'):
        self.cursor.execute('SELECT * FROM dbo.Table_cliente WHERE id_cliente = ?', cliente.id)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_cliente VALUES(?, ?, ?, ?, ?, ?, ?)', (cliente.id, cliente.nombre, cliente.apellido, cliente.cedula, cliente.telefono, cliente.direccion, cliente.correo))
        else:
            self.cursor.execute('UPDATE dbo.Table_cliente SET nombre = ?, apellido = ?, cedula = ?, telefono = ?, direccion = ?, correo = ? WHERE id_cliente = ?', (cliente.nombre, cliente.apellido, cliente.cedula, cliente.telefono, cliente.direccion, cliente.correo, cliente.id))
        self.conn.commit()

    def actualizar(self, todos_datos: dict):
        for admin in todos_datos['admins']:
            self.actualizar_admin(admin)
        for estante in todos_datos['estantes']:
            self.actualizar_estante(estante)
        for libro in todos_datos['libros']:
            self.actualizar_libro(libro)
        for prestamo in todos_datos['prestamos']:
            self.actualizar_prestamo(prestamo)
        for cliente in todos_datos['clientes']:
            self.actualizar_cliente(cliente)


db1 = db()
for estantes in db1.get_estantes():
    print(estantes.admin.nombre)
