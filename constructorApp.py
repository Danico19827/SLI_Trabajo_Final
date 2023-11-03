from ventanas.main import Main
from ventanas.finanzas import Finanza
from PyQt6.QtWidgets import QApplication



class Lanzador():
    def __init__(self) -> None:
        self.app = QApplication([])
        self.main = Main()
        self.app.exec()