from PyQt6 import uic

from controller.FinanzasWindow import Finanza
from controller.NotasWindow import Notas
#from controller.RecordatoriosWindow import Recordatorios

class Main():
    def __init__(self) -> None:
        self.main = uic.loadUi("../SLI_Trabajo_Final/resources/templates/main.ui")
        self.main.showMaximized()
        self.accederFinanzas()
        self.accederNotas()
        self.accederRecordatorios()
        #self.accederHorarios()

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