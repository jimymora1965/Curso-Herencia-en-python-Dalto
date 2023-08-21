class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nom = nombre
        self.e = edad
        self.n = nacionalidad
        

class Empleado(Persona):
    def __init__(self, nombre,edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)#lo que hereda de la clase padre
        self.t = trabajo
        self.s = salario
        
empleado1 = Empleado("Jimy","58","Colombiana","Progamador",100000)

print(empleado1.nom,empleado1.t, empleado1.s)

