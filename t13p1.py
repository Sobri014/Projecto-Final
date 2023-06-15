from t13p1modulo import EnumeracionDepartamento
from t13p1modulo import ClasePersona
from t13p1modulo import ClaseTrabajador,ClasEmpleado

persona = ClasePersona('Luis','26')
Empleado = ClaseTrabajador('TRD','  35000')
empleado_javier = ClasEmpleado("Javier Moreno",32,"CEQ",29500,EnumeracionDepartamento.FINANCIERO)
print(persona.Persona())
print(Empleado.Trabajador())
print(empleado_javier.Empleado())

