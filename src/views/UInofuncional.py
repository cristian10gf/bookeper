import typing
from datetime import datetime
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QRect, pyqtSignal, QObject, QEvent, QTimer, QTime
from PyQt6.QtGui import QFont, QIcon, QPixmap, QCursor, QPainter, QPaintEvent
from PyQt6.QtWidgets import (QApplication, QToolTip, QWidget, QMainWindow, QPushButton, QTextEdit, QLineEdit, QCheckBox, QLabel,
                             QScrollArea, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QSpacerItem, QDialog)
from functools import partial
import sys
from src.Controllers.control_bookeeper import ControlBookeeper


class CustomEdit(QLineEdit):
    def mousePressEvent(self, event):
        text = self.text()
        if event.button() == Qt.MouseButton.LeftButton and text == 'Buscar Libro':
            self.setText('')


# ______________________________________________________________________________________
class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.width = 1630
        self.height = 980
        if open('src/views/user_active.txt', 'r').read() != '':
            self.holdSesion = True
        else:
            self.holdSesion = False
        self.StartUp()
        self.control = ControlBookeeper()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#594E3F; border-radius: 20px;
                        background-image: url(src/views/images/Backimage.jpg)""")
        lg = QLabel(self)
        lg.move(945, 0)
        lg.resize(self.width - 945, self.height)
        lg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px""")
        ################################################
        self.labels()
        self.linesEdits()
        self.loggin_button()
        self.newCount_button()
        if self.holdSesion:  # antes de esto se debe ejecutar un codigo para saber cual usuario tiene la sesion activa
            user_active = open('src/views/user_active.txt', 'r').read()
            self.UserWin = UserWindow(user_active)
            self.UserWin.show()
            timer = QTimer(self)
            timer.start(5)
            timer.timeout.connect(self.close)
        #########1############
        self.minimize_button()
        self.close_button()
        self.center()  #
        self.show()  #
        #####################


    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def linesEdits(self):
        #   user
        self.user_line = QLineEdit(self)
        self.user_line.setFont(QFont('Now', 20))
        self.user_line.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px;
                                    border-color: transparent; border-bottom-color: #868179""")
        font = self.user_line.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.user_line.setFont(font)
        self.user_line.resize(485, 40)
        self.user_line.move(1045, 475)
        #   password
        self.pass_line = QLineEdit(self)
        self.pass_line.setFont(QFont('Now', 20))
        self.pass_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_line.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px;
                                    border-color: transparent; border-bottom-color: #868179""")
        self.pass_line.resize(485, 40)
        self.pass_line.move(1045, 630)

    def labels(self):
        #   title
        title_label = QLabel(' BooKeeper', self)
        title_label.setFont(QFont('Nickainley', 80, ))
        title_label.move(1000, 30)
        title_label.resize(580, 200)
        title_label.setStyleSheet("""color:#594E3F""")
        #   welcome
        welcome_label = QLabel('¡Bienvenido a BooKeeper!', self)
        welcome_label.setFont(QFont('Now', 32))
        font = welcome_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        welcome_label.setFont(font)
        welcome_label.move(1015, 220)
        welcome_label.setStyleSheet("""color:#868179""")
        #   user or address
        user_label = QLabel('Usuario o Correo', self)
        user_label.setFont(QFont('Now', 24))
        font = user_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        user_label.setFont(font)
        user_label.move(1045, 430)
        user_label.setStyleSheet("""color:#868179""")
        #   password
        pass_label = QLabel('Contraseña', self)
        pass_label.setFont(QFont('Now', 24))
        font = pass_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        pass_label.setFont(font)
        pass_label.move(1045, 585)
        pass_label.setStyleSheet("""color:#868179""")
        # Label del error
        # self.errorinicio_label= QLabel('', self)
        self.errorinicio_label = QLabel('                                             ', self)

        self.errorinicio_label.setFont(QFont('Now', 18))

    def linesEdits(self):
        #   user
        self.user_line = QLineEdit(self)
        self.user_line.setFont(QFont('Now', 20))
        self.user_line.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px; 
                                    border-color: transparent; border-bottom-color: #868179""")
        font = self.user_line.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.user_line.setFont(font)
        self.user_line.resize(485, 40)
        self.user_line.move(1045, 475)
        #   password
        self.pass_line = QLineEdit(self)
        self.pass_line.setFont(QFont('Now', 20))
        self.pass_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.pass_line.setStyleSheet("""background-color: transparent; border-style: solid ;border-width: 2px; 
                                    border-color: transparent; border-bottom-color: #868179""")
        self.pass_line.resize(485, 40)
        self.pass_line.move(1045, 630)

    def newCount_button(self):
        #self.confirminicio = QLineEdit(self)
        #este es el cuadro que estaba en la esquina superior izquierda
        Ncount = QPushButton('¿Nueva Cuenta?', self)
        Ncount.setFont(QFont('Now', 18))
        font = Ncount.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        Ncount.setFont(font)
        Ncount.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        Ncount.move(1180, 840)
        Ncount.resize(213, 30)
        Ncount.setStyleSheet("""color:#868179; background-color:transparent""")
        Ncount.clicked.connect(self.newCount_clicked)

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

    def minimize_button(self):
        label = QLabel('', self)
        label.resize(70, 50)
        label.move(self.width - 98, 0)
        label.setStyleSheet(
            """background-color:#6B6051 ;border-bottom-left-radius: 20px""")
        button = QPushButton('-', self)
        button.resize(48, 50)
        button.move(self.width - 98, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color: none ;border-style:solid""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.showMinimized)

    def close_button(self):
        closeAction = QApplication.instance().quit
        closeB = QPushButton("x", self)
        closeB.resize(50, 50)
        closeB.move(self.width - 49, 0)
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

    def errorlogin(self, act: bool):
        # Mensaje de error
        if act == True:
            self.errorinicio_label.resize(700, 35)
            self.errorinicio_label.setText('Ingrese un Usuario valido')
            self.errorinicio_label.setFont(QFont('Now', 18))
            font = self.errorinicio_label.font()
            font.setBold(True)
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            self.errorinicio_label.setFont(font)
            self.errorinicio_label.move(1040, 700)
            self.errorinicio_label.setStyleSheet("""color:#868179""")

        else:
            self.errorinicio_label.setText('')

    # this must be valided*******************************************************
    def login_clicked(self):
        userData = self.user_line.text()
        passData = self.pass_line.text()
        if userData == '' and passData == '':
            self.errorlogin(True)
        if userData != '' and passData != '':
            if self.control.verificar_admin(userData, passData):
                self.errorlogin(False)
                print('admin')
                self.UserWin = UserWindow(userData)
                self.UserWin.show()
                timer = QTimer(self)
                timer.start(5)
                timer.timeout.connect(self.close)
                user_active = open('src/views/user_active.txt', 'w')
                user_active.write(userData)
                user_active.close()
                self.holdSesion = True
            elif self.control.verificar_cliente(userData, passData):
                self.errorlogin(False)
                print('cliente')
                self.UserWin = UserWindow(userData)
                self.UserWin.show()
                timer = QTimer(self)
                timer.start(5)
                timer.timeout.connect(self.close)
                # crea un archivo para guardar el usuario
                user_active = open('src/views/user_active.txt', 'w')
                user_active.write(userData)
                user_active.close()
                self.holdSesion = True
            else:
                print('no existe')
                self.user_line.setText('')
                self.pass_line.setText('')
                self.errorlogin(True)

    def newCount_clicked(self):
        self.SignWin = SignUpWindow()
        self.SignWin.show()
        timer = QTimer(self)
        timer.start(5)
        timer.timeout.connect(self.close)


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
                        background-image: url(bookeepe/src/views/images/Backimage.jpg)""")
        sg = QLabel(self)
        sg.move(545, 0)
        sg.resize(self.width - 545, self.height)
        sg.setStyleSheet(
            """background-color:#FFF9F2; border-radius: 20px;border-top-left-radius: 23px""")
        self.labels()
        self.linesEdits()
        self.signUp_Button()
        self.back_button()
        self.checkBox()
        ######################
        self.minimize_button()
        self.close_button()  #
        self.center()  #
        self.show()  #
        ######################

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def labels(self):
        #   title
        title_label = QLabel(' BooKeeper', self)
        title_label.setFont(QFont('Nickainley', 80, ))
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
        self.config_label(adress_label, 545 + 61, 370)
        #   name
        name_label = QLabel('Nombre y Apellido', self)
        self.config_label(name_label, 545 + 61, 500)
        #   user
        user_label = QLabel('Nombre de Usuario', self)
        self.config_label(user_label, 545 + 61, 630)
        #   password
        pass_label = QLabel('Contraseña', self)
        self.config_label(pass_label, 545 + 61 + 450 + 63, 370)
        #   confirm password
        confirm_label = QLabel('Confirmar Contraseña', self)
        self.config_label(confirm_label, 545 + 61 + 450 + 63, 500)
        #   show
        self.show_label = QLabel('', self)

    def linesEdits(self):
        #   Adress
        self.adress_line = QLineEdit(self)
        self.config_linesEdit_text(self.adress_line, 545 + 61, 410, 450, 40)
        #   name
        self.name_line = QLineEdit(self)
        self.config_linesEdit_text(self.name_line, 545 + 61, 540, 450, 40)
        #   user
        self.user_line = QLineEdit(self)
        self.config_linesEdit_text(self.user_line, 545 + 61, 670, 450, 40)
        #   password
        self.pass_line = QLineEdit(self)
        self.config_linesEdit_pass(self.pass_line, 545 + 61 + 450 + 63, 410, 450, 40)
        #   confirm pass
        self.confirm_line = QLineEdit(self)
        self.confirm_line.textChanged.connect(self.confirmLineTyping)
        self.config_linesEdit_pass(
            self.confirm_line, 545 + 61 + 450 + 63, 540, 450, 40)

    def checkBox(self):
        self.admin_box = QCheckBox('Administrador', self)
        self.admin_box.setFont(QFont('Now', 20))
        font = self.admin_box.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.admin_box.setFont(font)
        self.admin_box.move(545 + 61 + 450 + 63, 630)
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
        signB.move(545 + 430, 780)
        signB.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        signB.setStyleSheet(
            """color:#FFF9F2; background-color:#594E3F; border-radius: 30px""")
        signB.clicked.connect(self.SignUp_clicked)

    def close_button(self):
        closeAction = QApplication.instance().quit
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width - 49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(closeAction)

    def minimize_button(self):
        label = QLabel('', self)
        label.resize(70, 50)
        label.move(self.width - 98, 0)
        label.setStyleSheet(
            """background-color:#6B6051 ;border-bottom-left-radius: 20px""")
        button = QPushButton('-', self)
        button.resize(48, 50)
        button.move(self.width - 98, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color: none ;border-style:solid""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.showMinimized)

    def back_button(self):
        button = QPushButton('«', self)
        button.resize(50, 50)
        button.move(545, 0)
        button.setFont(QFont('Now', 20))
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-top-left-radius:20px; border-bottom-right-radius:20px""")
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.back_clicked)

    def back_clicked(self):
        self.logwin = LoginWindow()
        self.logwin.show()
        timer = QTimer(self)
        timer.start(5)
        timer.timeout.connect(self.close)

    def SignUp_clicked(
            self):  # se requiere mostrar un mensaje de diciendo que el usuario ya existe o que se requieren campos llenos
        adress = self.user_line.text()
        name = self.name_line.text()
        user = self.user_line.text()
        password = self.pass_line.text()
        confirmpass = self.confirm_line.text()
        isAdmin = self.admin_box.isChecked()
        if password != confirmpass:
            pass
        else:
            if isAdmin and self.control.verificar_admin(user, password, 2) is False and user != '' and password != '':
                self.control.new_admin(name, password)
                self.back_clicked()
            elif isAdmin is False and self.control.verificar_cliente(user, password,
                                                                     2) is False and user != '' and password != '':
                self.control.new_cliente(user, password)
                self.back_clicked()
            else:
                # se requiere mostrar un mensaje de diciendo que el usuario ya existe o que se requieren campos llenos
                self.user_line.setText('')
                self.name_line.setText('')
                self.user_line.setText('')
                self.pass_line.setText('')
                self.confirm_line.setText('')

    def confirmLineTyping(self):
        password = self.pass_line.text()
        passconfirm = self.confirm_line.text()
        if password != passconfirm:
            self.show_label.setFont(QFont('Now', 15))
            self.show_label.resize(290, 33)
            font = self.show_label.font()
            self.show_label.setFont(font)
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            self.show_label.move(545 + 61 + 450 + 63, 580)
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


# _____________________________________________________________________________________
class UserWindow(QWidget):
# ____________________funciones escenciales_________________________
    def __init__(self, usuario: str) -> None:
        super(UserWindow, self).__init__()
        self.control = ControlBookeeper()
        self.usuario = usuario
        self.width = 1630
        self.height = 980
        self.boolAdmin = self.control.verificar_admin(usuario, '', 2)
        self.searchMode = 'Nombre'
        self.userName = usuario
        self.userImage = QPixmap("src/views/images/usuario.png")
        self.userImage = self.userImage.scaled(self.userImage.size(
        ), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.infoArea=None
        self.StartUp()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        # | QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#8C7662; border-radius: 20px;""")
        lg = QLabel(self)
        lg.move(1205, 0)
        lg.resize(self.width - 1205, self.height)  # 405, 980
        lg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px""")
        ######################
        self.searchBar()                      # barra de busqueda
        self.tagButtons()                     # botones de busqueda
        self.shelves_box()
        self.seemostrarlibrosde_button()      # ver todos los libros
        if self.boolAdmin:
            self.addShelve_button()           # add estante
            self.seeBorroweds_button()        # ver libros prestados
            self.admin = self.control.get_admin_by_name(self.userName)
        else:
            self.prestamo_button()            # ver mis prestamos
            self.cliente = self.control.get_cliente(1, self.userName)
        self.userInfo()                       # muestra el nombre del usuario
        self.viewProfile_button()             # ver perfil
        self.logOut_button()                  # cerrar sesion
        self.init_Shelve()                    # Mostrar Estantes Creados
        ########################
        self.minimize_button()
        self.close_button()  #
        self.center()  #
        self.show()  #
        ########################

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def secondBox(self):  # background
        if not self.shelveScroll.isHidden():
            self.shelveScroll.hide()
            self.back_button()
            self.boxScroll = QScrollArea(self)
            self.boxScroll.hide()
        ##############################
            if self.boxScroll.isVisible():
                self.boxScroll.deleteLater()
                self.boxScroll = QScrollArea(self)
        #######################################
        self.boxScroll.move(20, 200)
        self.boxScroll.resize(1175, 730)  # -1186,780
        self.boxScroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.boxScroll.setWidgetResizable(True)
        self.boxScroll.setStyleSheet(
            """
            QScrollArea{
                background-color: transparent;
                border:none;
                }
            QScrollBar:vertical{
                background-color: transparent;
                margin: 17px 1 17px 1;
                border-radius: 0px;
            }
            QScrollBar::handle:vertical{
                background-color:#FFF9F2;
                border-radius: 7px;
            }
            QScrollBar::sub-line:vertical{
                border:none;
                background-color:transparent;
                height:15px;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                margin:0px 1 0px 1;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical:hover{
                background-color:#FFF9F2;
            }
            QScrollBar::add-line:vertical{
                border:none;
                background-color:transparent;
                height:15px;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                margin:0px 1 0px 1;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::add-line:vertical:hover{
                background-color:#FFF9F2;
            }
            QScrollBar::up-arrow:vertical,QScrollBar::down-arrow:vertical{
                background-color: none;
            }
            QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{
                background-color: none;
            }
            """)
        self.searchWidget = QWidget()
        self.searchWidget.setGeometry(QRect(0, 0, 1188, 779))
        self.searchWidget.setStyleSheet(
            """background-color: transparent""")
        self.searchLayout = QVBoxLayout(self.searchWidget)
        self.searchLayout.addItem(QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding))
        self.boxScroll.setWidget(self.searchWidget)
        self.boxScroll.show()

    def showbook(self, name, autor, gender, estado):   # cuadro de un libro
        count = self.searchLayout.count()-1
        # exits = self.searchWidget.findChild(QGroupBox)
        # if exits is None:
        groupbox = QGroupBox('', self.searchWidget)
        groupbox.setStyleSheet(
            """background-color: none ;border-style:solid """)
        self.searchLayout.insertWidget(count, groupbox)
        ######################################################
        line = QLabel('', groupbox)
        line.setFixedHeight(5)
        line.setStyleSheet("""border-top: 3px solid #594E3F""")
        # name
        bookname = QPushButton(' '+name, groupbox)
        bookname.setStyleSheet(
            """color: #FFF9F2 ;border: solid transparent""")
        bookname.setFont(QFont('Now', 26))
        font = bookname.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        bookname.setFont(font)
        bookname.setCursor(
        QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        bookname.clicked.connect(self.bookInfo(name))
        # autor
        bookautor = QLabel('      '+autor, groupbox)
        bookautor.setStyleSheet("""color: #FFF9F2""")
        bookautor.setFont(QFont('Now', 20))
        font = bookautor.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        bookautor.setFont(font)
        # gender
        bookgender = QLabel('      '+gender, groupbox)
        bookgender.setStyleSheet("""color: #FFF9F2""")
        bookgender.setFont(QFont('Now', 20))
        font = bookgender.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        bookgender.setFont(font)
        # year


        #bookyear = QLabel('      ' + anopubli, groupbox)
        #bookyear.setStyleSheet("""color: #FFF9F2""")
        #bookyear.setFont(QFont('Now', 20))
        #font = bookyear.font()
        #font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        #bookyear.setFont(font)
        ################################
        grid = QGridLayout(groupbox)
        grid.addWidget(line, 0, 0, 1, 5)
        grid.addWidget(bookname, 1, 0, 1, 4, Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(bookautor, 2, 0, 1, 4, Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(bookgender, 3, 0, 1, 4,
                             Qt.AlignmentFlag.AlignLeft)
        #grid.addWidget(bookyear, 4, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)
        ################################
        if estado ==  None: 
            prestar = QPushButton('Prestar', groupbox)
            prestar.setFixedSize(180, 50)
            prestar.setStyleSheet(
                """color: #FFF9F2 ;background-color: #594E3F ;border: solid #594E3F ;border-radius: 25px""")
            prestar.setFont(QFont('Now', 26))
            font = prestar.font()
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            prestar.setFont(font)
            prestar.setCursor(
                QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            if self.boolAdmin is True:
                # name es el nombre del libro
                prestar.clicked.connect(partial(self.confirmLendingTo, name))
            else:
                prestar.clicked.connect(partial(self.lending, name))
            grid.addWidget(prestar, 2, 4, 1, 1,
                                 Qt.AlignmentFlag.AlignCenter)

        # se debe buscar si el dueño actual es igual al nombre del usuario
        elif self.userName == estado.cliente.nombre:
            devolver = QPushButton('Devolver', groupbox)
            devolver.setFixedSize(180, 50)
            devolver.setStyleSheet(
                """color: #FFF9F2 ;background-color: #594E3F ;border: solid #594E3F ;border-radius: 25px""")
            devolver.setFont(QFont('Now', 26))
            font = devolver.font()
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            devolver.setFont(font)
            devolver.setCursor(
                QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            devolver.clicked.connect(partial(self.returnBook, name))
            # add
            grid.addWidget(devolver, 2, 4, 1, 1,
                                 Qt.AlignmentFlag.AlignCenter)


# _______ cosas relacionadas al login________________________________________
    def userInfo(self):
        image = QLabel(self)
        image.resize(305, 305)
        image.move(self.width - 305 - 60, 40)
        image.setScaledContents(True)
        image.setPixmap(self.userImage)
        image.setStyleSheet("""background-color:none""")
        self.Labelname = QLabel(self.userName, self)
        self.Labelname.setFont(QFont('Now', 24))
        font = self.Labelname.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.Labelname.setFont(font)
        self.Labelname.setStyleSheet(
            """color:#594E3F ;background-color:none ;border-radius: 30px""")
        self.Labelname.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        #
        widget = QWidget(self)
        widget.resize(425, 50)
        widget.move(1205, 320)
        widget.setStyleSheet("""background-color:none""")
        layout = QHBoxLayout(widget)
        layout.addWidget(self.Labelname)

    def logOut_button(self):
        button = QPushButton('Cerrar Sesión', self)
        button.setFont(QFont('Now', 24))
        button.resize(245, 60)
        button.move(1295, 830)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px""")
        button.clicked.connect(self.logOut_clicked)

    def logOut_clicked(self):
        user_active = open('src/views/user_active.txt', 'w')
        user_active.write('')
        user_active.close()
        self.logwin = LoginWindow()
        self.logwin.show()
        timer = QTimer(self)
        timer.start(5)
        timer.timeout.connect(self.close)
        
        self.control.actualizar_todo()

    def viewProfile_button(self):
        label = QLabel(self)
        label.resize(245, 200)
        label.move(1295, 720)
        label.setStyleSheet(
            """background-color:#594E3F ;border-radius: 30px""")
        #
        self.profile_but = QPushButton('Ver Perfil', self)
        self.profile_but.setFont(QFont('Now', 24))
        self.profile_but.resize(165, 60)
        self.profile_but.move(1335, 750)
        font = self.profile_but.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        self.profile_but.setFont(font)
        self.profile_but.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.profile_but.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px""")
        self.profile_but.clicked.connect(self.viewProfile_clicked)

    def viewProfile_clicked(self):
        print(self.userName)
        self.profilewin = ProfileWindow(parent=self, user=self.usuario)
        self.hide()
        self.profilewin.show()


# _______ cosas relacionadas a los estantes ___________________________
    def shelves_box(self):  # caja de estantes
        self.shelveScroll = QScrollArea(self)
        self.shelveScroll.move(20, 200)
        self.shelveScroll.resize(1175, 730)  # -1186,780
        self.shelveScroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.shelveScroll.setWidgetResizable(True)
        self.shelveScroll.setStyleSheet(
            """
            QScrollArea{
                background-color: transparent;
                border:none;
                }
            QScrollBar:vertical{
                background-color: transparent;
                margin: 17px 1 17px 1;
                border-radius: 0px;
            }
            QScrollBar::handle:vertical{
                background-color:#FFF9F2;
                border-radius: 7px;
            }
            QScrollBar::sub-line:vertical{
                border:none;
                background-color:transparent;
                height:15px;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                margin:0px 1 0px 1;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical:hover{
                background-color:#FFF9F2;
            }
            QScrollBar::add-line:vertical{
                border:none;
                background-color:transparent;
                height:15px;
                border-top-left-radius: 7px;
                border-top-right-radius: 7px;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                margin:0px 1 0px 1;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::add-line:vertical:hover{
                background-color:#FFF9F2;
            }
            QScrollBar::up-arrow:vertical,QScrollBar::down-arrow:vertical{
                background-color: none;
            }
            QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{
                background-color: none;
            }
            """)
        self.shelveWidget = QWidget()
        self.shelveWidget.setGeometry(QRect(0, 0, 1188, 779))
        self.shelveWidget.setStyleSheet("""background-color: transparent;""")
        self.shelveLayout = QVBoxLayout(self.shelveWidget)
        self.shelveLayout.addItem(QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding))
        self.shelveScroll.setWidget(self.shelveWidget)

    def addShelve_button(self):  # boton de agregar estante
        button = QPushButton('Agregar Estante', self)
        button.setFont(QFont('Now', 24))
        button.resize(295, 60)
        button.move(1185 + 85, 610)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet("""color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px; padding-left: 14px
                            ;padding-right: 12px""")
        button.clicked.connect(self.confirmAdd)
    
    def addShelve_clicked(self, estante, bk1='Libro 1', bk2='Libro 2', bk3='Libro 3', bk4='Libro 4', no_guardar=False):
        count = self.shelveLayout.count() - 1
        shelveGroup = QGroupBox('', self.shelveWidget)
        shelveGroup.setStyleSheet(
            """background-color: none;border-style:solid; """)
        self.shelveLayout.insertWidget(count, shelveGroup)
        ################################
        grid = QGridLayout(shelveGroup)
        # label
        shelve_label = QLabel(estante, shelveGroup)
        shelve_label.setStyleSheet(
            """color: #FFF9F2 ;font:34px Now ;border-bottom: 3px solid #594E3F""")
        font = shelve_label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        shelve_label.setFont(font)
        # seeMore
        seeMore = QPushButton('Ver todo')
        seeMore.setStyleSheet(
            """color: #FFF9F2 ;background-color:none ;font: 24px Now ;text-align: center""")
        seeMore.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        font = seeMore.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        seeMore.setFont(font)
        seeMore.clicked.connect(self.seeMore_clicked)
        # AñadirLibro
        añadirLibro_button = QPushButton('Agregar libro')
        añadirLibro_button.setStyleSheet(
            """color: #FFF9F2 ;background-color:none ;font: 24px Now ;text-align: center""")
        añadirLibro_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        font = añadirLibro_button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        añadirLibro_button.setFont(font)
        añadirLibro_button.clicked.connect(self.añadirLibro_confirm)
        # delete
        delete = QPushButton(shelveGroup)
        delete.setStyleSheet(
            """background-color:none ;border-style:none; border-radius: 20px ;image: url("PooProyect/images/cancelar.png")""")
        delete.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        font = delete.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        delete.setFont(font)
        delete.clicked.connect(self.deleteConfirm)
        #
        book1 = QGroupBox('')
        self.config_BookBox(book1, bk1)
        book2 = QGroupBox('')
        self.config_BookBox(book2, bk2)
        book3 = QGroupBox('')
        self.config_BookBox(book3, bk3)
        book4 = QGroupBox('')
        self.config_BookBox(book4, bk4)
        #############################################
        grid.addWidget(shelve_label, 0, 0, 1, 15)
        grid.addWidget(seeMore, 0, 0, 1, 15,
                       Qt.AlignmentFlag.AlignRight)
        grid.addWidget(book1, 1, 0, 1, 3)
        grid.addWidget(book2, 1, 4, 1, 3)
        grid.addWidget(book3, 1, 8, 1, 3)
        grid.addWidget(book4, 1, 12, 1, 3)
        grid.addWidget(shelveGroup, 1, 14, 1, 4)
        grid.addWidget(añadirLibro_button, 2, 0, 1, 15,
                       Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(delete, 2, 14, 1, 1,
                       Qt.AlignmentFlag.AlignRight)

    def init_Shelve(self): # Mostrar Estantes Creados
        estantes = self.control.get_estantes()
        for estante in estantes:
            if len(estante.libros) == 4:
                self.addShelve_clicked(estante=estante.genero, bk1=estante.libros[0], bk2=estante.libros[1],
                                       bk3=estante.libros[2], bk4=estante.libros[3], no_guardar=True)
            elif len(estante.libros) == 3:
                self.addShelve_clicked(estante=estante.genero, bk1=estante.libros[0], bk2=estante.libros[1],
                                       bk3=estante.libros[2], bk4='libro 4', no_guardar=True)
            elif len(estante.libros) == 2:
                self.addShelve_clicked(estante=estante.genero, bk1=estante.libros[0], bk2=estante.libros[1],
                                       bk3='libro 3', bk4='libro 4', no_guardar=True)
            elif len(estante.libros) == 1:
                self.addShelve_clicked(estante=estante.genero, bk1=estante.libros[0], bk2='libro 2', bk3='libro 3',
                                       bk4='libro 4', no_guardar=True)
            else:
                self.addShelve_clicked(estante=estante.genero, bk1='libro 1', bk2='libro 2', bk3='libro 3',
                                       bk4='libro 4', no_guardar=True)

    def config_BookBox(self, GBox, libro: 'Libro'): # cuadro de un libro en un estante
        GBox.setMaximumSize(200, 210)
        GBox.setStyleSheet(
            """background-color: #594E3F ;border-radius: 20px """)
        layV = QVBoxLayout(GBox)
        layV.addSpacing(20)
        # item
        space = QSpacerItem(20, 30)
        # 4
        if isinstance(libro, str):
            label_4 = QLabel('Fecha lanzamiento')
        else:
            label_4 = QLabel(str(libro.fecha_lanzamiento))
        label_4.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:20px Now""")
        font = label_4.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label_4.setFont(font)
        # 3
        if isinstance(libro, str):
            label_3 = QLabel('Género')
        else:
            label_3 = QLabel(libro.genero)
        label_3.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:20px Now""")
        font = label_3.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label_3.setFont(font)
        # 2
        if isinstance(libro, str):
            label_2 = QLabel('Autor')
        else:
            autores = ''
            for i in range(0, len(libro.autores), 1):
                autores += str(libro.autores[i]) + ', '
            label_2 = QLabel(autores)
        label_2.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:20px Now""")
        font = label_2.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label_2.setFont(font)
        # 1
        if isinstance(libro, str):
            label_1 = QLabel('Nombre')
        else:
            label_1 = QLabel(libro.nombre)
        label_1.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:28px Now""")
        font = label_1.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        if isinstance(libro, str):
            text_length = label_1.fontMetrics().horizontalAdvance(libro)
        else:
            text_length = label_1.fontMetrics().horizontalAdvance(libro.nombre)
        if text_length > 60:
            label_1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        else:
            label_1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label_1.setFont(font)
        #
        layV.addWidget(label_1)
        layV.addWidget(label_2)
        layV.addWidget(label_3)
        layV.addWidget(label_4)
        layV.addItem(space)


# _______ botones de funciones especificas ________________________________________________

    def minimize_button(self):
        label = QLabel('', self)
        label.resize(70, 50)
        label.move(self.width - 98, 0)
        label.setStyleSheet(
            """background-color:#6B6051 ;border-bottom-left-radius: 20px""")
        button = QPushButton('-', self)
        button.resize(48, 50)
        button.move(self.width - 98, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color: none ;border-style:solid""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.showMinimized)

    def close_button(self):
        closeAction = QApplication.instance().quit
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width - 49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px;
            change-cursor: cursor('PointingHand')""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.pressed.connect(self.guardar)
        button.clicked.connect(closeAction)

    def guardar(self):
        self.control.actualizar_todo()
    
    def back_button(self):
        button = QPushButton('«', self)
        button.resize(30, 30)
        button.move(40, 175)
        button.setFont(QFont('Now', 30))
        button.setStyleSheet(
            """color: #FFF9F2 ; background-color:none ;border-style: solid""")
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.back_clicked)
        button.show()

    def back_clicked(self):
        button = self.sender()
        button.deleteLater()
        self.boxScroll.deleteLater()
        self.shelveScroll.show()
        self.shelveScroll.setEnabled(True)


# _______________busqueda de libros ________________________________________

    def searchBar(self):  # terminar la busqueda
        self.bar = CustomEdit('Buscar Libro', self)
        self.bar.setFont(QFont('Now', 20))
        self.bar.resize(905, 60)
        self.bar.move(150, 20)
        self.bar.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.bar.setStyleSheet("""color: #594E3F;background-color:#FFF9F2; border-style: solid ;border-radius: 30px;
                        border-bottom-color: #FFF9F2; padding-left: 30px; padding-right: 30px""")
        font = self.bar.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.bar.setFont(font)
        button = QPushButton(self)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet(
            """background-color:none ;border-style:none; border-radius: 20px ;image: url("src/views/images/len.png")""")
        button.resize(50, 50)
        button.move(995, 25)
        button.move(995, 25)
        button.clicked.connect(self.search)

    def search(self):  # validar el tipo de busqueda
        self.secondBox()
        if self.searchMode == 'Nombre':
            libros = list(set(self.control.get_libro_by_name(self.bar.text())))
            if len(libros) > 0:
                for lib in libros:
                    self.showbook(name=lib.nombre,
                                  autor=lib.autores[0], gender=lib.genero, estado=lib.estado)
            else:
                print("no se encontro el libro")

        elif self.searchMode == 'Género':
            libros = list(set(self.control.get_libro_by_genre(self.bar.text())))
            if len(libros) > 0:
                for lib in libros:
                    self.showbook(name=lib.nombre,
                                  autor=lib.autores[0], gender=lib.genero, estado=lib.estado)
            else:
                print("no se encontro el libro")

        elif self.searchMode == 'Autor':
            libros = list(set(self.control.get_libro_by_author(self.bar.text())))
            if len(libros) > 0:
                for lib in libros:
                    nautor= lib.autores[0]
                    for autor in lib.autores:
                        if self.bar.text() in autor:
                            nautor = autor

                    self.showbook(name=lib.nombre,
                                  autor=nautor, gender=lib.genero, estado=lib.estado)
            else:
                print("no se encontro el libro")

    def mousePressEvent(self, event):
        text = self.bar.text()
        if event.button() == Qt.MouseButton.LeftButton and event.pos() not in self.bar.geometry():
            self.bar.clearFocus()
            if text == '':
                self.bar.setText('Buscar Libro')

    def tagButton1_clicked(self):
        self.searchMode = 'Nombre'
        self.button1.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        self.button2.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        self.button3.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")

    def tagButton2_clicked(self):
        self.searchMode = 'Género'
        self.button2.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        self.button1.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        self.button3.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")

    def tagButton3_clicked(self):
        self.searchMode = 'Autor'
        self.button3.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        self.button2.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        self.button1.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")

    def tagButtons(self):
        # 1
        self.button1 = QPushButton('Nombre', self)
        self.button1.setFont(QFont('Now', 20))
        self.button1.resize(150, 60)
        self.button1.move(327, 100)
        self.button1.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        font = self.button1.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.button1.setFont(font)
        self.button1.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # 2
        self.button2 = QPushButton('Género', self)
        self.button2.setFont(QFont('Now', 20))
        self.button2.resize(151, 60)
        self.button2.move(527, 100)
        self.button2.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ; border-style: solid ;border-radius: 30px""")
        font = self.button2.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.button2.setFont(font)
        self.button2.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        # 3
        self.button3 = QPushButton('Autor', self)
        self.button3.setFont(QFont('Now', 20))
        self.button3.resize(151, 60)
        self.button3.move(728, 100)
        self.button3.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ; border-style: solid ;border-radius: 30px""")
        font = self.button3.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.button3.setFont(font)
        self.button3.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.button1.clicked.connect(self.tagButton1_clicked)
        self.button2.clicked.connect(self.tagButton2_clicked)
        self.button3.clicked.connect(self.tagButton3_clicked)

    def mousePressEvent(self, event):
        text = self.bar.text()
        if event.button() == Qt.MouseButton.LeftButton and event.pos() not in self.bar.geometry():
            self.bar.clearFocus()
            if text == '':
                self.bar.setText('Buscar Libro')
            else:
                self.search()





# cosas por arreglar ____________________________________________________________________________

# ______ prestamo funcionalidad ____________________________________________________________
 
    def ver_mis_prestamos(self):
        self.secondBox()
        self.books_prestados_for_client()

    def books_prestados_for_client(self):
        books_prestados = []
        for cliente in self.control.get_clientes():
            if cliente.nombre == self.userName:
                cliente_buscado = cliente
        prestamos_del_usuario = self.control.get_prestamos(cliente_buscado)
        if prestamos_del_usuario is not None:
            for prestamo in prestamos_del_usuario:
                books_prestados.append(prestamo.libro)
            for book in books_prestados:
                self.showbook(book.nombre, book.autores[0], book.genero, book.estado)
  
    def prestamo_button(self):
        button = QPushButton('mis prestamos', self)
        button.setFont(QFont('Now', 24))
        button.resize(295, 60)
        button.move(1185 + 85, 610)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet("""color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px; padding-left: 14px
                            ;padding-right: 12px""")
        button.clicked.connect(self.ver_mis_prestamos)

    def init_books_prestados(self) -> None:
        books_prestados = []
        if self.control.verificar_admin(self.userName, 'books_prestados', 2):
            '''for cliente in self.control.get_clientes():
                for libro in cliente.ver_libros_prestados():
                    books_prestados.append(libro.libro)'''
            books_prestados = self.control.get_libros_prestados()
            print(books_prestados)
            for book in books_prestados:
                self.showbook(book.nombre, book.autores[0], book.genero, book.estado)

    def seeBorroweds_button(self):
        button = QPushButton('Ver prestamos', self)
        button.setFont(QFont('Now', 24))
        button.resize(295, 60)
        button.move(1185 + 85, 510)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet("""color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px; padding-left: 14px
                            ;padding-right: 12px""")
        button.clicked.connect(self.seeBorroweds_clicked)

    def seeBorroweds_clicked(self):
        if not self.infoArea is None:
            self.infoArea.deleteLater()
            self.infoArea=None
        self.secondBox()
        self.init_books_prestados()

    def lending(self, book):
        botton = self.sender()
        botton.deleteLater()
        usuarios = self.control.get_clientes()
        for usuario in usuarios:
            if usuario.nombre == self.userName:
                user_a_prestar = usuario
        self.control.new_prestamo(fecha= datetime.now(), id_cliente = user_a_prestar.codigo_Usuario, nombre = book.nombre)
# ↑se debe agregar internamente el libro al usuario

    def confirmLendingTo(self, book):
        self.ledwin = LendBookTo(win=self, bookname=book)
        self.ledwin.show()
        # se debe mandar el libro

    def ledTo(self, user: 'Cliente', book: 'Libro'):
        self.control.new_prestamo(fecha= datetime.now(), id_cliente = user.codigo_Usuario, nombre = book.nombre )
# ↑se debe agregar internamente el libro al usuario






# ____ ver libros prestados ____________________________________________

    def seeBooks_button(self):
        button = QPushButton('Ver mis libros', self)
        button.setFont(QFont('Now', 24))
        button.resize(295, 60)
        button.move(1185 + 85, 510)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet("""color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px; padding-left: 14px
                            ;padding-right: 12px""")
        button.clicked.connect(self.seeBooks_clicked)

    def seeBooks_clicked(self):
        if not self.infoArea is None:
            self.infoArea.deleteLater()
            self.infoArea=None
        self.secondBox()
        todos_los_libros = self.control.get_libros()
        for libro in todos_los_libros:
            self.showbook(libro.nombre, libro.autores[0], libro.genero, libro.estado)

    def seemostrarlibrosde_button(self):
        button = QPushButton('Ver libros', self)
        button.setFont(QFont('Now', 24))
        button.resize(295, 60)
        button.move(1185 + 85, 410)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet("""color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px; padding-left: 14px
                            ;padding-right: 12px""")
        button.clicked.connect(self.seemostrarlibrosdeConfirm)

    def seemostrarlibrosde(self, user):
        if not self.infoArea is None:
            self.infoArea.deleteLater()
            self.infoArea=None
        self.secondBox()
        self.showbook(name=f'Libro de {user}', autor=user, gender='unknown', estado= None)
# ↑se deben mbuscar los libros del usuario para mostrarlos

    def seemostrarlibrosdeConfirm(self):
        self.seebookWin = SeeBooksSomeone(self)
        self.seebookWin.show()
#estas 2 son la misma
    def seemostrarlibrosde_clicked(self):
        self.secondBox()
        self.showbook(name=f'Libro de {user}', autor=user, gender='unknown',estado =None)
# ↑se deben mbuscar los libros del usuario para mostrarlos

    def seemostrarlibrosdeConfirm(self):
        self.seebookWin = SeeBooksSomeone(self)
        self.seebookWin.show()



    def seeMore_clicked(self):
        box = self.sender().parent()
        layout = box.layout()
        item = layout.itemAtPosition(0, 0).widget()
        itemName = item.text()
        self.secondBox()
        #self.showbook(name='libro de'+itemName, autor='yo', gender='idk', estado = None)
        # ↑internamente se deben buscar los libro de que estan en la estanteria con ese nombre

    def confirmAdd(self):
        self.shelvewin = AddShelveWindow(win=self, usuario=self.usuario)
        self.shelvewin.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.shelvewin.show()


# _________________ Añadir libro ______________________________
    def AñadirLibro(self, shelve, book, bookBox):
        libro = bookBox.itemAt(1).widget()
        libro.setText(book)
        #
        autor = bookBox.itemAt(2).widget()
        autor.setText('juan lucas')
        #
        Genero = bookBox.itemAt(3).widget()
        Genero.setText('aventura')
        #
        calificacion = bookBox.itemAt(4).widget()
        calificacion.setText('5')
# ↑ internamente de debe añadir el libro a al estante

    def añadirLibro_confirm(self):
        box = self.sender().parent()
        layout = box.layout()
        shelveName = layout.itemAtPosition(0, 0).widget().text()
        # se debe saber cuantos libros tiene el estante para cambiar la estetica del estante
        # esto es un ejemplo de como deberia ser
        # if numBooks < 4:
        #   if numBooks < 3:
        #       pos = numBooks*4
        #   elif numBooks = 3:
        #       pos = 14
        # esto de abajo debe estar dentro del primer if
        pos = 0
        book = layout.itemAtPosition(1, pos).widget()
        bookBox = book.layout()
        # esto de abajo ya no debe estar dentro del if
        self.añadirLibroWin = AñadirLibroAestante(
            win=self, bookBox=bookBox, shelve=shelveName)
        self.añadirLibroWin.show()

    def deleteShelve(self, shelve):
        shelve.deleteLater()
# ↑ internamente tambien se debe eliminar la estanteria

    def deleteConfirm(self):
        shelve = self.sender().parent()
        self.deleteWin = Delete(win=self, shelve=shelve)

    def deleteShelve(self):
        padre = self.sender().parent()
        padre.deleteLater()
    # ↑internamente tambien se debe eliminar la estanteria

    def returnBook(self, book):
        padre = self.sender().parent()
        padre.deleteLater()
# ↑internamente tambien se debe eliminar el libro del usuario


# ___________________ ver info de un libro ______________________________
    def backButton2(self, padre):
        button = QPushButton('«', padre)
        button.resize(30, 30)
        button.move(20, 0)
        button.setFont(QFont('Now', 30))
        button.setStyleSheet(
            """color: #FFF9F2 ; background-color:none ;border-style: solid""")  # FFF9F2
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.back_2_clicked)
        button.show()
        if not self.infoArea.isVisible:
            button.deleteLater()

    def back_2_clicked(self):
        button = self.sender()
        button.deleteLater()
        self.infoArea.deleteLater()
        self.infoArea=None
        self.boxScroll.show()
        self.boxScroll.setEnabled(True)

    def bookInfo(self, name: str):
        libro = self.control.get_libro_by_name(name)
        labels = []
        book = self.sender().text()
        self.boxScroll.hide()
        self.infoArea = QWidget(self)
        self.infoArea.setGeometry(QRect(20, 175, 1180, 700))
        self.infoArea.setStyleSheet("""background-color: #8C7662 """)
        name = QLabel(book, self.infoArea)
        name.move(60, 60)
        name.setStyleSheet(
            """color: #FFF9F2 ;border: solid transparent""")
        name.setFont(QFont('Now', 38))
        font = name.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        name.setFont(font)
        ######
        autor = QLabel('Autor/es '+ libro[0].guardar_autores() , self.infoArea)
        labels.append(autor)
        gender = QLabel('Género '+libro[0].genero, self.infoArea)
        labels.append(gender)
        date = QLabel('Fecha' + libro[0].fecha_fecha_lanzamiento, self.infoArea)
        labels.append(date)
        editorial = QLabel('Editorial '+libro[0].editorial, self.infoArea)
        labels.append(editorial)
        if libro[0].estado != None:
            state = QLabel('Estado: Prestado', self.infoArea)
            owner = QLabel(f'Dueño actual: {libro[0].estado.cliente}', self.infoArea)
            labels.append(owner)
        else:
            state = QLabel('Estado: Disponible', self.infoArea)
        labels.append(state)
        
        
        # rate=QLabel('Calificación', self.infoArea)
        # labels.append(rate)
        i = 1
        for label in labels:
            i = i + 1
            label.move(120, i * 70)
            label.setStyleSheet(
                """color: #FFF9F2 ;border: solid transparent""")
            label.setFont(QFont('Now', 32))
            font = label.font()
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            label.setFont(font)
        self.backButton2(padre=self.infoArea)
        self.infoArea.show()



# _____________________________________________________________________________________
class AddShelveWindow(QWidget):   # ventana agregar estante
    def __init__(self, win: UserWindow, usuario) -> None:
        super(AddShelveWindow, self).__init__()
        self.control = ControlBookeeper()
        self.usuario = usuario
        self.win = win
        self.width = 400
        self.height = 550
        self.StartUp()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint |
                            QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px;""")
        title = QLabel('Nuevo estante', self)
        title.setFont(QFont('Now', 24))
        title.move(30, 10)
        title.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        font = title.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        title.setFont(font)
        ########################
        self.labels()
        self.linesEdit()
        self.accept_button()
        ########################
        self.close_button()  #
        self.center()  #
        self.show()  #
        ########################

    def labels(self):
        # name
        name = QLabel('Nombre', self)
        self.config_label(name, 60, 85)
        # gender
        gender = QLabel('Género', self)
        self.config_label(gender, 60, 185)
        # max
        max = QLabel('Libros Máximos', self)
        self.config_label(max, 60, 285)

    def config_label(self, label: QLabel, x: int, y: int):
        label.setFont(QFont('Now', 22))
        font = label.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label.setFont(font)
        label.move(x, y)
        label.setStyleSheet("""color:#594E3F""")

    def linesEdit(self):
        #   name
        self.name = QLineEdit(self)
        self.config_linesEdit_text(self.name, 60, 120, 280, 40)
        #   gender
        self.gender = QLineEdit(self)
        self.config_linesEdit_text(self.gender, 60, 220, 280, 40)
        #   max
        self.max = QLineEdit(self)
        self.config_linesEdit_text(self.max, 60, 320, 280, 40)
        #   password

    def config_linesEdit_text(self, lineEdit: QLineEdit, x: int, y: int, width: int, height: int):
        lineEdit.setFont(QFont('Now', 20))
        lineEdit.setStyleSheet("""color:#868179 ;background-color: transparent; border-style: solid ;border-width: 2px;
                                    border-color: transparent; border-bottom-color: #868179""")
        font = lineEdit.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        lineEdit.setFont(font)
        lineEdit.resize(width, height)
        lineEdit.move(x, y)

    def accept_button(self):
        button = QPushButton('Aceptar', self)
        button.setFont(QFont('Now', 24))
        button.resize(200, 60)
        button.move(100, 440)
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.accept_clicked)

    def accept_clicked(self):
        name = self.name.text()
        genero = self.gender.text()
        max = self.max.text()
        pasa = False
        if max != '' or genero != '' or name != '':
            try:
                max_libros = int(genero) or int(name)
                self.name.setText('')
                self.gender.setText('')
            except Exception:
                if self.control.verificar_genero(genero) == False:
                    pasa = True
                else:
                    self.gender.setText('')

            if pasa == True:
                isAdmin = self.control.verificar_admin(self.usuario, 'password', 2)
                if isAdmin == True:
                    for admin in self.control.get_admins():
                        if admin.nombre == self.usuario:
                            self.control.new_estante(genero, int(max), admin)
                            self.win.addShelve_clicked(estante=self.name.text())
                            self.close()
        # ↑internamente tambien se debe agregar la libreria con los datos obtenidos

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def close_button(self):
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width - 49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.close)


# ______________________________________________________________________________________
class LendBookTo(QWidget):   # ventana prestar libro
    def __init__(self, bookname, win=None) -> None:
        super(LendBookTo, self).__init__()
        self.win = win
        self.bookname = bookname
        self.width = 400
        self.height = 300
        self.StartUp()
        self.control = ControlBookeeper()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint |
                           QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px;""")
        title = QLabel('Prestar libro a:', self)
        title.setFont(QFont('Now', 24))
        title.move(30, 10)
        title.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        font = title.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        title.setFont(font)
        ########################
        self.lendTo()
        self.accept_button()
        ########################
        self.close_button()    #
        self.center()          #
        self.show()            #
        ########################

    def lendTo(self):
        # name
        name = QLabel('Usuario', self)
        name.setFont(QFont('Now', 22))
        font = name.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        name.setFont(font)
        name.move(60, 85)
        name.setStyleSheet("""color:#594E3F""")
        # lineEdit
        self.name = QLineEdit(self)
        self.name.setFont(QFont('Now', 20))
        self.name.setStyleSheet("""color:#868179 ;background-color: transparent; border-style: solid ;border-width: 2px;
                                    border-color: transparent; border-bottom-color: #868179""")
        font = self.name.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.name.setFont(font)
        self.name.resize(280, 40)
        self.name.move(60, 120)

    def accept_button(self):
        button = QPushButton('Aceptar', self)
        button.setFont(QFont('Now', 24))
        button.resize(200, 60)
        button.move(100, 200)
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.accept_clicked)

    def accept_clicked(self):
        user=self.name.text()
        for cliente in self.control.get_clientes():
            if cliente.nombre == user:
                cliente_a_prestar = cliente
                break
        libros = list(set(self.control.get_libro_by_name(self.bookname)))
        for book in libros:
            if book.nombre == self.bookname:
                guardar_libro = book
                break
        self.win.ledTo(user =cliente_a_prestar, book=guardar_libro)
        self.close()
    # ↑internamente tambien se debe agregar el libro al usuario

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def close_button(self):
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width-49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.close)

# ______________________________________________________________________________________


class SeeBooksSomeone(QWidget):   # ventana ver libros de alguien
    def __init__(self, win=None) -> None:
        super(SeeBooksSomeone, self).__init__()
        self.win = win
        self.width = 400
        self.height = 300
        self.StartUp()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint |
                           QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px;""")
        title = QLabel('Ver libros de:', self)
        title.setFont(QFont('Now', 24))
        title.move(30, 10)
        title.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        font = title.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        title.setFont(font)
        ########################
        self.mostrarlibrosde()
        self.accept_button()
        ########################
        self.close_button()    #
        self.center()          #
        self.show()            #
        ########################

    def mostrarlibrosde(self):
        # name
        user = QLabel('Usuario', self)
        user.setFont(QFont('Now', 22))
        font = user.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        user.setFont(font)
        user.move(60, 85)
        user.setStyleSheet("""color:#594E3F""")
        # lineEdit
        self.user = QLineEdit(self)
        self.user.setFont(QFont('Now', 20))
        self.user.setStyleSheet("""color:#868179 ;background-color: transparent; border-style: solid ;border-width: 2px;
                                    border-color: transparent; border-bottom-color: #868179""")
        font = self.user.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.user.setFont(font)
        self.user.resize(280, 40)
        self.user.move(60, 120)

    def accept_button(self):
        button = QPushButton('Aceptar', self)
        button.setFont(QFont('Now', 24))
        button.resize(200, 60)
        button.move(100, 200)
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.accept_clicked)

    def accept_clicked(self):
        self.win.seemostrarlibrosde(user=self.user.text())
        self.close()
    # ↑internamente tambien se debe agregar el libro al usuario

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def close_button(self):
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width-49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.close)
# ______________________________________________________________________________________


class AñadirLibroAestante(QWidget):      # ventana eliminar libro de estante
    def __init__(self, shelve, bookBox, win) -> None:
        super(AñadirLibroAestante, self).__init__()
        self.win = win
        # esto es el nombre que se va a reeemplazar por el nombre del nuevo libro
        self.bookBox = bookBox
        self.shelve = shelve
        self.width = 400
        self.height = 300
        self.StartUp()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint |
                           QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px;""")
        title = QLabel('Agregar libro:', self)
        title.setFont(QFont('Now', 24))
        title.move(30, 10)
        title.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        font = title.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        title.setFont(font)
        ########################
        self.añadir()
        self.accept_button()
        ########################
        self.close_button()    #
        self.center()          #
        self.show()            #
        ########################

    def añadir(self):
        # name
        book = QLabel('Libro', self)
        book.setFont(QFont('Now', 22))
        font = book.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        book.setFont(font)
        book.move(60, 85)
        book.setStyleSheet("""color:#594E3F""")
        # lineEdit
        self.book = QLineEdit(self)
        self.book.setFont(QFont('Now', 20))
        self.book.setStyleSheet("""color:#868179 ;background-color: transparent; border-style: solid ;border-width: 2px;
                                    border-color: transparent; border-bottom-color: #868179""")
        font = self.book.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.book.setFont(font)
        self.book.resize(280, 40)
        self.book.move(60, 120)

    def accept_button(self):
        button = QPushButton('Aceptar', self)
        button.setFont(QFont('Now', 24))
        button.resize(200, 60)
        button.move(100, 200)
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.accept_clicked)

    def accept_clicked(self):
        self.win.AñadirLibro(book=self.book.text(),
                         bookBox=self.bookBox, shelve=self.shelve)
        self.close()
    # ↑internamente tambien se debe agregar el libro al usuario

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def close_button(self):
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width-49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.close)
# ______________________________________________________________________________________


class Delete(QWidget):      # ventana eliminar estante
    def __init__(self, shelve, win=None) -> None:
        super(Delete, self).__init__()
        self.win = win
        self.shelve = shelve
        self.width = 400
        self.height = 300
        self.StartUp()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint |
                           QtCore.Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px;""")
        title = QLabel('Eliminar', self)
        title.setFont(QFont('Now', 24))
        title.move(30, 10)
        title.setStyleSheet(
            """color:#594E3F ;background-color:#FFF9F2 ;border-style: solid ;border-radius: 30px""")
        font = title.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        title.setFont(font)
        ########################
        self.eliminar_estante()
        self.yes_button()
        self.no_button()
        ########################
        self.close_button()    #
        self.center()          #
        self.show()            #
        ########################
    def eliminar_estante(self):
        # name
        book = QLabel(' ¿Seguro que quieres\neliminar este Estante?', self)
        book.setFont(QFont('Now', 22))
        font = book.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        book.setFont(font)
        book.move(40, 85)
        book.setStyleSheet("""color:#594E3F""")

    def yes_button(self):
        button = QPushButton('si', self)
        button.setFont(QFont('Now', 24))
        button.resize(100, 60)
        button.move(50, 200)
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.yes_clicked)

    def no_button(self):
        button = QPushButton('no', self)
        button.setFont(QFont('Now', 24))
        button.resize(100, 60)
        button.move(self.width-155, 200)
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-style: solid ;border-radius: 30px""")
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.close)

    def yes_clicked(self):
        self.win.deleteShelve(shelve=self.shelve)
        self.close()
    # ↑internamente tambien se debe agregar el libro al usuario

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def close_button(self):
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width-49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.close)
# ______________________________________________________________________________________


class ProfileWindow(QMainWindow):     # ventana perfil de usuario
    def __init__(self, user, parent=None) -> None:
        super().__init__(parent)
        self.control = ControlBookeeper()
        self.width = 1630
        self.height = 980
        self.userName = user
        self.image = QPixmap("src/views/images/usuario.png")
        self.image = self.image.scaled(self.image.size(
        ), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.StartUp()

    def StartUp(self):
        self.setWindowTitle('BooKeeper')
        self.setFixedSize(self.width, self.height)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # background
        bg = QLabel(self)
        bg.resize(self.width, self.height)
        bg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px;""")
        ########################
        self.back_button()
        self.UserImage()
        self.MainLine()
        self.otherLines()
        self.saveChanges_button()
        ########################
        self.close_button()    #
        self.center()          #
        self.show()            #
        ########################

    def UserImage(self):  # cambiar a label circular solo si se implementa lo de cambiar foto
        image = QLabel(self)
        image.resize(350, 350)
        image.move(40, 40)
        image.setScaledContents(True)
        image.setPixmap(self.image)
        image.setStyleSheet("""background-color:none""")

    def MainLine(self):
        self.user_line = QLineEdit(self.userName, self)
        self.user_line.resize(1100, 100)
        self.user_line.move(400, 200)
        self.user_line.setReadOnly(True)
        self.user_line.setFont(QFont('Now', 50))
        self.user_line.setStyleSheet("""color:#594E3F ;background-color: transparent; border-style: solid ;border-width: 4px;
                                    border-color: transparent; border-bottom-color: #868179""")
        font = self.user_line.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.user_line.setFont(font)
        widget = QWidget(self)
        widget.resize(300, 100)
        widget.move(1200, 195)
        widget.setStyleSheet("""background-color:#FFF9F2""")
        # button
        changeUser = QPushButton('Cambiar', self)
        changeUser.setFont(QFont('Now', 25))
        changeUser.resize(155, 50)
        changeUser.move(1270, 230)
        changeUser.setStyleSheet(
            """backgroun-color: none; color:#868179; border-style: solid""")
        font = changeUser.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        changeUser.setFont(font)
        changeUser.setFont(font)
        changeUser.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        changeUser.clicked.connect(self.changeUser_clicked)

    def changeUser_clicked(self):
        self.user_line.setReadOnly(False)
        self.user_line.setFocus()

    def otherLines(self):
        dic = {'1': 'Nombre Completo',
               '2': f'{self.control.get_cliente(id = 3, name = self.userName).contrasena}', '3': 'Correo electrónico'}
        widget = QWidget(self)
        widget.resize(1200, 400)
        widget.move(70, 350)
        widget.setStyleSheet("""background-color:none""")
        self.grid = QGridLayout(widget)
        for i in range(3):
            line = QLineEdit(dic[str(i + 1)], self)
            line.resize(100, 60)
            line.setReadOnly(True)
            line.setFont(QFont('Now', 30))
            if i == 1:
                line.setEchoMode(QLineEdit.EchoMode.Password)
            line.setStyleSheet(
                """color:#594E3F ;background-color: transparent; border-style: solid""")
            font = line.font()
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            line.setFont(font)
            #
            button = QPushButton('Cambiar', self)
            button.setFont(QFont('Now', 25))
            button.setStyleSheet(
                """color:#868179 ;background-color: none; border-style: solid""")
            font = button.font()
            font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
            button.setFont(font)
            button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            button.clicked.connect(self.change_clicked)
            ######
            self.grid.addWidget(line, i, 0, 1, 1)
            self.grid.addWidget(button, i, 1, 1, 1)

    def change_clicked(self):
        button = self.sender()
        position = self.grid.indexOf(button)
        row = position // 2
        column = position % 2
        item = self.grid.itemAtPosition(row, column - 1).widget()
        item.setStyleSheet("""color:#594E3F ;background-color: transparent; border-style: solid ;border-width: 2px;
                                    border-color: transparent; border-bottom-color: #868179""")
        item.setReadOnly(False)
        item.setFocus()

    def saveChanges_button(self):
        button = QPushButton('Guardar cambios', self)
        button.resize(300, 60)
        button.move(665, 800)
        button.setFont(QFont('Now', 24))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F ;border-radius:30px; """)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.saveChanges_clicked)

    def saveChanges_clicked(self):
        self.user_line.setReadOnly(True)
        user = self.user_line.text()
        #
        line1 = self.grid.itemAtPosition(0, 0).widget()
        line1.setReadOnly(True)
        line1.setStyleSheet(
            """color:#594E3F ;background-color: transparent; border-style: solid""")
        name = line1.text()
        #
        line2 = self.grid.itemAtPosition(1, 0).widget()
        line2.setReadOnly(True)
        line2.setStyleSheet(
            """color:#594E3F ;background-color: transparent; border-style: solid""")
        password = line2.text()
        #
        line3 = self.grid.itemAtPosition(2, 0).widget()
        line3.setReadOnly(True)
        line3.setStyleSheet(
            """color:#594E3F ;background-color: transparent; border-style: solid""")
        adress = line3.text()
        #####
        if (user != self.parent().userName and user != 'Nombre de usuario' and user != ''):
            # cambiar en la base de datos
            self.control.cambiar_info(nombre=self.parent().userName, password=password, segundo=user)
            self.parent().userName = user
            self.parent().Labelname.setText(user)

    # se deben cambiar internamente los datos y cambiar el nombre de usuario en la ventana principal

    def back_button(self):
        button = QPushButton('«', self)
        button.resize(50, 50)
        button.move(0, 0)
        button.setFont(QFont('Now', 30))
        button.setStyleSheet(
            """color: #594E3F; background-color:none; border-top-left-radius:20px; border-bottom-right-radius:20px""")
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(self.back_clicked)

    def back_clicked(self):
        self.hide()
        self.parent().show()
        self.deleteLater()

    def close_button(self):
        closeAction = QApplication.instance().quit
        button = QPushButton("x", self)
        button.resize(50, 50)
        button.move(self.width - 49, 0)
        button.setFont(QFont('Now', 20))
        font = button.font()
        font.setBold(True)
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setStyleSheet(
            """color: #FFF9F2; background-color:#594E3F; border-bottom-left-radius:20px; border-top-right-radius:20px;
            change-cursor: cursor('PointingHand')""")
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.clicked.connect(closeAction)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


  # ________________________________________________________________________________________________________


def Main():
    app = QApplication(sys.argv)
    LogWin = LoginWindow()
    sys.exit(app.exec())