class ListaTemperatura():
    def __init__(self):
        self.temperatura = []
    def add(self):
        print("Introduzca un numero:")
        num = float(input())
        if num > 35.0 and num < 42.0:
            self.temperatura.append(num)
        else:
            raise ExcepcionesTemperaturas
LT = []
LT = ListaTemperatura()

class ExcepcionesTemperaturas(Exception):
    def __init__(self):
        print("Fuera del rango")
try:
    LT.add()
    LT.add()
except ExcepcionesTemperaturas as error:
    print(error)










