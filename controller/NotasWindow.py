from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class Notas():
    def __init__(self) -> None:
        self.notas = uic.loadUi("../SLI_Trabajo_Final/resources/templates/notas.ui")
        self.notas.showMaximized()
        self.notas.btn_guardar.clicked.connect(self.clickedHandler)
        self.notas.btn_cancelar.clicked.connect(self.clickedHandler)
        #self.btn_archivadas.clicked.connect(self.clickedHandler)
        #self.btn_creadas.clicked.connect(self.clickedHandler)
        
        
    def clickedHandler(self):
        print("click")
        contenido_nota = self.notas.ptxt_contenidoNota.toPlainText()
        titulo_nota = self.notas.txt_tituloNota.text()

        
        if contenido_nota.strip() != "" and titulo_nota.strip() != "":
            self.notas.wdglist_notasCreadas.addItem((titulo_nota) +  (contenido_nota))