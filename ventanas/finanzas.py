from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QTableWidgetItem
import json

from matplotlib.figure import Figure

class Finanza():
    def __init__(self) -> None:
        self.finanzas = uic.loadUi("../SLI_Trabajo_Final/ventanas/finanzas.ui")
        self.finanzas.setMinimumSize(self.finanzas.size()) 
        self.finanzas.setMaximumSize(self.finanzas.size())
        self.finanzas.show()
        #inicializar
        self.cargarDatos()
        self.aplicar()
        self.reiniciar()


    def cargarDatos(self):
        try:
            with open('tablaInput.json', 'r') as archivo:
                datos = json.load(archivo)
                self.llenarTablaDesdeJSON(datos)
        except FileNotFoundError:
            self.finanzas.aviso_txt.setText("No se encontró el archivo de datos")
        self.cargarValores()

    
    def cargarValores(self):
        self.calcularGastos()
        self.calcularAhorro()
        self.finanzas.ingresosInput.setText("0")


    def llenarTablaDesdeJSON(self, datos):
        tabla_input = self.finanzas.tablaInput
        for columna, filas in datos.items():
            for fila, valor in filas.items():
                col = int(columna.replace("columna", ""))
                fil = int(fila.replace("fila", ""))
                tabla_input.setItem(fil, col, QTableWidgetItem(str(valor)))


    def aplicar(self):
        self.finanzas.btnAplicar.clicked.connect(self.comprobarDatos)


    def comprobarDatos(self):
        tabla_input = self.finanzas.tablaInput
        num_filas = tabla_input.rowCount()
        num_columnas = tabla_input.columnCount()
        valores_validos = True

        for fila in range(num_filas):
            for columna in range(num_columnas):
                item = tabla_input.item(fila, columna)
                if item is not None:
                    valor = item.text()
                    if not self.validarNumero(valor):
                        valores_validos = False
                        break

        if valores_validos:
            self.guardarDatos()
            self.calcularAhorro()
            self.calcularGastos()
            self.aplicarFormato()
            self.mostrarConclusion()
            self.finanzas.aviso_txt.setText("")
        else:
            self.finanzas.aviso_txt.setText("Se encontraron valores inválidos")


    def guardarDatos(self):
        tabla_input = self.finanzas.tablaInput
        num_filas = tabla_input.rowCount()
        num_columnas = tabla_input.columnCount()
        datos = {}

        for columna in range(num_columnas):
            datos[f"columna{columna}"] = {}
            for fila in range(num_filas):
                item = tabla_input.item(fila, columna)
                if item is not None:
                    valor = item.text()
                else:
                    valor = 0
                datos[f"columna{columna}"][f"fila{fila}"] = valor

        with open('tablaInput.json', 'w') as archivo:
            json.dump(datos, archivo, indent=2)

        
    def reiniciar(self):
        self.finanzas.btnReiniciar.clicked.connect(self.reiniciarDatos)


    def reiniciarDatos(self):
        tabla_input = self.finanzas.tablaInput
        num_filas = tabla_input.rowCount()
        num_columnas = tabla_input.columnCount()
        for fila in range(num_filas):
            for columna in range(num_columnas):
                tabla_input.setItem(fila, columna, QTableWidgetItem(str(0)))
        self.guardarDatos()
        self.finanzas.aviso_txt.setText("")
        self.finanzas.ahorro_txt.setText("0$")
        self.finanzas.gastos_txt.setText("0$")
        self.finanzas.conclusion_txt.setText("")

    def validarNumero(self, item):
        try:
            int(item)
            return True
        except:
            return False
        
    def aplicarFormato(self):
        valor = self.finanzas.ingresosInput.text()
        if valor is None or valor == "":
            valor = 0
        else:
            valor = valor.replace(',', '')
            valorFinal = '{:,}'.format(int(valor))
            self.finanzas.ingresosInput.setText(f"{valorFinal}")
        
    #OPERACIONES

    def calcularGastos(self):
        tabla_input = self.finanzas.tablaInput
        num_filas = tabla_input.rowCount()
        num_columnas = tabla_input.columnCount()
        suma = 0
        for fila in range(num_filas):
            for columna in range(num_columnas):
                if (fila == 4):
                    pass
                else:
                    item = tabla_input.item(fila, columna)
                    suma = suma + int(item.text()) 
        totalGasto = '{:,}'.format(suma)
        self.finanzas.gastos_txt.setText(f"{totalGasto}$")



    def calcularAhorro(self):
        tabla_input = self.finanzas.tablaInput
        num_columnas = tabla_input.columnCount()
        suma = 0
        for columna in range(num_columnas):
                item = tabla_input.item(4, columna)
                suma = suma + int(item.text()) 
        totalAhorro = '{:,}'.format(suma)
        self.finanzas.ahorro_txt.setText(f"{totalAhorro}$")
        

    def mostrarConclusion(self):
        ingresos = self.finanzas.ingresosInput.text().replace(',', '')
        gastos = self.finanzas.gastos_txt.text().replace(',', '')
        gastos = ''.join([caracter for caracter in gastos if caracter != "$"])
        total = int(ingresos) - int(gastos)
        totalFinal = '{:,}'.format(total)
        if total < 0:
            self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted gasto más dinero de lo que tenía. Dinero Actual = {totalFinal}$")
        elif total >0:
            self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted no gasto todo dinero que tenía. Dinero Actual = {totalFinal}$")
        elif total == 0:
            self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted gasto todo el dinero que tenía. Dinero Actual = {totalFinal}$")
        
    
    def grafico(self):
        pass