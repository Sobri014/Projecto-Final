def funcion(numero):
    return 100/numero
# con try podemos capturar excepciones
try:
    print(funcion(0))
# print(funcion(1))
except ZeroDivisionError as e: # se ejecuta si se da un tipo especifico de error
    print("El numero NO puede ser 0 " + str(e))
except: # se ejecuta si hay algun otro error
    print("Error inesperado")
else: # se ejecuta si no hay errores
    print("El numero SI puede ser 1")
finally: # se ejecuta en cualquier caso
    print("esto se ejecuta en cualquier caso")

# con raise podemos forzar el lanzamiento de una excepcion aunque no se hubiera produci-do

numero_positivo = input("Introduce un numero positivo")
if int(numero_positivo) < 0:
    raise Exception("el numero debe ser positivo")
else:
    print("El numero es correcto")