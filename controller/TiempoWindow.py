from PyQt6 import uic
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt
import json
import numpy as np
import math

from PyQt6.QtGui import QIntValidator

class Tiempo():

    def __init__(self) -> None:
        self.tiempo = uic.loadUi("../SLI_Trabajo_Final/resources/templates/prueba2.ui")

        # Esto permite solamente el ingreso de enteros entre el rango 0~24
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 24)
        self.tiempo.txtTrabajar.setValidator(onlyInt)
        self.tiempo.txtEstudiar.setValidator(onlyInt)
        self.tiempo.txtComer.setValidator(onlyInt)
        self.tiempo.txtDescansar.setValidator(onlyInt)
        self.tiempo.txtJugar.setValidator(onlyInt)
        self.tiempo.txtViajar.setValidator(onlyInt)
        self.tiempo.txtDeportes.setValidator(onlyInt)

        # Método para detectar cambios en los txt
        self.detectarCambio()
        
        # Método para cargar datos
        self.cargarDatos()

        self.tiempo.txtTrabajar.setFocus() 
        self.tiempo.show()
        self.tiempo.showMaximized()
        
    # Muestra un resultado en la ventana
    def cambiarResultado(self):

        horasDelDia  = 24
        trabajar = int(self.tiempo.txtTrabajar.text())
        estudiar = int(self.tiempo.txtEstudiar.text())
        comer = int(self.tiempo.txtComer.text())
        descansar = int(self.tiempo.txtDescansar.text())
        jugar = int(self.tiempo.txtJugar.text())
        viajar = int(self.tiempo.txtViajar.text())
        deportes = int(self.tiempo.txtDeportes.text())
        horasDelDia -= (trabajar + estudiar + comer + descansar + jugar + viajar + deportes)
        
        resultado = self.calcularResultado(horasDelDia, trabajar, estudiar, comer, descansar, jugar, viajar, deportes)

        self.tiempo.lblResultado.setText(resultado)
        
        self.guardarDatos()
        pass

    # Calcula el resultado de la evaluación
    def calcularResultado(self, horasDelDia, trabajar, estudiar, comer, descansar, jugar, viajar, deportes):
        resultado = 'Tienes ' + str(horasDelDia) + ' horas disponibles '
        if horasDelDia <= 0:
            resultado = 'Tienes 0 horas disponibles '

        if horasDelDia > 6:
            if trabajar < 4 or estudiar < 2:
                resultado +=  ', dedicale más tiempo al trabajo o estudio.'
            else:
                resultado += ', tienes tiempo para descansar y jugar'
        elif horasDelDia > 4:
            if viajar > 6:
                resultado += ', deberías mudarte a un lugar más cercano'
            elif jugar > 6:
                resultado += ', al parecer eres jugador profesional'
            else:
                resultado += ', vamos bien'
        else:
            if descansar > 8 or jugar > 8:
                resultado += ',no es bueno relajarse tanto'
            else:
                resultado += ',algo anda mal'
        return resultado

    # Son lo métodos que se activan al realizar un cambio en cada txt
    def detectarCambio(self):
        self.tiempo.txtTrabajar.textChanged.connect(self.cambiarResultado)
        self.tiempo.txtEstudiar.textChanged.connect(self.cambiarResultado)
        self.tiempo.txtComer.textChanged.connect(self.cambiarResultado)
        self.tiempo.txtDescansar.textChanged.connect(self.cambiarResultado)
        self.tiempo.txtJugar.textChanged.connect(self.cambiarResultado)
        self.tiempo.txtViajar.textChanged.connect(self.cambiarResultado)
        self.tiempo.txtDeportes.textChanged.connect(self.cambiarResultado)
    
    # Carga de datos desde JSON
    def cargarDatos(self):
        try:
            with open('gestionDelTiempo.json', 'r') as archivo:
                datos = json.load(archivo)
                print(datos)
                self.llenarCamposDesdeJSON(datos)
        except FileNotFoundError:
            self.tiempo.lblResultado.setText("No se encontró el archivo de datos")

    def llenarCamposDesdeJSON(self, datos):
        self.tiempo.txtTrabajar.setText(datos["trabajar"])
        self.tiempo.txtEstudiar.setText(datos["estudiar"])
        self.tiempo.txtComer.setText(datos["comer"])
        self.tiempo.txtDescansar.setText(datos["descansar"])
        self.tiempo.txtJugar.setText(datos["jugar"])
        self.tiempo.txtViajar.setText(datos["viajar"])
        self.tiempo.txtDeportes.setText(datos["deportes"])
        self.tiempo.lblResultado.setText(datos["resultado"])


    # Guarda los datos luego de cada cambio
    def guardarDatos(self):
        datos = {}
        datos["trabajar"] = self.tiempo.txtTrabajar.text()
        datos["estudiar"] = self.tiempo.txtEstudiar.text()
        datos["comer"] = self.tiempo.txtComer.text()
        datos["descansar"] = self.tiempo.txtDescansar.text()
        datos["jugar"] = self.tiempo.txtJugar.text()
        datos["viajar"] = self.tiempo.txtViajar.text()
        datos["deportes"] = self.tiempo.txtDeportes.text()
        datos["resultado"] = self.tiempo.lblResultado.text()
        try:
            with open('gestionDelTiempo.json', 'w') as archivo:
                json.dump(datos, archivo, indent=2)
        except:
            self.tiempo.lblResultado.setText('No se encontró el archivo de datos')