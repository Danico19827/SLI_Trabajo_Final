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
        #Comienza Leyendo la Nota 1
        self.leerNota(self.notas.comboBox.currentText())
    
        #(Botones)
        self.notas.btn_guardar.clicked.connect(self.GuardarNota)
        self.notas.btn_cancelar.clicked.connect(self.Cancelar)
        self.notas.btn_copiar.clicked.connect(self.Copiar)
        self.notas.btn_cortar.clicked.connect(self.Cortar)
        self.notas.btn_pegar.clicked.connect(self.Pegar)
        self.notas.btn_borrar.clicked.connect(self.Borrar)
        self.notas.comboBox.currentIndexChanged.connect(lambda index: self.leerNota(self.notas.comboBox.itemText(index)))

        #(Funcionalidad)
    def Copiar(self):
        cursor = self.notas.pte_contenido.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def Cortar(self):
        cursor = self.notas.pte_contenido.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            cursor.removeSelectedText()
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def Pegar(self):
        clipboard = QApplication.clipboard()
        text_to_paste = clipboard.text()
        if text_to_paste:
            cursor = self.notas.pte_contenido.textCursor()
            cursor.insertText(text_to_paste)

    def Borrar(self):
        self.notas.pte_contenido.clear()

    def GuardarNota(self):
        nota = self.notas.comboBox.currentText()
        nota = str(nota).lower().replace(" ", "")
        contenido = self.notas.pte_contenido.toPlainText()
        try:
            with open('notas.json', 'r') as archivo:
                datos = json.load(archivo)
            datos[nota] = contenido

            with open('notas.json', 'w') as archivo:
                json.dump(datos, archivo, indent=2)
        except FileNotFoundError as e:
            print(e)

        

    def leerNota(self, nota):
        nota = str(nota).lower().replace(" ", "")
        try:
            with open('notas.json', 'r') as archivo:
                datos = json.load(archivo)
                contenido = datos[nota]
                self.notas.pte_contenido.setPlainText(str(contenido))
        except FileNotFoundError as e:
            print(e)

    def Cancelar(self):
        self.notas.pte_contenido.clear()


