from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

from controller.FinanzasController import Finanza

class Main():
    def __init__(self) -> None:
        self.main = uic.loadUi("../SLI_Trabajo_Final/resources/templates/main.ui")
        self.main.showMaximized()
        self.accederFinanzas()


    def accederFinanzas(self):
        self.main.btnFinanzas.clicked.connect(self.abrirFinanzas)

    
    def abrirFinanzas(self):
        self.finanzas = Finanza()
        self.main.close()