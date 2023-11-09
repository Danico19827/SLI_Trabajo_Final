from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class Notas():
    def __init__(self) -> None:
        self.notas = uic.loadUi("../SLI_Trabajo_Final/resources/templates/notas.ui")
        self.notas.showMaximized()