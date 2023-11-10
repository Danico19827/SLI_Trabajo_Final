import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6 import uic

#from PySide6 import QtCore
#from PySide6.QtCore import QPropertyAnimation
#from PySide6 import QtCore, QtGui, QtWidgets

#from controller.FinanzasWindow import Finanza
#from controller.NotasWindow import Notas
#from controller.RecordatoriosWindow import Recordatorios

class MainWindowChild(QMainWindow):

    def __init__(self):
        self.main = uic.loadUi("../SLI_Trabajo_Final/resources/templates/mainWindowChild.ui")       

        self.main.showMaximized()

        self.main.stackedWidget.setCurrentWidget(self.main.page_1)

        self.main.btnInicio.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_1))
        self.main.btnFinanzas.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_2))
        self.main.btnNotas.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_3))
        self.main.btnTiempo.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_4))
        self.main.btnHorario.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_5))
        self.main.btnRecordatorios.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_6))
        self.main.btnCreditos.clicked.connect(lambda: self.main.stackedWidget.setCurrentWidget(self.main.page_7))
        #self.main.stackedWidget.currentChanged.connect(self.adjustHeight)
        #self.adjustHeight()
        #c:\Program Files\Python311\python3.dll
        #eliminar barra de control superior
        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setWindowOpacity(1)


   