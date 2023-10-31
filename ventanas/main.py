from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

class Main():
    def __init__(self) -> None:
        self.main = uic.loadUi("../SLI_Trabajo_Final/ventanas/main.ui")
        self.main.showMaximized()