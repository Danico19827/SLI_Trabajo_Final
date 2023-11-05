from PyQt6.QtWidgets import QApplication
from controller.MainController import Main

class Lanzador():
    def __init__(self) -> None:
        self.app = QApplication([])
        self.main = Main()
        self.app.exec()