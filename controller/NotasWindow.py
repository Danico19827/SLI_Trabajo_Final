'''
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
'''
from PyQt6 import uic
import json
from PyQt6.QtWidgets import QMessageBox, QApplication ,QApplication,QFileDialog
import typing
from PyQt6 import QtCore
import sys

class Notas():
    def __init__(self) -> None:
        self.notas = uic.loadUi("../SLI_Trabajo_Final/resources/templates/notas.ui")
        self.notas.showMaximized()
    
        #(Botones)
        self.notas.btn_guardar.clicked.connect(self.Guardar)
        self.notas.btn_cancelar.clicked.connect(self.Cancelar)
        self.notas.btn_copiar.clicked.connect(self.HeCopiar)
        self.notas.btn_cortar.clicked.connect(self.HeCortar)
        self.notas.btn_pegar.clicked.connect(self.HePegar)
        self.notas.btn_borrar.clicked.connect(self.HeBorrar)

        #(Funcionalidad)
    def HeCopiar (self):
        cursor = self.notas.pte_contenido.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def HeCortar (self):
        cursor = self.notas.pte_contenido.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            cursor.removeSelectedText()
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def HePegar (self):
        clipboard = QApplication.clipboard()
        text_to_paste = clipboard.text()
        if text_to_paste:
            cursor = self.notas.pte_contenido.textCursor()
            cursor.insertText(text_to_paste)

    def HeBorrar (self):
        self.notas.pte_contenido.clear()

    def Guardar (self):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Mensaje")
        mensaje.setText("Archivo Guardado")
        mensaje.exec()

        contenido_nota=self.notas.pte_contenido.toPlainText()
        nombre, _ = QFileDialog.getSaveFileName(self, 'Guardar JSON', '', 'Archivos JSON (*.json);;Todos los Archivos (*)')

        if nombre:
            with open(nombre, 'w') as guardado:
                json.dump({'Contenido Nota': contenido_nota}, guardado, indent=2)

    '''
        if contenido_nota.strip() != "":
            nota1 = self.notas.pte_contenido.toPlainText()
            with open("n1.txt", "w") as n1:
                n1.write(str(nota1))
    '''

            
    def leerTxt(self):
        with open("n1.txt", "r") as archivo:
            texto = archivo.read()
            self.finanzas.autoEvM.setText(str(texto))

    def Cancelar (self):
        self.notas.pte_contenido.clear()


