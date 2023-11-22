from PyQt6 import uic

from controller.FinanzasWindow import Finanza
from controller.NotasWindow import Notas
from controller.RecordatoriosWindow import Recordatorios
from controller.TiempoWindow import Tiempo

class Main():
    def __init__(self) -> None:
        self.main = uic.loadUi("../SLI_Trabajo_Final/resources/templates/main.ui")
        self.main.showMaximized()
        self.accederFinanzas()
        self.accederNotas()
        self.accederRecordatorios()
        #self.accederHorarios()
        self.accederTiempo()

    def accederFinanzas(self):
        self.main.btnFinanzas.clicked.connect(self.abrirFinanzas)
    
    def abrirFinanzas(self):
        self.finanzas = Finanza()

    def accederRecordatorios(self):
        self.main.btnRecordatorios.clicked.connect(self.abrirRecordatorios)
  
    def abrirRecordatorios(self):
        self.recordatorios = Recordatorios()

    def accederNotas(self):
        self.main.btnNotas.clicked.connect(self.abrirNotas)

    def abrirNotas(self):
        self.notas = Notas()

    def accederTiempo(self):
        self.main.btnTiempo.clicked.connect(self.abrirTiempo)

    def abrirTiempo(self):
        self.notas = Tiempo()