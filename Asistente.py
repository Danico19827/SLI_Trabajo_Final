from PyQt6.QtWidgets import QApplication
from controller.MainWindow import Main
from controller.mainWindowChild import MainWindowChild

class Lanzador():
    def __init__(self) -> None:
        self.app = QApplication([])
        self.main = Main()
        self.app.exec()