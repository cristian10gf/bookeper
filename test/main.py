import unittest
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)



from db_prueba import Test_db, Test_gestor, Test_libro, Test_cliente, Test_estante, Test_prestamo, Test_recomendacion, Test_admin

if __name__ == '__main__':
    unittest.main()
