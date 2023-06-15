from enum import Enum

class EnumeracionDepartamento(Enum):
        TESORERIA = 'tesoreria'
        RRHH = 'rrhh'
        GUERRA = 'guerra'
        FINANCIERO = 'financiero'
class ClasePersona():
    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad = Edad

    def Persona(self):
        return f"{self.Nombre} {self.Edad}"

class ClaseTrabajador():
    def __init__(self, Codigo, Salario):
        self.Codigo = Codigo
        self.Salario = Salario

    def Trabajador(self):
        return f"{self.Codigo} {self.Salario}"

class ClasEmpleado(ClaseTrabajador,ClasePersona):

    def __init__(self,Codigo, Salario, Nombre, Edad, Departamento):
        ClaseTrabajador.__init__(self, Codigo, Salario)
        ClasePersona.__init__(self, Edad, Nombre)
        self.departamento = Departamento
    def Empleado(self):
        return f"{ClasePersona.Persona(self)} {ClaseTrabajador.Trabajador(self)} {self.departamento.value}"

