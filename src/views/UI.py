from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QRect, pyqtSignal, QObject, QEvent, QTimer, QTime
from PyQt6.QtGui import QFont, QPixmap, QCursor
from PyQt6.QtWidgets import (QApplication, QToolTip, QWidget, QMainWindow, QPushButton, QTextEdit, QLineEdit, QCheckBox, QLabel,
                             QFrame, QDialog)
import sys
from src.Controllers.control_bookeeper import ControlBookeeper

def clickableQLineEdit(widget):
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget and event.type() == QEvent.Type.MouseButtonRelease and obj.rect().contains(event.pos()):
                self.clicked.emit()
                return True
            else:
                return False
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked
# clickableQLineEdit(self.confirm_line).connect(self.confirmLineClick)


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.width = 1630
        self.height = 980
        self.StartUp()
        self.control = ControlBookeeper()


    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        # | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#594E3F; border-radius: 20px;
                        background-image: url(src/views/images/Backimage.jpg)""")
        lg = QLabel(self)
        lg.move(945, 0)
        lg.resize(self.width-945, self.height)
        lg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px""")
        ################################################
        self.labels()
        self.linesEdits()
        self.loggin_button()
        self.newCount_button()
        #####################
        self.close_button()
        self.center()       #
        self.show()         #
        #####################

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def linesEdits(self):
        #   user
        self.user_line = QLineEdit(self)
        self.user_line.setFont(QFont('Now', 18))
        self.user_line.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px; 
                                    border-color: transparent; border-bottom-color: #868179""")
        font = self.user_line.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.user_line.setFont(font)
        self.user_line.resize(485, 40)
        self.user_line.move(1045, 470)
        #   password
        self.pass_line = QLineEdit(self)
        self.pass_line.setFont(QFont('Now', 18))
        self.pass_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_line.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px; 
                                    border-color: transparent; border-bottom-color: #868179""")
        self.pass_line.resize(485, 40)
        self.pass_line.move(1045, 625)

    def newCount_button(self):
        Ncount = QPushButton('¿Nueva Cuenta?', self)
        Ncount.setFont(QFont('Now', 15))
        font = Ncount.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        Ncount.setFont(font)
        Ncount.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        Ncount.move(1200, 840)
        Ncount.resize(173, 30)
        Ncount.setStyleSheet("""color:#868179; background-color:transparent""")
        Ncount.clicked.connect(self.signUp_clicked)

    def labels(self):
        #   title
        title_label = QLabel(' BooKeeper', self)
        title_label.setFont(QFont('Nickainley', 92,))
        title_label.move(1000, 30)
        title_label.resize(580, 200)
        title_label.setStyleSheet("""color:#594E3F""")
        #   welcome
        welcome_label = QLabel('¡Bienvenido a BooKeeper!', self)
        welcome_label.setFont(QFont('Now', 28))
        font = welcome_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        welcome_label.setFont(font)
        welcome_label.move(1045, 220)
        welcome_label.setStyleSheet("""color:#868179""")
        #   user or address
        user_label = QLabel('Usuario o Correo', self)
        user_label.setFont(QFont('Now', 20))
        font = user_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        user_label.setFont(font)
        user_label.move(1045, 430)
        user_label.setStyleSheet("""color:#868179""")
        #   password
        pass_label = QLabel('Contraseña', self)
        pass_label.setFont(QFont('Now', 20))
        font = pass_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        pass_label.setFont(font)
        pass_label.move(1045, 585)
        pass_label.setStyleSheet("""color:#868179""")

    def loggin_button(self):
        loginB = QPushButton("Acceder", self)
        loginB.setFont(QFont('Now', 20))
        font = loginB.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        loginB.setFont(font)
        loginB.resize(205, 60)
        loginB.move(1185, 760)
        loginB.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        loginB.setStyleSheet(
            """color:#FFF9F2; background-color:#594E3F; border-radius: 30px""")
        loginB.clicked.connect(self.login_clicked)

    def close_button(self):
        closeAction = QApplication.instance().quit
        closeB = QPushButton("x", self)
        closeB.resize(50, 50)
        closeB.move(self.width-49, 0)
        closeB.setFont(QFont('Now', 20))
        closeB.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px;
            change-cursor: cursor('PointingHand')""")
        closeB.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        closeB.clicked.connect(closeAction)

    def signUp_clicked(self):
        self.SignWin = SignUpWindow()
        self.SignWin.show()
        timer = QTimer(self)
        timer.start(5)
        timer.timeout.connect(self.close)

    # this must be valided*******************************************************
    def login_clicked(self):
        userData = self.user_line.text()
        passData = self.pass_line.text()
        if self.control.verificar_admin(userData, passData):
            print('admin')
        else:
            print('cliente')


# _____________________________________________________________________________________
class SignUpWindow(QWidget):
    def __init__(self) -> None:
        super(SignUpWindow, self).__init__()
        self.width = 1630
        self.height = 980
        self.StartUp()
        self.control = ControlBookeeper()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint
            | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#A69073; border-radius: 20px;
                        background-image: url(src/views/images/Backimage.jpg)""")
        sg = QLabel(self)
        sg.move(545, 0)
        sg.resize(self.width-545, self.height)
        sg.setStyleSheet(
            """background-color:#FFF9F2; border-radius: 20px;border-top-left-radius: 23px""")
        self.labels()
        self.linesEdits()
        self.signUp_Button()
        self.back_button()
        self.checkBox()
        ######################
        self.close_button()  #
        self.center()        #
        self.show()          #
        ######################
# validar que el user y el adress no existan

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def labels(self):
        #   title
        title_label = QLabel(' BooKeeper', self)
        title_label.setFont(QFont('Nickainley', 92,))
        title_label.move(797, 30)
        title_label.resize(580, 200)
        title_label.setStyleSheet("""color:#594E3F""")
        #   welcome
        welcome_label = QLabel('¡Hola nuevo usuario!', self)
        welcome_label.setFont(QFont('Now', 28))
        font = welcome_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        welcome_label.setFont(font)
        welcome_label.move(905, 220)
        welcome_label.setStyleSheet("""color:#868179""")
        #   adress
        adress_label = QLabel('Correo Electrónico', self)
        self.config_label(adress_label, 545+61, 370)
        #   name
        name_label = QLabel('Nombre y Apellido', self)
        self.config_label(name_label, 545+61, 500)
        #   user
        user_label = QLabel('Nombre de Usuario', self)
        self.config_label(user_label, 545+61, 630)
        #   password
        pass_label = QLabel('Contraseña', self)
        self.config_label(pass_label, 545+61+450+63, 370)
        #   confirm password
        confirm_label = QLabel('Confirmar Contraseña', self)
        self.config_label(confirm_label, 545+61+450+63, 500)
        #   show
        self.show_label = QLabel('', self)

    def linesEdits(self):
        #   Adress
        self.adress_line = QLineEdit(self)
        self.config_linesEdit_text(self.adress_line, 545+61, 410, 450, 40)
        #   name
        self.name_line = QLineEdit(self)
        self.config_linesEdit_text(self.name_line, 545+61, 540, 450, 40)
        #   user
        self.user_line = QLineEdit(self)
        self.config_linesEdit_text(self.user_line, 545+61, 670, 450, 40)
        #   password
        self.pass_line = QLineEdit(self)
        self.config_linesEdit_pass(self.pass_line, 545+61+450+63, 410, 450, 40)
        #   confirm pass
        # cuando haces click sobre confirm_line debe verificar q lo de arriba es igual
        self.confirm_line = QLineEdit(self)
        self.confirm_line.textChanged.connect(self.confirmLineClick)
        self.config_linesEdit_pass(
            self.confirm_line, 545+61+450+63, 540, 450, 40)

    def checkBox(self):
        self.admin_box = QCheckBox('administrador',self)
        self.admin_box.setFont(QFont('Now', 20))
        font = self.admin_box.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.admin_box.setFont(font)
        self.admin_box.move(545+61+450+63, 630)
        self.admin_box.setStyleSheet(
            "QCheckBox""{"
                "color: #868179;"
            "}"
            "QCheckBox::indicator""{"
                "width: 30px;"
                "height: 30px;"
            "}"
            "QCheckBox::indicator::unchecked""{"
                "image: url(src/views/images/uncheckmark.png);"
            "}"
            "QCheckBox::indicator::checked""{"
                "image: url(src/views/images/checkmark.png);"
            "}")

    def signUp_Button(self):
        signB = QPushButton("Crear Cuenta", self)
        signB.setFont(QFont('Now', 20))
        font = signB.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        signB.setFont(font)
        signB.resize(225, 60)
        signB.move(545+430, 780)
        signB.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        signB.setStyleSheet(
            """color:#FFF9F2; background-color:#594E3F; border-radius: 30px""")
        signB.clicked.connect(self.SignUp_clicked)

    def close_button(self):
        closeAction = QApplication.instance().quit
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width-49, 0)
        button.setFont(QFont('Now', 20))
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px;
            change-cursor: cursor('PointingHand')""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(closeAction)

    def back_button(self):
        button = QPushButton('«', self)
        button.resize(50, 50)
        button.move(545, 0)
        button.setFont(QFont('Now', 20))
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-top-left-radius:20px; border-bottom-right-radius:20px;
            change-cursor: cursor('PointingHand')""")
        font = button.font()
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.back_clicked)

    def back_clicked(self):
        self.logwin = LoginWindow()
        self.logwin.show()
        timer = QTimer(self)
        timer.start(5)
        timer.timeout.connect(self.close)

    def SignUp_clicked(self):  # validar las entradas
        adress = self.user_line.text()
        name = self.name_line.text()
        user = self.user_line.text()
        password = self.pass_line.text()
        confirmpass = self.confirm_line.text()
        isAdmin = self.admin_box.isChecked()
        if password != confirmpass:
            pass
        else:
            if isAdmin:
                pass
                self.control.new_admin(name, password)
            else:
                self.control.new_cliente(user, password)

    def confirmLineClick(self):  # arreglar(para validar igualdad de password)
        password = self.pass_line.text()
        passconfirm = self.confirm_line.text()
        if password != passconfirm:
            self.show_label.setFont(QFont('Now', 15))
            self.show_label.resize(290, 33)
            font = self.show_label.font()
            self.show_label.setFont(font)
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            self.show_label.move(545+61+450+63, 580)
            self.show_label.setStyleSheet("""color:red""")
            self.show_label.setText('Las contraseñas no coinciden')
        else:
            self.show_label.setText('')

    def config_label(self, label: QLabel, x: int, y: int):
        label.setFont(QFont('Now', 20))
        font = label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("""color:#868179""")

    def config_linesEdit_text(self, lineEdit: QLineEdit, x: int, y: int, width: int, height: int):
        lineEdit.setFont(QFont('Now', 18))
        lineEdit.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px; 
                                    border-color: transparent; border-bottom-color: #868179""")
        font = lineEdit.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        lineEdit.setFont(font)
        lineEdit.resize(width, height)
        lineEdit.move(x, y)

    def config_linesEdit_pass(self, lineEdit: QLineEdit, x: int, y: int, width: int, height: int):
        lineEdit.setFont(QFont('Now', 18))
        lineEdit.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px; 
                                    border-color: transparent; border-bottom-color: #868179""")
        lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        lineEdit.resize(width, height)
        lineEdit.move(x, y)


def Main():  # ________________________________________________________________________________________________________
    app = QApplication(sys.argv)
    LogWin = LoginWindow()
    app.exec()
