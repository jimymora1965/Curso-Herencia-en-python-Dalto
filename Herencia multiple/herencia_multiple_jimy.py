class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.n = nombre
        self.e = edad
        self.nac = nacionalidad
        

class Artista:
    def __init__(self, habilidad):
        self.hab = habilidad
        
    def mostrarHabilidad(self):
        print(f"mi habilidad es: {self.hab}")
        

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre, edad,nacionalidad,habilidad, salario, empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.sal = salario
        self.emp = empresa
        
        
        
cantante = EmpleadoArtista("jimy",55,"colombia","cantar",100000,"Vegas")

print(cantante.hab)