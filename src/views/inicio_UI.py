from PyQt6 import  QtWidgets
from PyQt6.QtCore import Qt, QRect, pyqtSignal, QObject, QEvent, QTimer, QTime
from PyQt6.QtWidgets import (QApplication, QToolTip, QWidget
                             )
import src.views.UI as UI
import sys

class Inicio(QWidget):
    def __init__(self):
        super(Inicio, self).__init__()
        self.width = 400
        self.height = 600

        self.setWindowTitle("Pantanlla de carga de la app")
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.show()

    def active(self):
        UI.Main()
        self.close()


def Main():  # ________________________________________________________________________________________________________
    app = QApplication(sys.argv)
    win = Inicio()
    win.active()
    sys.exit(app.exec())