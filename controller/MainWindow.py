from PyQt6 import uic

from controller.FinanzasWindow import Finanza
from controller.NotasWindow import Notas
from controller.TiempoWindow import Tiempo
from controller.HorariosWindow import Horario

class Main():
    def __init__(self) -> None:
        self.main = uic.loadUi("../SLI_Trabajo_Final/resources/templates/main.ui")
        self.main.showMaximized()
        self.acceder()

    def acceder(self):
        self.main.btnFinanzas.clicked.connect(self.abrirFinanzas)
        self.main.btnNotas.clicked.connect(self.abrirNotas)
        self.main.btnTiempo.clicked.connect(self.abrirTiempo)
        self.main.btnHorarios.clicked.connect(self.abrirHorario)
        
    
    def abrirFinanzas(self):
        self.finanzas = Finanza()

    def abrirNotas(self):
        self.notas = Notas()

    def abrirTiempo(self):
        self.tiempo = Tiempo()

    def abrirHorario(self):
        self.horarios = Horario()