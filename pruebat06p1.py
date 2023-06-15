# La Herencia es una relación de ‘Generalizacion’
# puesto que la clase padre es un ‘caso general’ de la clase hija
# clase padre (superclase)
class Vehiculo:
n_ruedas = 3
# clase hija (subclase)
class Coche(Vehiculo):
color = "gris"
precio = 30000
n_puertas = 3
def indicador(self):
print("es un coche")
def indicador2(self):
print("es un coche 2")
class Bmw(Coche):
modelobmw = "320"
def indicador(self):
print("es un Bmw")
# al tener el mismo nombre sobreescribe el de la clase padre (Coche)
# en Python No tenemos sobrecarga de método
# podemos hacer algo parecido a la sobrecarga mediante parámetros opcionales
cocheconcreto = Bmw()
# cocheconcreto, de la clase Bmw, tiene todos los miembros
# especificos de su clase (Bmw) y ademas todos los heredados
# de las clases de las que hereda (Coche y Vehiculo)
cocheconcreto.n_ruedas = 4
cocheconcreto.color = "azul"
cocheconcreto.precio = 40000
cocheconcreto.n_puertas = 5
cocheconcreto.modelobmw = "520"
cocheconcreto.indicador() # ejecuta el de la clase hija
cocheconcreto.indicador2()
print("Numero de Ruedas: " + str(cocheconcreto.n_ruedas) +
" Color: " + cocheconcreto.color +
" Precio: " + str(cocheconcreto.precio) +
" Numero de Puertas: " + str(cocheconcreto.n_puertas) +
" Modelo Bmw: " + cocheconcreto.modelobmw)
print(" ")
# para comprobar si una clase deriva de otra
print(issubclass(Coche,Vehiculo)) # True clase Coche es subclase de clase Vehiculo
print(issubclass(Vehiculo,Coche)) # False
print(issubclass(Bmw,Vehiculo)) # True clase Coche tambien deriva de clase Vehiculo
print(issubclass(Coche,Coche)) # True una clase tambien es subclase de si misma
print(issubclass(Bmw,(Vehiculo,Coche))) # True
# en el segundo parámetro podemos meter una tupla de clases en lugar de una sola clase
print(" ")
# para comprobar si un objeto es una instancia de una clase
print(isinstance(cocheconcreto,Bmw)) # True
# tambien se considera instancia de las clases de las que deriva su propia clase
print(isinstance(cocheconcreto,Coche)) # True
print(isinstance(cocheconcreto,Vehiculo)) # True
print(isinstance(cocheconcreto,(Vehiculo,Coche))) # True
# en el segundo parámetro podemos meter una tupla de clases en lugar de una sola clase