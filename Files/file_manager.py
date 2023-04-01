import os

#from config import PROJECT_PATH, DATA_DIR

# encuentra la ruta absoluta de bookeper
PROJECT_PATH = os.path.dirname(os.path.abspath("bookeper"))
DATA_DIR = 'Datos'

class FileManager:

    DATA_PATH = os.path.join(PROJECT_PATH, DATA_DIR)

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def generate_path(self) -> str:
        return os.path.join(FileManager.DATA_PATH, self.filename)