from PyQt6 import uic
from PyQt6.QtWidgets import QDialog
from email.message import EmailMessage
import smtplib

class Recordatorios():
    def __init__(self) -> None:
        self.recordatorios = uic.loadUi("../SLI_Trabajo_Final/resources/templates/recordatorios.ui")
        self.recordatorios.showMaximized()
        self.prepararCorreo()


    def prepararCorreo(self):
        self.recordatorios.btnCorreo.clicked.connect(self.enviarCorreo)


    def enviarCorreo(self):

        mensaje = self.recordatorios.mensajeInput.toPlainText()
        emisor = "shadowbyteweb@gmail.com"
        receptor = self.recordatorios.correoInput.text()
        correo = EmailMessage()
        correo["From"] = emisor
        correo["To"] = receptor
        correo["Subject"] = "Recordatorio"
        correo.set_content(mensaje)

        smtp = smtplib.SMTP_SSL('smtp.gmail.com')
        smtp.login(emisor, "kigp xuzp ogps mrqe")
        smtp.sendmail(emisor,receptor,correo.as_string())
        smtp.quit()