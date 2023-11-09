from PyQt6 import uic
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QTableWidgetItem
import json
import pyqtgraph as pg


class Finanza():

    def __init__(self) -> None:
        self.finanzas = uic.loadUi("../SLI_Trabajo_Final/resources/templates/finanzas.ui")
        self.finanzas.show()
        self.finanzas.showMaximized()
        #Inicializar
        self.cargarDatos()
        self.aplicar()
        self.reiniciar()
        self.plot = None
        self.grafico()
        

    def cargarDatos(self):
        try:
            with open('tablaInput.json', 'r') as archivo:
                datos = json.load(archivo)
                self.datos_originales = datos
                self.llenarTablaDesdeJSON(datos)
        except FileNotFoundError:
            self.finanzas.aviso_txt.setText("No se encontró el archivo de datos")
        self.cargarValores()

    
    def cargarValores(self):
        self.calcularGastos()
        self.calcularAhorro()
        self.finanzas.ingresosInput.setText("0")


    def llenarTablaDesdeJSON(self, datos):
        tablaInput = self.finanzas.tablaInput
        for columna, filas in datos.items():
            for fila, valor in filas.items():
                col = int(columna.replace("columna", ""))
                fil = int(fila.replace("fila", ""))
                tablaInput.setItem(fil, col, QTableWidgetItem(str(valor)))


    def aplicar(self):
        self.finanzas.btnAplicar.clicked.connect(self.comprobarDatos)


    def comprobarDatos(self):
        tablaInput = self.finanzas.tablaInput
        numFilas = tablaInput.rowCount()
        numColumnas = tablaInput.columnCount()
        valores_validos = True

        for fila in range(numFilas):
            for columna in range(numColumnas):
                item = tablaInput.item(fila, columna)
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
            self.grafico()
            self.finanzas.aviso_txt.setText("")
        else:
            self.finanzas.aviso_txt.setText("Se encontraron valores inválidos")


    def guardarDatos(self):
        tablaInput = self.finanzas.tablaInput
        numFilas = tablaInput.rowCount()
        numColumnas = tablaInput.columnCount()
        datos = {}

        for columna in range(numColumnas):
            datos[f"columna{columna}"] = {}
            for fila in range(numFilas):
                item = tablaInput.item(fila, columna)
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
        tablaInput = self.finanzas.tablaInput
        numFilas = tablaInput.rowCount()
        numColumnas = tablaInput.columnCount()
        for fila in range(numFilas):
            for columna in range(numColumnas):
                tablaInput.setItem(fila, columna, QTableWidgetItem(str(0)))
        self.guardarDatos()
        self.grafico()
        self.finanzas.aviso_txt.setText("")
        self.finanzas.ahorros_txt.setText("0$")
        self.finanzas.gastos_txt.setText("0$")
        self.finanzas.conclusion_txt.setText("")

    def validarNumero(self, item):
        try:
            int(item)
            return True
        except:
            return False
        
    def aplicarFormato(self):
        valor = self.finanzas.ingresosInput.text().replace(',', '')
        if valor is None or valor == "" or not self.validarNumero(str(valor)):
            valor = 0
            self.finanzas.ingresosInput.setText("0")
            #self.finanzas.aviso_txt.setText("Valor invalido en 'Ingreso', se reemplazo con 0")
        else:
            valor = valor.replace(',', '')
            valorFinal = '{:,}'.format(int(valor))
            self.finanzas.ingresosInput.setText(f"{valorFinal}")
        
    #OPERACIONES

    def calcularGastos(self):
        tablaInput = self.finanzas.tablaInput
        numFilas = tablaInput.rowCount()
        numColumnas = tablaInput.columnCount()
        suma = 0
        for fila in range(numFilas):
            for columna in range(numColumnas):
                if (fila == 4):
                    pass
                else:
                    item = tablaInput.item(fila, columna)
                    suma = suma + int(item.text()) 
        totalGasto = '{:,}'.format(suma)
        self.finanzas.gastos_txt.setText(f"{totalGasto}$")



    def calcularAhorro(self):
        tablaInput = self.finanzas.tablaInput
        numColumnas = tablaInput.columnCount()
        suma = 0
        for columna in range(numColumnas):
                item = tablaInput.item(4, columna)
                suma = suma + int(item.text()) 
        totalAhorro = '{:,}'.format(suma)
        self.finanzas.ahorros_txt.setText(f"{totalAhorro}$")
        

    def mostrarConclusion(self):
        ingresos = self.finanzas.ingresosInput.text().replace(',', '')
        gastos = self.finanzas.gastos_txt.text().replace(',', '')
        gastos = ''.join([caracter for caracter in gastos if caracter != "$"])
        ahorros = self.finanzas.ahorros_txt.text().replace(',', '')
        ahorros = ''.join([caracter for caracter in ahorros if caracter != "$"])
        if self.validarNumero(ingresos):
            total = int(ingresos) - int(gastos) - int(ahorros)
            totalFinal = '{:,}'.format(total)
            ahorroFinal = '{:,}'.format(int(ahorros))
            if total < 0:
                self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted gasto más dinero de lo que tenía. Dinero Actual = {totalFinal}$. Ahorros: {ahorroFinal}$.")
            elif total >0:
                self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted no gasto todo dinero que tenía. Dinero Actual = {totalFinal}$. Ahorros: {ahorroFinal}$.")
            elif total == 0:
                self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted gasto todo el dinero que tenía. Dinero Actual = {totalFinal}$. Ahorros: {ahorroFinal}$.")
        else:
            self.finanzas.aviso_txt.setText("Error")
    
    def gastosColumna(self, columna):
        tablaInput = self.finanzas.tablaInput
        numFilas = tablaInput.rowCount()
        suma = 0
        for fila in range(numFilas):
            if fila == 4:
                pass
            else:
                item = tablaInput.item(fila, columna)
                suma = suma + int(item.text())
        return suma

    def borrarGrafico(self):
        if self.plot is not None:
            self.plot.hide() 

    def grafico(self):
        self.borrarGrafico() 
        plot = pg.PlotWidget(title="Gráfico de Gastos", color="black")
        
        x = [1, 2, 3, 4, 5, 6, 7]
        y = [self.gastosColumna(0), self.gastosColumna(1),
            self.gastosColumna(2), self.gastosColumna(3),
            self.gastosColumna(4), self.gastosColumna(5),
            self.gastosColumna(6)]

        bar = pg.BarGraphItem(x=x, height=y, width=0.4, brush="lightblue")

        plot.addItem(bar)

        plot.setBackground("#FFFF")
        plot.setLabel("bottom", "Días", color=(0, 0, 0))
        plot.setLabel("left", "Gastos", color=(0, 0, 0))
        plot.setTitle("Gráfico de Gastos", color="black")
        plot.getAxis("bottom").setPen(color="black")
        plot.getAxis("left").setPen(color="black")
        plot.getAxis("bottom").setLabel(color="black")  
        plot.getAxis("left").setLabel(color="black")  
        plot.getAxis("bottom").setTextPen(color="black")  
        plot.getAxis("left").setTextPen(color="black")   
        

        self.finanzas.frameGrafico.setLayout(QVBoxLayout()) 
        self.finanzas.frameGrafico.layout().addWidget(plot)  
        self.plot = plot