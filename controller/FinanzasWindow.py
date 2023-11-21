from PyQt6 import uic
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QTableWidgetItem
import json
import pyqtgraph as pg
import numpy as np
import math


class Finanza():

    def __init__(self) -> None:
        self.finanzas = uic.loadUi("../SLI_Trabajo_Final/resources/templates/finanzas.ui")
        self.finanzas.show()
        self.finanzas.showMaximized()
        #Inicializar Finanza Semanal
        self.cargarDatos()
        self.aplicar()
        self.reiniciar()
        self.plot = None
        self.grafico()
        #inicializar Finanza Mensual
        self.cargarDatosMensual()
        self.aplicarMensual()
        self.reiniciarMensual()
        self.plotLinealMensual = None
        self.plotMensual = None
        self.graficoLinealMensual()
        self.graficoMensual()
        #inicializar Anual
        self.cargarDatosAnual()
        self.aplicarAnual()
        self.reiniciarAnual()
        self.plotLineal = None
        self.graficoLineal()
        self.mostrarConclusionAnual()
        #inicializar Calculadora
        self.calcularInteres()
        self.reiniciarInteres()
        self.calcularDescuento()
        self.reiniciarDescuento()
        self.calcularCuota()
        self.reiniciarCuota()
        self.calcularMetaAhorro()
        self.reiniciarMetaAhorro()


#----------------------------------Finanza Semanal----------------------------------#

    def cargarDatos(self):
        try:
            with open('finanzaSemanal.json', 'r') as archivo:
                datos = json.load(archivo)
                #self.datos_originales = datos
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

        with open('finanzaSemanal.json', 'w') as archivo:
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

#----------------------------------Finanza Mensual----------------------------------#

    def cargarDatosMensual(self):
        try:
            with open('finanzaMensual.json', 'r') as archivo:
                datos = json.load(archivo)
                self.llenarTablaDesdeJSONMensual(datos)
        except FileNotFoundError:
            self.finanzas.aviso_txtM.setText("No se encontró el archivo de datos")
        self.cargarValoresMensual()

    def cargarValoresMensual(self):
        self.calcularGastosMensual()
        self.calcularAhorrosMensual()
        self.calcularIngresosMensual()

    def llenarTablaDesdeJSONMensual(self, datos):
        tablaMensual = self.finanzas.tablaMensual
        for columna, filas in datos.items():
            for fila, valor in filas.items():
                col = int(columna.replace("columna", ""))
                fil = int(fila.replace("fila", ""))
                tablaMensual.setItem(fil, col, QTableWidgetItem(str(valor)))

    def calcularIngresosMensual(self):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        suma = 0
        for fila in range(numFilas):
            if fila != 4:
                item = tablaMensual.item(fila, 0)
                suma = suma + int(item.text())
        totalIngreso = '{:,}'.format(suma)
        tablaMensual.setItem(4, 0, QTableWidgetItem(str(totalIngreso)))

    def calcularGastosMensual(self):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        suma = 0
        for fila in range(numFilas):
            if fila != 4:
                item = tablaMensual.item(fila, 1)
                suma = suma + int(item.text())
        totalGasto = '{:,}'.format(suma)
        tablaMensual.setItem(4, 1, QTableWidgetItem(str(totalGasto)))

    def calcularAhorrosMensual(self):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        suma = 0
        for fila in range(numFilas):
            if fila != 4:
                item = tablaMensual.item(fila, 2)
                suma = suma + int(item.text())
        totalAhorros = '{:,}'.format(suma)
        tablaMensual.setItem(4, 2, QTableWidgetItem(str(totalAhorros)))

    def aplicarMensual(self):
        self.finanzas.btnAplicarM.clicked.connect(self.comprobarDatosMensual)

    def comprobarDatosMensual(self):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        numColumnas = tablaMensual.columnCount()
        valores_validos = True

        for fila in range(numFilas):
            for columna in range(numColumnas):
                item = tablaMensual.item(fila, columna)
                if item is not None:
                    valor = item.text()
                    if not self.validarNumero(valor):
                        valores_validos = False
                        break

        if valores_validos:
            self.guardarDatosMensual()
            self.calcularAhorrosMensual()
            self.calcularGastosMensual()
            self.calcularIngresosMensual()
            self.graficoMensual()
            self.graficoLinealMensual()
            self.comprobarMetas()
            self.finanzas.aviso_txtM.setText("")
        else:
            self.finanzas.aviso_txtM.setText("Se encontraron valores inválidos")

    def guardarDatosMensual(self):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        numColumnas = tablaMensual.columnCount()
        datos = {}

        for columna in range(numColumnas):
            datos[f"columna{columna}"] = {}
            for fila in range(numFilas):
                item = tablaMensual.item(fila, columna)
                if item is not None:
                    valor = item.text()
                else:
                    valor = 0
                datos[f"columna{columna}"][f"fila{fila}"] = valor

        with open('finanzaMensual.json', 'w') as archivo:
            json.dump(datos, archivo, indent=2)
        
    def reiniciarMensual(self):
        self.finanzas.btnReiniciarM.clicked.connect(self.reiniciarDatosMensual)

    def reiniciarDatosMensual(self):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        numColumnas = tablaMensual.columnCount()
        for fila in range(numFilas):
            for columna in range(numColumnas):
                tablaMensual.setItem(fila, columna, QTableWidgetItem(str(0)))
        self.guardarDatosMensual()
        self.graficoLinealMensual()
        self.graficoMensual()
        self.finanzas.aviso_txtM.setText("")
        tablaMensual.setItem(4, 0, QTableWidgetItem("0"))
        tablaMensual.setItem(4, 1, QTableWidgetItem("0"))
        tablaMensual.setItem(4, 2, QTableWidgetItem("0"))

    def borrarGraficoLinealMensual(self):
        if self.plotLinealMensual is not None:
            self.plotLinealMensual.hide() 

    def graficoLinealMensual(self):
        self.borrarGraficoLinealMensual()  

        semanas = np.arange(1, 5)
        ingresos = []
        self.valoresColumnaMensual(0,ingresos)
        gastos = []
        self.valoresColumnaMensual(1,gastos)
        ahorros = []
        self.valoresColumnaMensual(2,ahorros)

        plotLinealMensual = pg.PlotWidget(title="Gráfico Mensual", color="black")
        plotLinealMensual.plot(semanas, ingresos, pen=(0, 0, 255), name="Ingresos")
        plotLinealMensual.plot(semanas, gastos, pen=(255, 0, 0), name="Gastos")
        plotLinealMensual.plot(semanas, ahorros, pen=(0, 255, 0), name="Ahorros")

        plotLinealMensual.setLabel("bottom", "Mensual", color=(0, 0, 0))
        plotLinealMensual.setLabel("left", "Dinero ($)", color=(0, 0, 0))
        plotLinealMensual.addLegend()
        plotLinealMensual.setTitle("Gráfico Mensual", color="black")
        plotLinealMensual.setBackground("#FFFF")
        plotLinealMensual.getAxis("bottom").setPen(color="black")
        plotLinealMensual.getAxis("left").setPen(color="black")
        plotLinealMensual.getAxis("bottom").setLabel(color="black")
        plotLinealMensual.getAxis("left").setLabel(color="black")
        plotLinealMensual.getAxis("bottom").setTextPen(color="black")
        plotLinealMensual.getAxis("left").setTextPen(color="black")

        self.finanzas.frameGraficoM_1.setLayout(QVBoxLayout())
        self.finanzas.frameGraficoM_1.layout().addWidget(plotLinealMensual)
        self.plotLinealMensual = plotLinealMensual
    
    def borrarGraficoMensual(self):
        if self.plotMensual is not None:
            self.plotMensual.hide() 

    def graficoMensual(self):
        self.borrarGraficoMensual() 
        plotMensual = pg.PlotWidget(title="Gráfico de Gastos", color="black")
        
        x = [1, 2, 3]
        y = [self.gastosColumnaMensual(0), self.gastosColumnaMensual(1),
            self.gastosColumnaMensual(2)]

        bar = pg.BarGraphItem(x=x, height=y, width=0.4, brush="lightblue")

        plotMensual.addItem(bar)

        plotMensual.setBackground("#FFFF")
        plotMensual.setLabel("bottom", "Días", color=(0, 0, 0))
        plotMensual.setLabel("left", "Gastos", color=(0, 0, 0))
        plotMensual.setTitle("Gráfico de Gastos", color="black")
        plotMensual.getAxis("bottom").setPen(color="black")
        plotMensual.getAxis("left").setPen(color="black")
        plotMensual.getAxis("bottom").setLabel(color="black")  
        plotMensual.getAxis("left").setLabel(color="black")  
        plotMensual.getAxis("bottom").setTextPen(color="black")  
        plotMensual.getAxis("left").setTextPen(color="black")   
        

        self.finanzas.frameGraficoM_2.setLayout(QVBoxLayout()) 
        self.finanzas.frameGraficoM_2.layout().addWidget(plotMensual)  
        self.plotMensual = plotMensual

    def gastosColumnaMensual(self, columna):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        suma = 0
        for fila in range(numFilas):
            if fila != 4:
                item = tablaMensual.item(fila, columna)
                suma = suma + int(item.text())
        return suma

    def valoresColumnaMensual(self, columna, lista):
        tablaMensual = self.finanzas.tablaMensual
        numFilas = tablaMensual.rowCount()
        for fila in range(numFilas):
            if fila != 4:
                item = tablaMensual.item(fila, columna)
                valor = int(item.text())
                lista.append(valor)

    def comprobarMetas(self):
        pass
        '''
        if int(self.finanzas.tablaMensual.item(4, 0)) >= self.finanzas.spin1M.value():
            self.finanzas.check1.setChecked(True)
        else:
            self.finanzas.check1.setChecked(False)
        if int(self.finanzas.tablaMensual.item(4, 1)) <= self.finanzas.spin2M.value():
            self.finanzas.check2.setChecked(True)
        else:
            self.finanzas.check2.setChecked(False)
        if int(self.finanzas.tablaMensual.item(4, 2)) >= self.finanzas.spin3M.value():
            self.finanzas.check3.setChecked(True)
        else:
            self.finanzas.check3.setChecked(False)
        '''

#----------------------------------Finanza Anual----------------------------------#

    def cargarDatosAnual(self):
        try:
            with open('finanzaAnual.json', 'r') as archivo:
                datos = json.load(archivo)
                self.llenarTablaDesdeJSONAnual(datos)
        except FileNotFoundError:
            self.finanzas.aviso_txt.setText("No se encontró el archivo de datos")
        self.cargarValoresAnual()
    
    def cargarValoresAnual(self):
        self.calcularGastosAnual()
        self.calcularAhorrosAnual()
        self.calcularIngresosAnual()

    def llenarTablaDesdeJSONAnual(self, datos):
        tablaAnual = self.finanzas.tablaAnual
        for columna, filas in datos.items():
            for fila, valor in filas.items():
                col = int(columna.replace("columna", ""))
                fil = int(fila.replace("fila", ""))
                tablaAnual.setItem(fil, col, QTableWidgetItem(str(valor)))

    def calcularIngresosAnual(self):
        tablaAnual = self.finanzas.tablaAnual
        numFilas = tablaAnual.rowCount()
        suma = 0
        for fila in range(numFilas):
            item = tablaAnual.item(fila, 0)
            suma = suma + int(item.text())
        totalIngreso = '{:,}'.format(suma)
        self.finanzas.ingresos_txtA.setText(f"{totalIngreso}$")

    def calcularGastosAnual(self):
        tablaAnual = self.finanzas.tablaAnual
        numFilas = tablaAnual.rowCount()
        suma = 0
        for fila in range(numFilas):
            item = tablaAnual.item(fila, 1)
            suma = suma + int(item.text())
        totalGasto = '{:,}'.format(suma)
        self.finanzas.gastos_txtA.setText(f"{totalGasto}$")

    def calcularAhorrosAnual(self):
        tablaAnual = self.finanzas.tablaAnual
        numFilas = tablaAnual.rowCount()
        suma = 0
        for fila in range(numFilas):
            item = tablaAnual.item(fila, 2)
            suma = suma + int(item.text())
        totalAhorros = '{:,}'.format(suma)
        self.finanzas.ahorros_txtA.setText(f"{totalAhorros}$")

    def aplicarAnual(self):
        self.finanzas.btnAplicarA.clicked.connect(self.comprobarDatosAnual)

    def comprobarDatosAnual(self):
        tablaAnual = self.finanzas.tablaAnual
        numFilas = tablaAnual.rowCount()
        numColumnas = tablaAnual.columnCount()
        valores_validos = True

        for fila in range(numFilas):
            for columna in range(numColumnas):
                item = tablaAnual.item(fila, columna)
                if item is not None:
                    valor = item.text()
                    if not self.validarNumero(valor):
                        valores_validos = False
                        break

        if valores_validos:
            self.guardarDatosAnual()
            self.calcularAhorrosAnual()
            self.calcularGastosAnual()
            self.calcularIngresosAnual()
            self.mostrarConclusionAnual()
            self.graficoLineal()
            self.finanzas.aviso_txtA.setText("")
        else:
            self.finanzas.aviso_txtA.setText("Se encontraron valores inválidos")

    def guardarDatosAnual(self):
        tablaAnual = self.finanzas.tablaAnual
        numFilas = tablaAnual.rowCount()
        numColumnas = tablaAnual.columnCount()
        datos = {}

        for columna in range(numColumnas):
            datos[f"columna{columna}"] = {}
            for fila in range(numFilas):
                item = tablaAnual.item(fila, columna)
                if item is not None:
                    valor = item.text()
                else:
                    valor = 0
                datos[f"columna{columna}"][f"fila{fila}"] = valor

        with open('finanzaAnual.json', 'w') as archivo:
            json.dump(datos, archivo, indent=2)
        
    def reiniciarAnual(self):
        self.finanzas.btnReiniciarA.clicked.connect(self.reiniciarDatosAnual)

    def reiniciarDatosAnual(self):
        tablaAnual = self.finanzas.tablaAnual
        numFilas = tablaAnual.rowCount()
        numColumnas = tablaAnual.columnCount()
        for fila in range(numFilas):
            for columna in range(numColumnas):
                tablaAnual.setItem(fila, columna, QTableWidgetItem(str(0)))
        self.guardarDatosAnual()
        self.graficoLineal()
        self.finanzas.aviso_txtA.setText("")
        self.finanzas.ahorros_txtA.setText("0$")
        self.finanzas.gastos_txtA.setText("0$")
        self.finanzas.ingresos_txtA.setText("0$")
        self.finanzas.conclusion_txtA.setText("")

    def mostrarConclusionAnual(self):
        ingresos = self.finanzas.ingresos_txtA.text().replace(',', '')
        ingresos = ''.join([caracter for caracter in ingresos if caracter != "$"])
        gastos = self.finanzas.gastos_txtA.text().replace(',', '')
        gastos = ''.join([caracter for caracter in gastos if caracter != "$"])
        ahorros = self.finanzas.ahorros_txtA.text().replace(',', '')
        ahorros = ''.join([caracter for caracter in ahorros if caracter != "$"])
        if self.validarNumero(ingresos):
            total = int(ingresos) - int(gastos) - int(ahorros)
            totalFinal = '{:,}'.format(total)
            ahorroFinal = '{:,}'.format(int(ahorros))
            if  int(ingresos) < int(gastos):
                self.finanzas.conclusion_txtA.setText(f"De acuerdo a los datos actuales, usted está gastando más de lo que gana. Se recomienda reducir los gastos.")
            elif int(ingresos)  > int(gastos):
                self.finanzas.conclusion_txtA.setText(f"De acuerdo a los datos actuales, usted está ganando más de lo que gasta. Se recomienda continuar con su modelo de gestión.")
            elif int(ingresos)  == int(gastos):
                self.finanzas.conclusion_txtA.setText(f"De acuerdo a los datos actuales usted no obtuvo perdidas ni ganancias. Se recomienda reducir los gastos para que pueda mejorar sus ganancias.")
        else:
            self.finanzas.aviso_txtA.setText("Error")

    def valoresColumna(self, columna, lista):
        tablaAnual = self.finanzas.tablaAnual
        numFilas = tablaAnual.rowCount()
        for fila in range(numFilas):
            item = tablaAnual.item(fila, columna)
            valor = int(item.text())
            lista.append(valor)

    def borrarGraficoLineal(self):
        if self.plotLineal is not None:
            self.plotLineal.hide() 

    def graficoLineal(self):
        self.borrarGraficoLineal()  

        meses = np.arange(1, 13)
        ingresos = []
        self.valoresColumna(0,ingresos)
        gastos = []
        self.valoresColumna(1,gastos)
        ahorros = []
        self.valoresColumna(2,ahorros)

        plotLineal = pg.PlotWidget(title="Gráfico Anual", color="black")
        plotLineal.plot(meses, ingresos, pen=(0, 0, 255), name="Ingresos")
        plotLineal.plot(meses, gastos, pen=(255, 0, 0), name="Gastos")
        plotLineal.plot(meses, ahorros, pen=(0, 255, 0), name="Ahorros")

        plotLineal.setLabel("bottom", "Meses", color=(0, 0, 0))
        plotLineal.setLabel("left", "Dinero ($)", color=(0, 0, 0))
        plotLineal.addLegend()
        plotLineal.setTitle("Gráfico Anual", color="black")
        plotLineal.setBackground("#FFFF")
        plotLineal.getAxis("bottom").setPen(color="black")
        plotLineal.getAxis("left").setPen(color="black")
        plotLineal.getAxis("bottom").setLabel(color="black")
        plotLineal.getAxis("left").setLabel(color="black")
        plotLineal.getAxis("bottom").setTextPen(color="black")
        plotLineal.getAxis("left").setTextPen(color="black")

        self.finanzas.frameGraficoA.setLayout(QVBoxLayout())
        self.finanzas.frameGraficoA.layout().addWidget(plotLineal)
        self.plotLineal = plotLineal

#----------------------------------Calculadora----------------------------------#

    def calcularInteres(self):
        self.finanzas.btnCalcular1.clicked.connect(self.interesCalculadora)

    def reiniciarInteres(self):
        self.finanzas.btnReiniciar1.clicked.connect(self.reiniciarValoresInteres)

    def calcularDescuento(self):
        self.finanzas.btnCalcular2.clicked.connect(self.descuentoCalculadora)

    def reiniciarDescuento(self):
        self.finanzas.btnReiniciar2.clicked.connect(self.reiniciarValoresDescuento)

    def calcularCuota(self):
        self.finanzas.btnCalcular3.clicked.connect(self.cuotaCalculadora)

    def reiniciarCuota(self):
        self.finanzas.btnReiniciar3.clicked.connect(self.reiniciarValoresCuota)

    def calcularMetaAhorro(self):
        self.finanzas.btnCalcular4.clicked.connect(self.metaCalculadora)

    def reiniciarMetaAhorro(self):
        self.finanzas.btnReiniciar4.clicked.connect(self.reiniciarValoresMeta)

    def pasar(self):
        pass

    def interesCalculadora(self):
        if self.validarNumero(self.finanzas.input1.text()):
            precio = int(self.finanzas.input1.text())
            valor = self.finanzas.spin1.value()

            total = precio + (precio * (valor / 100))

            self.finanzas.rta1.setText(str(total) + "$")
            self.finanzas.aviso1.setText("")
        else:
            self.finanzas.aviso1.setText("Valores Invalidos")

    def reiniciarValoresInteres(self):
        self.finanzas.input1.setText("0")
        self.finanzas.spin1.setValue(00.0)
        self.finanzas.rta1.setText("0$")
        self.finanzas.aviso1.setText("")

    def descuentoCalculadora(self):
        if self.validarNumero(self.finanzas.input2.text()):
            precio = int(self.finanzas.input2.text())
            valor = self.finanzas.spin2.value()

            total = precio - (precio * (valor / 100))

            self.finanzas.rta2.setText(str(total) + "$")
            self.finanzas.aviso2.setText("")
        else:
            self.finanzas.aviso2.setText("Valores Invalidos")

    def reiniciarValoresDescuento(self):
        self.finanzas.input2.setText("0")
        self.finanzas.spin2.setValue(00.0)
        self.finanzas.rta2.setText("0$")
        self.finanzas.aviso2.setText("")

    def cuotaCalculadora(self):
        if self.validarNumero(self.finanzas.input3.text()):
            if self.finanzas.spin3_1.value() == 00.0:
                cuota = int(self.finanzas.input3.text())  / self.finanzas.spin3_2.value()
            else:
                interes = self.finanzas.spin3_1.value() / 100
                cuota = int(self.finanzas.input3.text()) * interes * (1 + interes)**self.finanzas.spin3_2.value() / ((1 + interes)**self.finanzas.spin3_2.value() - 1)
    
            cuotaFinal = "{:.2f}".format(math.ceil(cuota))
            self.finanzas.rta3.setText(str(cuotaFinal)+ "$")
            self.finanzas.aviso2.setText("")
        else:
            self.finanzas.aviso3.setText("Valores Invalidos")

    def reiniciarValoresCuota(self):
        self.finanzas.input3.setText("0")
        self.finanzas.spin3_1.setValue(00.0)
        self.finanzas.spin3_2.setValue(00.0)
        self.finanzas.rta3.setText("0$")
        self.finanzas.aviso3.setText("")

    def metaCalculadora(self):
        if self.validarNumero(self.finanzas.input4.text()):
            meta = int(self.finanzas.input4.text())
            meses = self.finanzas.spin4.value()
            
            total = meta / meses

            self.finanzas.rta4.setText(str(total) + "$")
            self.finanzas.aviso4.setText("")

        else:
            self.finanzas.aviso4.setText("Valores Invalidos")

    def reiniciarValoresMeta(self):
        self.finanzas.input4.setText("0")
        self.finanzas.spin4.setValue(0)
        self.finanzas.rta4.setText("0$")
        self.finanzas.aviso4.setText("")