from src.Models.core.gestor import Gestor

BookKeeper = Gestor()

# Crea un administrador
BookKeeper.new_admin("admin", "admin")

# Crea 3 estantes
BookKeeper.new_estante("Fantasía", 10, BookKeeper.administradores[0])
BookKeeper.new_estante("Terror", 10, BookKeeper.administradores[0])
BookKeeper.new_estante("Romance", 10, BookKeeper.administradores[0])

