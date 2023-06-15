class Ciudad():
    def __init__(self,nombre,escan,sal,pais):
        self.Nombre = nombre
        self.Escandinava = escan
        self.Salario = sal
        self.Pais = pais
    def muestra(self):
        print(self.Nombre + " " + str(self.Escandinava) + " " + str(self.Salario) +" " + self.Pais)
    def incrementaSueldo(self, porcentaje):
        if type(self.Salario) == list:
            porcentaje = (porcentaje/100) + 1
            self.Salario[0] = self.Salario[0] * porcentaje
        else:
            porcentaje = (porcentaje/100) + 1
            self.Salario = self.Salario * porcentaje
    def normaliza(self):
       self.Nombre = self.Nombre.capitalize()
       self.Pais = self.Pais.capitalize()
#        if type(self.Salario) == float:
#            self.Salario.round()
ciudades = [Ciudad("madrid",False,1200,"españa"),
        Ciudad("estocolmo",True,1800,"suecia"),
        Ciudad("helsinki",True,2100,"finlandia"),
        Ciudad("bruselas",False,1400,"belgica"),
        Ciudad("paris",False,1500,"francia"),
        Ciudad("lyon",False,1400,"francia"),
        Ciudad("tampere",True,2000,"finlandia")]


for c in ciudades:
    c.normaliza()
    c.incrementaSueldo(5)
    c.muestra()
    print("\n")
class Ciudad2(Ciudad):
    def muestra(self):
        print(self.Nombre + "\n" + str(self.Escandinava) + "\n\t" + str(self.Salario[0]) + "\t" + str(self.Salario[1]) +"\n" + self.Pais + "\n")
ciudades2 = [Ciudad2("Madrid",False,[1200,0.84],"España"),
        Ciudad2("Estocolmo",True,[1800,0.91],"Suecia"),
        Ciudad2("Helsinki",True,[2100,0.90],"Finlandia"),
        Ciudad2("Bruselas",False,[1400,0,88],"Belgica"),
        Ciudad2("Paris",False,[1500,0.87],"Francia"),
        Ciudad2("Lyon",False,[1400,0.87],"Francia"),
        Ciudad2("Tampere",True,[2000,0.90],"Finlandia")]
print("CIUDADES2")
for c in ciudades2:
    c.normaliza()
    c.incrementaSueldo(5)
    c.muestra()
