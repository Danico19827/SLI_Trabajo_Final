from PyQt6 import uic
import json

from PyQt6.QtGui import QIntValidator


class Tiempo():

    def __init__(self) -> None:
        self.tiempo = uic.loadUi("../SLI_Trabajo_Final/resources/templates/tiempo.ui")

        # Esto permite solamente el ingreso de enteros entre el rango 0~24
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 9)
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
        resultado = str(horasDelDia) + ' horas disponibles: '
        if horasDelDia > 7:
            if trabajar == 0:
                resultado += 'Puedes trabajar en algo'
            elif estudiar == 0:
                resultado += 'Puedes estudiar algo'
            elif deportes > 4 and descansar < 7:
                resultado += 'Descansar tambien es entrenar'
            else:
                resultado += 'Todo en orden'
        elif horasDelDia > 3:
            if trabajar > 3 and estudiar > 3 and descansar > 6:
                resultado += 'Vas bien, sigue así'
            elif jugar > 3:
                resultado += 'Debes dejar de jugar tanto'
            elif comer > 3:
                resultado += 'No comas tanto'
            elif viajar > 3:
                resultado += 'Deberías mudarte para ahorrar tiempo'
            else:
                resultado += 'Todo en orden'
        elif horasDelDia >= 0:
            if descansar > 8:
                resultado += 'Te relajas demasiado'
            elif trabajar > 8:
                resultado += 'Trabajas demasiado'
            elif estudiar > 8:
                resultado += 'Estudias demasiado'
            elif jugar > 8:
                resultado += 'Juegas demasiado'
            elif viajar > 8:
                resultado += 'Definitivamente debes mudarte'
            elif comer > 4:
                resultado += 'Comes demasiado'
            elif deportes > 5:
                resultado += 'Descansar tambien es entrenar'
            else:
                resultado += 'Tomate las cosas con calma'
        else:
            return 'Error en el calculo, revisa nuevamente'
        if descansar < 7:
                resultado += ', no olvides descansar'
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


    # Guarda los datos luego de cada cambio y crea un archivo nuevo si no existe el JSON
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

