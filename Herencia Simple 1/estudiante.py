class Persona:
    def __init__(self, nombre,edad):
        self.n = nombre
        self.e = edad
        
    def mostrarDatos(self):
        print(f"Nombre: {self.n}")
        print(f"Edad:{self.e}")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad, grado):
        super().__init__(nombre,edad)
        self.g = grado
    
    def mostrarGrado(self):
        print(f"Grado: {self.g}")

estudiante = Estudiante("Juan","24","10mo")
estudiante.mostrarDatos()
estudiante.mostrarGrado()