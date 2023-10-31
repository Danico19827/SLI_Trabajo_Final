from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

class Finanzas():
    def __init__(self) -> None:
        self.finanzas = uic.loadUi("../SLI_Trabajo_Final/ventanas/finanzas.ui")
        self.acceder()
        self.finanzas.show()
