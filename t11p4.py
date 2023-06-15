import sys
def print_to_stderr(*a):

	# Here a is the array holding the objects
	# passed as the argument of the function
	print(*a, file=sys.stderr)


#print_to_stderr("Hello World")

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

    import sys
    def presentaBonito(self,numero):
            print_to_stderr(numero)
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
    LT.presentaBonito()



