from PyQt6 import uic
from PyQt6.QtWidgets import QTableWidgetItem
import json

class Horario():
    def __init__(self) -> None:
        self.horarios = uic.loadUi("../SLI_Trabajo_Final/resources/templates/horarios.ui")
        self.horarios.showMaximized()
        self.cargarDatos()
        self.iniciar()

    #Inicializa los Botones
    def iniciar(self):
        self.horarios.btnGuardarH.clicked.connect(self.guardarDatos)
        self.horarios.btnReiniciarH.clicked.connect(self.reiniciarDatos)

    #Detecta el tipo de Finanzas y obtiene los datos del archivo JSON
    def cargarDatos(self):
        try:
            with open('horario.json', 'r') as archivo:
                datos = json.load(archivo)
                self.llenarTablaDesdeJSON(datos)
        except FileNotFoundError as e:
            print(e)

    #Llena las tablas con los datos obtenidos del archivo JSON
    def llenarTablaDesdeJSON(self, datos):
        tabla = self.horarios.tablaHorario
        for columna, filas in datos.items():
            for fila, valor in filas.items():
                col = int(columna.replace("columna", ""))
                fil = int(fila.replace("fila", ""))
                tabla.setItem(fil, col, QTableWidgetItem(str(valor)))

    #Guarda los datos actuales de las tablas en el archivo JSON
    def guardarDatos(self):
        tabla = self.horarios.tablaHorario
        numFilas = tabla.rowCount()
        numColumnas = tabla.columnCount()
        datos = {}

        for columna in range(numColumnas):
            datos[f"columna{columna}"] = {}
            for fila in range(numFilas):
                item = tabla.item(fila, columna)
                valor = item.text()
                datos[f"columna{columna}"][f"fila{fila}"] = valor

        with open('horario.json', 'w') as archivo:
            json.dump(datos, archivo, indent=2)

    #Reinicia las celdas de la tabla dandole los valores por defecto
    def reiniciarDatos(self):
        tabla = self.horarios.tablaHorario
        numFilas = tabla.rowCount()
        numColumnas = tabla.columnCount()
        for fila in range(numFilas):
            for columna in range(numColumnas):
                tabla.setItem(fila, columna, QTableWidgetItem(""))
        self.guardarDatos()