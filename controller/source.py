# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowChildhngAwi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 636)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frameSuperior = QFrame(self.centralwidget)
        self.frameSuperior.setObjectName(u"frameSuperior")
        self.frameSuperior.setMinimumSize(QSize(0, 40))
        self.frameSuperior.setMaximumSize(QSize(16777215, 40))
        self.frameSuperior.setStyleSheet(u"QFrame{\n"
"	background-color: #242526;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #E4E6EB;\n"
"	border-radius: 5px;\n"
"}")
        self.frameSuperior.setFrameShape(QFrame.StyledPanel)
        self.frameSuperior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameSuperior)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(597, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonMinimize = QPushButton(self.frameSuperior)
        self.pushButtonMinimize.setObjectName(u"pushButtonMinimize")
        self.pushButtonMinimize.setMaximumSize(QSize(16777215, 32))
        self.pushButtonMinimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../static/images/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMinimize.setIcon(icon)
        self.pushButtonMinimize.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.pushButtonMinimize)

        self.pushButtonMaximize = QPushButton(self.frameSuperior)
        self.pushButtonMaximize.setObjectName(u"pushButtonMaximize")
        self.pushButtonMaximize.setMaximumSize(QSize(16777215, 32))
        self.pushButtonMaximize.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../static/images/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonMaximize.setIcon(icon1)
        self.pushButtonMaximize.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.pushButtonMaximize)

        self.pushButtonRestore = QPushButton(self.frameSuperior)
        self.pushButtonRestore.setObjectName(u"pushButtonRestore")
        self.pushButtonRestore.setMaximumSize(QSize(16777215, 32))
        self.pushButtonRestore.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../static/images/restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRestore.setIcon(icon2)
        self.pushButtonRestore.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.pushButtonRestore)

        self.pushButtonClose = QPushButton(self.frameSuperior)
        self.pushButtonClose.setObjectName(u"pushButtonClose")
        self.pushButtonClose.setMaximumSize(QSize(16777215, 32))
        self.pushButtonClose.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../static/images/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonClose.setIcon(icon3)
        self.pushButtonClose.setIconSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.pushButtonClose)


        self.verticalLayout.addWidget(self.frameSuperior)

        self.frameInferior = QFrame(self.centralwidget)
        self.frameInferior.setObjectName(u"frameInferior")
        self.frameInferior.setFrameShape(QFrame.StyledPanel)
        self.frameInferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameInferior)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frameMenu = QFrame(self.frameInferior)
        self.frameMenu.setObjectName(u"frameMenu")
        self.frameMenu.setMinimumSize(QSize(200, 450))
        self.frameMenu.setMaximumSize(QSize(200, 16777215))
        self.frameMenu.setStyleSheet(u"QFrame{\n"
"	background-color: #242526;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"  	background: #1683c6;\n"
"  	color: #fff;\n"
"  	padding: 10px;\n"
"  	font-size: 16px;\n"
"  	border-radius: 5px;\n"
"  	position: relative;\n"
"  	box-sizing: border-box;\n"
"  	transition: all 500ms ease;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: #1683c6;\n"
"  	border: #ff7a59 solid 1px;\n"
"  	background:#fff;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frameMenu.setFrameShape(QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QFrame.Raised)
        self.btnInicio = QPushButton(self.frameMenu)
        self.btnInicio.setObjectName(u"btnInicio")
        self.btnInicio.setGeometry(QRect(10, 40, 181, 41))
        self.btnInicio.setStyleSheet(u"")
        self.label = QLabel(self.frameMenu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 490, 181, 51))
        self.btnFinanzas = QPushButton(self.frameMenu)
        self.btnFinanzas.setObjectName(u"btnFinanzas")
        self.btnFinanzas.setGeometry(QRect(10, 100, 181, 41))
        self.btnFinanzas.setStyleSheet(u"")
        self.btnNotas = QPushButton(self.frameMenu)
        self.btnNotas.setObjectName(u"btnNotas")
        self.btnNotas.setGeometry(QRect(10, 160, 181, 41))
        self.btnNotas.setStyleSheet(u"")
        self.btnTiempo = QPushButton(self.frameMenu)
        self.btnTiempo.setObjectName(u"btnTiempo")
        self.btnTiempo.setGeometry(QRect(10, 220, 181, 41))
        self.btnTiempo.setStyleSheet(u"")
        self.btnHorario = QPushButton(self.frameMenu)
        self.btnHorario.setObjectName(u"btnHorario")
        self.btnHorario.setGeometry(QRect(10, 280, 181, 41))
        self.btnHorario.setStyleSheet(u"")
        self.btnRecordatorios = QPushButton(self.frameMenu)
        self.btnRecordatorios.setObjectName(u"btnRecordatorios")
        self.btnRecordatorios.setGeometry(QRect(10, 340, 181, 41))
        self.btnRecordatorios.setStyleSheet(u"")
        self.btnCreditos = QPushButton(self.frameMenu)
        self.btnCreditos.setObjectName(u"btnCreditos")
        self.btnCreditos.setGeometry(QRect(10, 400, 181, 41))
        self.btnCreditos.setStyleSheet(u"")
        self.label_2 = QLabel(self.frameMenu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 91, 21))

        self.horizontalLayout_2.addWidget(self.frameMenu)

        self.frameContainer = QFrame(self.frameInferior)
        self.frameContainer.setObjectName(u"frameContainer")
        self.frameContainer.setFrameShape(QFrame.StyledPanel)
        self.frameContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frameContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frameContainer)


        self.verticalLayout.addWidget(self.frameInferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonMinimize.setText("")
        self.pushButtonMaximize.setText("")
        self.pushButtonRestore.setText("")
        self.pushButtonClose.setText("")
        self.btnInicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Seminario de Lenguajes I - 2023", None))
        self.btnFinanzas.setText(QCoreApplication.translate("MainWindow", u"Finanzas", None))
        self.btnNotas.setText(QCoreApplication.translate("MainWindow", u"Notas", None))
        self.btnTiempo.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None))
        self.btnHorario.setText(QCoreApplication.translate("MainWindow", u"Horario", None))
        self.btnRecordatorios.setText(QCoreApplication.translate("MainWindow", u"Recordatorios", None))
        self.btnCreditos.setText(QCoreApplication.translate("MainWindow", u"Creditos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bienvenid@", None))
    # retranslateUi

