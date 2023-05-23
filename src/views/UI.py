from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QRect, pyqtSignal, QObject, QEvent, QTimer, QTime
from PyQt6.QtGui import QFont, QPixmap, QCursor
from PyQt6.QtWidgets import (QApplication, QToolTip, QWidget, QMainWindow, QPushButton, QTextEdit, QLineEdit, QCheckBox, QLabel,
                             QScrollArea, QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, QSpacerItem)
import sys
from src.Controllers.control_bookeeper import ControlBookeeper

class CustomEdit(QLineEdit):
    def mousePressEvent(self, event):
        text = self.text()
        if event.button() == Qt.MouseButton.LeftButton and text == 'Buscar Libro':
            self.setText('')


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

    def labels(self):
        #   title
        title_label = QLabel(' BooKeeper', self)
        title_label.setFont(QFont('Nickainley', 80,))
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
        label.move(self.width-98, 0)
        label.setStyleSheet(
            """background-color:#6B6051 ;border-bottom-left-radius: 20px""")
        button = QPushButton('-', self)
        button.resize(48, 50)
        button.move(self.width-98, 0)
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
            self.UserWin = UserWindow()
            self.UserWin.show()
            timer = QTimer(self)
            timer.start(5)
            timer.timeout.connect(self.close)
        else:
            print('cliente')
            self.UserWin = UserWindow()
            self.UserWin.show()
            timer = QTimer(self)
            timer.start(5)
            timer.timeout.connect(self.close)

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
        self.confirm_line.textChanged.connect(self.confirmLineTyping)
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

    def minimize_button(self):
        label = QLabel('', self)
        label.resize(70, 50)
        label.move(self.width-98, 0)
        label.setStyleSheet(
            """background-color:#6B6051 ;border-bottom-left-radius: 20px""")
        button = QPushButton('-', self)
        button.resize(48, 50)
        button.move(self.width-98, 0)
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

    def confirmLineTyping(self):  # arreglar(para validar igualdad de password)
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


# _____________________________________________________________________________________
class UserWindow(QWidget):
    def __init__(self) -> None:
        super(UserWindow, self).__init__()
        self.width = 1630
        self.height = 980
        self.searchMode = 'Nombre'  # para saber si se buscar por nombre de libro, autor, genero
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
        lg.resize(self.width-1205, self.height)
        lg.setStyleSheet("""background-color:#FFF9F2; border-radius: 20px""")
        ######################
        self.searchBar()
        self.logOut_button()
        self.shelves_box()
        self.addShelve_button()
        self.tagButtons()
        ########################
        self.minimize_button()
        self.close_button()    #
        self.center()          #
        self.show()            #
        ########################

    def shelves_box(self):
        self.shelve_bx = QScrollArea(self)
        self.shelve_bx.move(20, 150)
        self.shelve_bx.resize(1175, 780)  # -1186,780
        self.shelve_bx.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.shelve_bx.setWidgetResizable(True)
        self.shelve_bx.setStyleSheet(
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
        # al final revisar si el add spaceritem servia
        self.shelve_bx.setWidget(self.shelveWidget)

    def config_BookBox(self, GBox, libro):
        GBox.setMaximumSize(200, 210)
        GBox.setStyleSheet(
            """background-color: #594E3F ;border-radius: 20px """)
        layV = QVBoxLayout(GBox)
        layV.addSpacing(20)
        # item
        space = QSpacerItem(20, 30)
        # 4
        label_4 = QLabel('Calificación')
        label_4.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:20px Now""")
        font = label_4.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label_4.setFont(font)
        # 3
        label_3 = QLabel('Género')
        label_3.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:20px Now""")
        font = label_3.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label_3.setFont(font)
        # 2
        label_2 = QLabel('Autor')
        label_2.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:20px Now""")
        font = label_2.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        label_2.setFont(font)
        # 1
        label_1 = QLabel(libro)
        label_1.setStyleSheet(
            """background-color: none;color: #FFF9F2 ;font:28px Now""")
        font = label_1.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        text_length = label_1.fontMetrics().horizontalAdvance(libro)
        print(text_length)
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

    def logOut_button(self):  # al abrir la app debe mostrar login
        button = QPushButton('Cerrar Sesión', self)
        button.setFont(QFont('Now', 24))
        button.resize(245, 60)
        button.move(1295, 800)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet(
            """color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px""")
        button.clicked.connect(self.logOut_clicked)

    def logOut_clicked(self):
        self.logwin = LoginWindow()
        self.logwin.show()
        timer = QTimer(self)
        timer.start(5)
        timer.timeout.connect(self.close)

    def addShelve_button(self):
        button = QPushButton('Agregar Estante', self)
        button.setFont(QFont('Now', 24))
        button.resize(295, 60)
        button.move(1185+85, 600)
        font = button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        button.setFont(font)
        button.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        button.setStyleSheet("""color:#FFF9F2 ;background-color:#594E3F ;border-radius: 30px; padding-left: 14px
                            ;padding-right: 12px""")
        button.clicked.connect(self.addShelve_clicked)

    def addShelve_clicked(self):
        count = self.shelveLayout.count()-1
        shelveGroup = QGroupBox('', self.shelveWidget)
        shelveGroup.setStyleSheet(
            """background-color: none;border-style:solid; """)
        self.shelveLayout.insertWidget(count, shelveGroup)
        ################################
        grid = QGridLayout(shelveGroup)
        # label
        shelve_label = QLabel('Estante ' + str(count+1), shelveGroup)
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
        # Addbook
        addBook_button = QPushButton('Agregar libro')
        addBook_button.setStyleSheet(
            """color: #FFF9F2 ;background-color:none ;font: 24px Now ;text-align: center""")
        addBook_button.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        font = addBook_button.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        addBook_button.setFont(font)
        # delete
        delete = QPushButton('X', shelveGroup)
        delete.setStyleSheet(
            """color: #FFF9F2 ;background-color:none ;font: 24px Now ;text-align: center""")
        delete.setCursor(
            QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        font = delete.font()
        font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        font.setBold(True)
        delete.setFont(font)
        delete.clicked.connect(self.deleteShelve)
        #
        book1 = QGroupBox('')
        self.config_BookBox(book1, 'caperucita')
        book2 = QGroupBox('')
        self.config_BookBox(book2, 'los 3 cerditos')
        book3 = QGroupBox('')
        self.config_BookBox(book3, 'batman y superman')
        book4 = QGroupBox('')
        self.config_BookBox(book4, 'Libro 4')
        #############################################
        grid.addWidget(shelve_label,     0, 0, 1, 15)
        grid.addWidget(seeMore,    0, 0, 1, 15,
                       Qt.AlignmentFlag.AlignRight)
        grid.addWidget(book1,            1, 0, 1, 3)
        grid.addWidget(book2,            1, 4, 1, 3)
        grid.addWidget(book3,            1, 8, 1, 3)
        grid.addWidget(book4,            1, 12, 1, 3)
        grid.addWidget(shelveGroup,      1, 14, 1, 4)
        grid.addWidget(addBook_button,   2, 0, 1, 15,
                       Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(delete,           2, 14, 1, 1,
                       Qt.AlignmentFlag.AlignRight)

    def deleteShelve(self):
        button = self.sender()
        padre = self.sender().parent()
        padre.deleteLater()

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
            """background-color:none ;border-style:none; border-radius: 20px ;image: url("PooProyect/images/len.png")""")
        button.resize(50, 50)
        button.move(995, 25)
        button.move(995, 25)

    def search(self):#must be valided
        if self.searchMode == 'Libro':
            pass
        elif self.searchMode == 'Género':
            pass
        else:
            pass

    def mousePressEvent(self, event):
        text = self.bar.text()
        if event.button() == Qt.MouseButton.LeftButton and event.pos() not in self.bar.geometry():
            self.bar.clearFocus()
            if text == '':
                self.bar.setText('Buscar Libro')

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def minimize_button(self):
        label = QLabel('', self)
        label.resize(70, 50)
        label.move(self.width-98, 0)
        label.setStyleSheet(
            """background-color:#6B6051 ;border-bottom-left-radius: 20px""")
        button = QPushButton('-', self)
        button.resize(48, 50)
        button.move(self.width-98, 0)
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
        button.move(self.width-49, 0)
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


def Main():  # ________________________________________________________________________________________________________
    app = QApplication(sys.argv)
    LogWin = LoginWindow()
    app.exec()