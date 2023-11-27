from PyQt6 import uic
import json
from PyQt6.QtWidgets import QMessageBox, QApplication ,QApplication,QFileDialog
import typing
from PyQt6 import QtCore
import sys

class Notas():
    def __init__(self) -> None:
        self.notas = uic.loadUi("view/notas.ui")
        self.notas.showMaximized()
        #Comienza Leyendo la Nota 1
        self.leerNota(self.notas.comboBox.currentText())
    
        #(Botones)
        self.notas.btn_guardar.clicked.connect(self.guardarNota)
        self.notas.btn_cancelar.clicked.connect(self.cancelar)
        self.notas.btn_copiar.clicked.connect(self.copiar)
        self.notas.btn_cortar.clicked.connect(self.cortar)
        self.notas.btn_pegar.clicked.connect(self.pegar)
        self.notas.btn_borrar.clicked.connect(self.borrar)
        self.notas.comboBox.currentIndexChanged.connect(lambda index: self.leerNota(self.notas.comboBox.itemText(index)))

    #(Funcionalidad)
    def copiar(self):
        cursor = self.notas.pte_contenido.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def cortar(self):
        cursor = self.notas.pte_contenido.textCursor()
        selected_text = cursor.selectedText()
        if selected_text:
            cursor.removeSelectedText()
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_text)

    def pegar(self):
        clipboard = QApplication.clipboard()
        text_to_paste = clipboard.text()
        if text_to_paste:
            cursor = self.notas.pte_contenido.textCursor()
            cursor.insertText(text_to_paste)

    def borrar(self):
        self.notas.pte_contenido.clear()

    # Guarda una nota en el JSON notas.json
    def guardarNota(self):
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
            self.crearJson()

    def cancelar(self):
        self.notas.pte_contenido.clear()

    def crearJson(self):
        datos = {
            "nota1": "",
            "nota2": "",
            "nota3": "",
            "nota4": "",
            "nota5": "",
            "nota6": "",
            "nota7": "",
            "nota8": "",
            "nota9": "",
            "nota10": ""
        }
        with open('notas.json', 'w') as archivo:
            json.dump(datos, archivo, indent=2)


