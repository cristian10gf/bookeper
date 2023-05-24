import pyodbc
from src.Models.Usuarios.admin import administrador, Prestamo
from src.Models.Usuarios.cliente import Cliente
from src.Models.core.estante_libros import EstanteDeLibros, Libro
from datetime import date, datetime
from src.Models.Libros.recomendacio import Recomendacion

info = {
    'server': 'proyecto-bookeeper.database.windows.net',
    'database': 'bookeeper',
    'username': 'cristian',
    'password': 'Franco14*',
}

# table_admin = id_admin, nombre, contraseña
# table_estantes = id_estante, genero, tamaño, administrador
# table_libros = id_libro, genero, ubicacion, autores, estado, editorial, nombre, fecha_lanzamiento
# table_prestamo = id_prestamo, cliente, fecha_prestamo, fecha_devolucion, devuelto, libro
# table_cliente = id_cliente, nombre, contraseña
# table_recomendacion = id_recom, libro, cliente, prestamo

class db:
    conn = None
    try:
        conn = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=proyecto-bookeeper.database.windows.net;'
            'DATABASE=bookeeper;'
            'UID=cristian;'
            'PWD=Franco14*'
        )
        print("Connection to Azure SQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")

    def __init__(self):
        self.cursor = db.conn.cursor()

    def get_recomendacion(self, id: int) -> 'Recomendacion':
        self.cursor.execute('SELECT * FROM dbo.Table_recomendacion WHERE id_recom = ?', id)
        recomendacion = self.cursor.fetchone()
        if recomendacion is None:
            return None
        else:
            recomendacion = Recomendacion(recomendacion[0], recomendacion[1], recomendacion[2], True if recomendacion[3] == 1 else False)
        return recomendacion

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
                libro_new: Libro
                self.cursor.execute('SELECT * FROM dbo.Table_prestamo WHERE libro = ?',libro[0])
                prestamo = self.cursor.fetchall()
                # table_libros = id_libro, genero, ubicacion, autores, estado, editorial, nombre, fecha_lanzamiento
                libro_new = Libro(str(libro[-2]), str(libro[3]), int(libro[-1]),  str(libro[1]),  str(libro[5]),   int(libro[2]), int(libro[0]))
                if prestamo is None or len(prestamo) == 0:
                    prestamo = None
                else:
                    prestamo_new = Prestamo(prestamo[0], self.get_cliente(prestamo[1]), libro_new, prestamo[2], prestamo[3], True if prestamo[4] == 1 else False)
                estante_admin.agregar_libro(libro_new)
        return admid

    def get_estante(self, id) -> 'EstanteDeLibros':
        self.cursor.execute('SELECT * FROM dbo.Table_estantes WHERE id_estante = ?', id)
        estante = self.cursor.fetchone()
        if estante is None:
            return None
        else:
            estante = self.get_admin(estante[-1]).get_estante(id)
        return estante

    def get_libro(self, id) -> 'Libro':
        self.cursor.execute('SELECT * FROM dbo.Table_libros WHERE id_libro = ?', id)
        libro = self.cursor.fetchone()
        neolibro = Libro(str(libro[-2]), str(libro[3]), int(libro[-1]),  str(libro[1]),  str(libro[5]),   int(libro[2]), int(libro[0]))
        return neolibro


    def get_prestamo(self, id) -> 'Prestamo':
        self.cursor.execute('SELECT * FROM dbo.Table_prestamo WHERE id_prestamo = ?', id)
        prestamo = self.cursor.fetchone()
        print(prestamo)
        nuevo_prestamo = Prestamo(prestamo[0], prestamo[-1], prestamo[1], prestamo[2], prestamo[3])
        return nuevo_prestamo

    def get_cliente(self, id: int) -> 'Cliente':
        self.cursor.execute('SELECT * FROM dbo.Table_cliente WHERE id_cliente = ?', id)
        cliente = self.cursor.fetchone()
        if cliente is None:
            return None
        else:
            nuevo_cliente = Cliente(cliente[1], cliente[2], cliente[0])
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
        prestamos_convertidos = []
        for prestamo in prestamos:
            prestamos_convertidos.append(Prestamo(prestamo[0], prestamo[1], prestamo[-1], prestamo[2], prestamo[3], True if prestamo[4] == 1 else False))
        return prestamos_convertidos

    def get_recomendaciones(self) -> list['Recomendacion']:
        self.cursor.execute('SELECT * FROM dbo.Table_recomendacion')
        recomendaciones = self.cursor.fetchall()
        if recomendaciones is None:
            return None
        else:
            recomendaciones_convertidas = []
            for recomendacion in recomendaciones:
                recomendaciones_convertidas.append(Recomendacion(recomendacion[0],self.get_libro(recomendacion[1]),self.get_cliente(recomendacion[2]), True if recomendacion[3] == 1 else False))
            return recomendaciones_convertidas

    def get_clientes(self) -> list['Cliente']:
        self.cursor.execute('SELECT * FROM dbo.Table_cliente')
        clientes = self.cursor.fetchall()
        clientes_convertidos = []
        for cliente in clientes:
            cliente_nuevo = Cliente(cliente[1], cliente[2], cliente[0])
            clientes_convertidos.append(cliente_nuevo)
        return clientes_convertidos

    def actualizar_admin(self, admin: 'administrador'):
        self.cursor.execute('SELECT * FROM dbo.Table_admin WHERE id_admin = ?', admin.codigo_Usuario)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_admin VALUES(?, ?, ?)', (admin.nombre, admin.contrasena, admin.codigo_Usuario))
        else:
            self.cursor.execute('UPDATE dbo.Table_admin SET nombre = ?, contraseña = ? WHERE id_admin = ?', (admin.nombre, admin.contrasena, admin.codigo_Usuario))
        self.conn.commit()

    def actualizar_estante(self, estante: 'EstanteDeLibros'):
        # table_estantes = id_estante, genero, tamaño, administrador
        self.cursor.execute('SELECT * FROM dbo.Table_estantes WHERE id_estante = ?', estante.codigo)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_estantes VALUES(?, ?, ?, ?)', (estante.codigo, estante.genero, estante.tamano, estante.admin.codigo_Usuario))
        else:
            self.cursor.execute('UPDATE dbo.Table_estantes SET tamano = ?, genero = ?, administrador = ? WHERE id_estante = ?', (estante.tamano, estante.genero, estante.admin.codigo_Usuario, estante.codigo))
        self.conn.commit()

    def actualizar_libro(self, libro: 'Libro'):
        # table_libros = id_libro, genero, fecha_publicacion, ubicacion, autores, estado, editorial, nombre
        if libro.estado is None:
            pass
        else:
            existe_estado = self.get_prestamo(libro.estado.codigo)
            if existe_estado is None:
                pass
            else:
                self.actualizar_prestamo(libro.estado)

        self.cursor.execute('SELECT * FROM dbo.Table_libros WHERE id_libro = ?', libro.codigo)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_libros VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (libro.codigo, libro.genero, libro.ubicacion, libro.guardar_autores(), libro.estado, libro.editorial, libro.nombre, libro.fecha_lanzamiento))
        else:
            self.cursor.execute('UPDATE dbo.Table_libros SET genero = ?, fecha_lanzamiento = ?, ubicacion = ?, autores = ?, estado = ?, editorial = ?, nombre = ? WHERE id_libro = ?', (libro.genero, libro.fecha_lanzamiento, libro.ubicacion, libro.guardar_autores(), libro.estado, libro.editorial, libro.nombre, libro.codigo))
        self.conn.commit()

    def actualizar_prestamo(self, prestamo: 'Prestamo'):
        # table_prestamo = id_prestamo, cliente, fecha_prestamo, fecha_devolucion, devuelto, libro
        self.cursor.execute('SELECT * FROM dbo.Table_prestamo WHERE id = ?', prestamo.codigo)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_prestamo VALUES(?, ?, ?, ?, ?)', (prestamo.cliente.codigo_Usuario, prestamo.fecha_prestamo, prestamo.fecha_devolucion, prestamo.devuelto, prestamo.libro.codigo))
        else:
            self.cursor.execute('UPDATE dbo.Table_prestamo SET cliente = ?, libro = ?, fecha_prestamo = ?, fecha_devolucion = ?, devuelto = ? WHERE id = ?', (prestamo.cliente.codigo_Usuario, prestamo.libro.codigo, prestamo.fecha_prestamo, prestamo.fecha_devolucion, prestamo.devuelto, prestamo.codigo))
        self.conn.commit()

    def actualizar_cliente(self, cliente: 'Cliente'):
        # table_cliente = id_cliente, nombre, contraseña
        self.cursor.execute('SELECT * FROM dbo.Table_cliente WHERE id_cliente = ?', cliente.codigo_Usuario)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_cliente VALUES(?, ?, ?)', (cliente.codigo_Usuario, cliente.nombre, cliente.contrasena))
        else:
            self.cursor.execute('UPDATE dbo.Table_cliente SET nombre = ?, contraseña = ? WHERE id_cliente = ?', (cliente.nombre, cliente.contrasena, cliente.codigo_Usuario))
        self.conn.commit()

    def actualizar_recomendacion(self, recomendacion: 'Recomendacion'):
        # table_recomendacion = id_recomendacion, libro, cliente, prestamo
        self.cursor.execute('SELECT * FROM dbo.Table_recomendacion WHERE id_recom = ?', recomendacion.id)
        if self.cursor.fetchone() is None:
            self.cursor.execute('INSERT INTO dbo.Table_recomendacion VALUES(?, ?, ?, ?)', (recomendacion.id, recomendacion.libro.codigo, recomendacion.cliente.codigo_Usuario, 1 if recomendacion.prestamo == True else 0))
        else:
            self.cursor.execute('UPDATE dbo.Table_recomendacion SET libro = ?, cliente = ?, prestamo = ? WHERE id_recom = ?', (recomendacion.libro.codigo, recomendacion.cliente.codigo_Usuario,1 if recomendacion.prestamo == True else 0, recomendacion.id))
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
        for recomendacion in todos_datos['recomendaciones']:
            self.actualizar_recomendacion(recomendacion)

    def eliminar_recomendacion(self, recomendacion: 'Recomendacion'):
        self.cursor.execute('DELETE FROM dbo.Table_recomendacion WHERE id_recom = ?', recomendacion.id)
        self.conn.commit()