from dataclasses import dataclass

@dataclass
class Util():
    
    @staticmethod
    def validarNumero(item):
        try:
            item = float(item)
            return True
        except ValueError:
            print('Error, debe ingresar un valor numérico')
            return False
