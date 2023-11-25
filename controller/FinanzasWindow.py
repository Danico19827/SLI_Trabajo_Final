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
        self.tablas = {"Semanal": self.finanzas.tablaSemanal,"Mensual": self.finanzas.tablaMensual,"Anual": self.finanzas.tablaAnual}
        self.aplicar()
        self.reiniciar()
        #Inicializar Finanza Semanal
        self.cargarDatos("Semanal")
        self.plot = None
        self.grafico("Semanal")
        #inicializar Finanza Mensual
        self.cargarDatos("Mensual")
        self.plotLinealMensual = None
        self.plotMensual = None
        self.grafico("Mensual")
        self.leerTxt()
        #inicializar Anual
        self.cargarDatos("Anual")
        self.plotLineal = None
        self.grafico("Anual")
        self.mostrarConclusion("Anual")

#----------------------------------Finanza Semanal----------------------------------#

    def aplicar(self):
        self.finanzas.btnAplicar.clicked.connect(lambda: self.comprobarDatos("Semanal"))
        self.finanzas.btnAplicarM.clicked.connect(lambda: self.comprobarDatos("Mensual"))
        self.finanzas.btnAplicarA.clicked.connect(lambda: self.comprobarDatos("Anual"))
        self.finanzas.btnGuardarM.clicked.connect(self.guardarTxT)
        self.finanzas.btnCalcular1.clicked.connect(self.interesCalculadora)
        self.finanzas.btnCalcular2.clicked.connect(self.descuentoCalculadora)
        self.finanzas.btnCalcular3.clicked.connect(self.cuotaCalculadora)
        self.finanzas.btnCalcular4.clicked.connect(self.metaCalculadora)

    def reiniciar(self):
        self.finanzas.btnReiniciar.clicked.connect(lambda: self.reiniciarDatos("Semanal"))
        self.finanzas.btnReiniciarM.clicked.connect(lambda: self.reiniciarDatos("Mensual"))
        self.finanzas.btnReiniciarA.clicked.connect(lambda: self.reiniciarDatos("Anual"))
        self.finanzas.btnReiniciar1.clicked.connect(self.reiniciarValoresInteres)
        self.finanzas.btnReiniciar2.clicked.connect(self.reiniciarValoresDescuento)
        self.finanzas.btnReiniciar3.clicked.connect(self.reiniciarValoresCuota)
        self.finanzas.btnReiniciar4.clicked.connect(self.reiniciarValoresMeta)

    def cargarDatos(self, tipo):
        try:
            with open(f'finanza{tipo}.json', 'r') as archivo:
                datos = json.load(archivo)
                self.llenarTablaDesdeJSON(datos, tipo)
        except FileNotFoundError:
            self.finanzas.aviso_txt.setText("No se encontró el archivo de datos")
        self.cargarValores(tipo)
    
    def cargarValores(self, tipo):
        if tipo == "Semanal":
            self.calcularGastos(tipo)
            self.calcularAhorro(tipo)
            self.finanzas.ingresosInput.setText("0")
        elif tipo == "Mensual":
            self.calcularGastos(tipo)
            self.calcularAhorro(tipo)
            self.calcularIngreso(tipo)
        else:
            self.calcularGastos(tipo)
            self.calcularAhorro(tipo)
            self.calcularIngreso(tipo)

    def llenarTablaDesdeJSON(self, datos, tipo):
        tabla = self.tablas[tipo]
        for columna, filas in datos.items():
            for fila, valor in filas.items():
                col = int(columna.replace("columna", ""))
                fil = int(fila.replace("fila", ""))
                tabla.setItem(fil, col, QTableWidgetItem(str(valor)))

    def comprobarDatos(self, tipo):
        tabla = self.tablas[tipo]
        numFilas = tabla.rowCount()
        numColumnas = tabla.columnCount()
        valoresValidos = True

        for fila in range(numFilas):
            for columna in range(numColumnas):
                item = tabla.item(fila, columna)
                if item is not None:
                    valor = item.text()
                    if not self.validarNumero(valor):
                        valoresValidos = False
                        break

        if valoresValidos:
            if tipo == "Semanal":
                self.guardarDatos(tipo)
                self.calcularAhorro(tipo)
                self.calcularGastos(tipo)
                self.mostrarConclusion(tipo)
                self.grafico(tipo)
                self.finanzas.aviso_txt.setText("")
            elif tipo == "Mensual": 
                self.guardarDatos(tipo)
                self.calcularAhorro(tipo)
                self.calcularGastos(tipo)
                self.calcularIngreso(tipo)
                self.grafico(tipo)
                self.comprobarMetas()
                self.finanzas.aviso_txtM.setText("")
            else:
                self.guardarDatos(tipo)
                self.calcularAhorro(tipo)
                self.calcularGastos(tipo)
                self.calcularIngreso(tipo)
                self.mostrarConclusion(tipo)
                self.grafico(tipo)
                self.finanzas.aviso_txtA.setText("")
        else:
            if tipo == "Semanal": self.finanzas.aviso_txt.setText("Se encontraron valores inválidos")
            elif tipo == "Mensual": self.finanzas.aviso_txtM.setText("Se encontraron valores inválidos")
            else: self.finanzas.aviso_txtA.setText("Se encontraron valores inválidos")

    def guardarDatos(self, tipo):
        tabla = self.tablas[tipo]
        numFilas = tabla.rowCount()
        numColumnas = tabla.columnCount()
        datos = {}

        for columna in range(numColumnas):
            datos[f"columna{columna}"] = {}
            for fila in range(numFilas):
                item = tabla.item(fila, columna)
                if item is not None:
                    valor = item.text()
                else:
                    valor = 0
                datos[f"columna{columna}"][f"fila{fila}"] = valor

        with open(f'finanza{tipo}.json', 'w') as archivo:
            json.dump(datos, archivo, indent=2)

    def reiniciarDatos(self, tipo):
        if tipo == "Semanal": 
            tabla = self.finanzas.tablaSemanal
            self.finanzas.aviso_txt.setText("")
            self.finanzas.ahorros_txt.setText("0")
            self.finanzas.gastos_txt.setText("0")
            self.finanzas.conclusion_txt.setText("")
        elif tipo == "Mensual": 
            tabla = self.finanzas.tablaMensual
            self.finanzas.aviso_txtM.setText("")
            tabla.setItem(4, 0, QTableWidgetItem("0"))
            tabla.setItem(4, 1, QTableWidgetItem("0"))
            tabla.setItem(4, 2, QTableWidgetItem("0"))
        else: 
            tabla = self.finanzas.tablaAnual
            self.finanzas.aviso_txtA.setText("")
            self.finanzas.ahorros_txtA.setText("0")
            self.finanzas.gastos_txtA.setText("0")
            self.finanzas.ingresos_txtA.setText("0")
            self.finanzas.conclusion_txtA.setText("")
        numFilas = tabla.rowCount()
        numColumnas = tabla.columnCount()
        for fila in range(numFilas):
            for columna in range(numColumnas):
                tabla.setItem(fila, columna, QTableWidgetItem(str(0)))
        self.guardarDatos(tipo)
        self.grafico(tipo)
        
    def validarNumero(self, item):
        try:
            int(item)
            return True
        except:
            return False
        
    #OPERACIONES

    def calcularGastos(self, tipo):
        tabla = self.tablas[tipo]
        numFilas = tabla.rowCount()
        numColumnas = tabla.columnCount()
        suma = 0
        for fila in range(numFilas):
            if tipo == "Semanal":
                for columna in range(numColumnas):
                    item = tabla.item(fila, columna)
                    suma = suma + int(item.text()) 
            elif tipo == "Mensual":
                if fila != 4:
                    item = tabla.item(fila, 1)
                    suma = suma + int(item.text())
            else:
                item = tabla.item(fila, 1)
                suma = suma + int(item.text())
        totalGasto = suma
        if tipo == "Semanal":
            self.finanzas.gastos_txt.setText(str(totalGasto))
        elif tipo == "Mensual":
            tabla.setItem(4, 1, QTableWidgetItem(str(totalGasto)))
        else:
            self.finanzas.gastos_txtA.setText(str(totalGasto))
            

    def calcularAhorro(self, tipo):
        tabla = self.tablas[tipo]
        numColumnas = tabla.columnCount()
        numFilas = tabla.rowCount()
        suma = 0
        if tipo == "Semanal":
            for columna in range(numColumnas):
                    item = tabla.item(4, columna)
                    suma = suma + int(item.text()) 
            totalAhorro = int(suma)
            self.finanzas.ahorros_txt.setText(str(totalAhorro))
        elif tipo == "Mensual":
             for fila in range(numFilas):
                if fila != 4:
                    item = tabla.item(fila, 2)
                    suma = suma + int(item.text())
                totalAhorros = int(suma)
                tabla.setItem(4, 2, QTableWidgetItem(str(totalAhorros)))
        else:
            for fila in range(numFilas):
                item = tabla.item(fila, 2)
                suma = suma + int(item.text())
            totalAhorros = suma
            self.finanzas.ahorros_txtA.setText(str(totalAhorros))

    def calcularIngreso(self, tipo):
        tabla = self.tablas[tipo]
        numFilas = tabla.rowCount()
        suma = 0
        if tipo == "Mensual":
            for fila in range(numFilas):
                if fila != 4:
                    item = tabla.item(fila, 0)
                    suma = suma + int(item.text())
                totalIngreso = int(suma)
                tabla.setItem(4, 0, QTableWidgetItem(str(totalIngreso)))
        else:
            for fila in range(numFilas):
                item = tabla.item(fila, 0)
                suma = suma + int(item.text())
            totalIngresos = int(suma)
            self.finanzas.ingresos_txtA.setText(str(totalIngresos))

    def mostrarConclusion(self, tipo):
        if tipo == "Semanal":
            ingresos = self.finanzas.ingresosInput.text()
            gastos = self.finanzas.gastos_txt.text()
            ahorros = self.finanzas.ahorros_txt.text()
            if self.validarNumero(ingresos):
                total = int(ingresos) - int(gastos) - int(ahorros)
                totalFinal = '{:,}'.format(total)
                ahorroFinal = int(ahorros)
                if total < 0:
                    self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted gasto más dinero de lo que tenía. Dinero Actual = {totalFinal}$. Ahorros: {ahorroFinal}$.")
                elif total >0:
                    self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted no gasto todo dinero que tenía. Dinero Actual = {totalFinal}$. Ahorros: {ahorroFinal}$.")
                elif total == 0:
                    self.finanzas.conclusion_txt.setText(f"De acuerdo a sus ingresos, hasta ahora usted gasto todo el dinero que tenía. Dinero Actual = {totalFinal}$. Ahorros: {ahorroFinal}$.")
            else:
                self.finanzas.aviso_txt.setText("Error")
        else:
            ingresos = self.finanzas.ingresos_txtA.text().replace(',', '')
            gastos = self.finanzas.gastos_txtA.text().replace(',', '')
            gastos = ''.join([caracter for caracter in gastos if caracter != "$"])
            ahorros = self.finanzas.ahorros_txtA.text().replace(',', '')
            ahorros = ''.join([caracter for caracter in ahorros if caracter != "$"])
            if self.validarNumero(ingresos):
                if  int(ingresos) < int(gastos):
                    self.finanzas.conclusion_txtA.setText(f"De acuerdo a los datos actuales, usted está gastando más de lo que gana. Se recomienda reducir los gastos.")
                elif int(ingresos)  > int(gastos):
                    self.finanzas.conclusion_txtA.setText(f"De acuerdo a los datos actuales, usted está ganando más de lo que gasta. Se recomienda continuar con su modelo de gestión.")
                elif int(ingresos)  == int(gastos):
                    self.finanzas.conclusion_txtA.setText(f"De acuerdo a los datos actuales usted no obtuvo perdidas ni ganancias. Se recomienda reducir los gastos para que pueda mejorar sus ganancias.")
            else:
                self.finanzas.aviso_txtA.setText("Error") 
    
    def gastosColumna(self, columna, tipo):
        tabla = self.tablas[tipo]
        numFilas = tabla.rowCount()
        suma = 0
        for fila in range(numFilas):
            if tipo == "Semanal" or tipo == "Mensual":
                if fila != 4:
                    item = tabla.item(fila, columna)
                    suma = suma + int(item.text())
        return suma
    
    def valoresColumna(self, columna, lista, tipo):
        tabla = self.tablas[tipo]
        numFilas = tabla.rowCount()
        for fila in range(numFilas):
            if tipo == "Mensual":
                if fila != 4:
                    item = tabla.item(fila, columna)
                    valor = int(item.text())
                    lista.append(valor)
            else: 
                item = tabla.item(fila, columna)
                valor = int(item.text())
                lista.append(valor)

    def borrarGrafico(self, tipo):
        if tipo == "Semanal":
            if self.plot is not None:
                self.plot.hide() 
        elif tipo == "Mensual":
            if self.plotLinealMensual is not None:
                self.plotLinealMensual.hide() 
            if self.plotMensual is not None:
                self.plotMensual.hide()
        else: 
            if self.plotLineal is not None:
                self.plotLineal.hide() 

    def grafico(self, tipo):
        self.borrarGrafico(tipo) 
        if tipo == "Semanal":
            plot = pg.PlotWidget(title="Gráfico de Gastos", color="black")
            x = [1, 2, 3, 4, 5, 6, 7]
            y = [self.gastosColumna(0, "Semanal"), self.gastosColumna(1, "Semanal"),
                self.gastosColumna(2, "Semanal"), self.gastosColumna(3, "Semanal"),
                self.gastosColumna(4, "Semanal"), self.gastosColumna(5, "Semanal"),
                self.gastosColumna(6, "Semanal")]
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
        elif tipo == "Mensual": 
            plotMensual = pg.PlotWidget(title="Gráfico de Gastos", color="black")
            x = [1, 2, 3]
            y = [self.gastosColumna(0, "Mensual"), self.gastosColumna(1, "Mensual"),
                self.gastosColumna(2, "Mensual")]
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

            semanas = np.arange(1, 5)
            ingresos = []
            self.valoresColumna(0,ingresos, "Mensual")
            gastos = []
            self.valoresColumna(1,gastos, "Mensual")
            ahorros = []
            self.valoresColumna(2,ahorros, "Mensual")
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
        elif tipo == "Anual":
            meses = np.arange(1, 13)
            ingresos = []
            self.valoresColumna(0,ingresos, "Anual")
            gastos = []
            self.valoresColumna(1,gastos, "Anual")
            ahorros = []
            self.valoresColumna(2,ahorros, "Anual")
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

    def comprobarMetas(self):
        if int(self.finanzas.tablaMensual.item(4, 0).text()) >= self.finanzas.spin1M.value():
            self.finanzas.check1.setChecked(True)
        else:
            self.finanzas.check1.setChecked(False)
        if int(self.finanzas.tablaMensual.item(4, 1).text()) <= self.finanzas.spin2M.value():
            self.finanzas.check2.setChecked(True)
        else:
            self.finanzas.check2.setChecked(False)
        if int(self.finanzas.tablaMensual.item(4, 2).text()) >= self.finanzas.spin3M.value():
            self.finanzas.check3.setChecked(True)
        else:
            self.finanzas.check3.setChecked(False)

    def guardarTxT(self):
        texto = self.finanzas.autoEvM.toPlainText()
        with open("finanzaAutoEvaluacion.txt", "w") as archivo:
            archivo.write(str(texto))
        
    def leerTxt(self):
        with open("finanzaAutoEvaluacion.txt", "r") as archivo:
            texto = archivo.read()
            self.finanzas.autoEvM.setText(str(texto))


#----------------------------------Calculadora----------------------------------#

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