class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
  # la clase artista no herede de Persona, es una clase diferente
class Artista: 
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrarHabilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        
""" creamos la clase EmpleadoArtista que hereda de 2 clases diferente y
propiedades diferentes     """   

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self,nombre, edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
#ahora, si quiero usar la clase "super" que se usa en herencia simple:

    def presentarse(self):
       return(super().mostrarHabilidad)#puedo usar return o print. el resultado es igual 
   
   
domador = EmpleadoArtista("Robert",55,"colombia","cantar",10000,"Circo Gasca")
print(domador.nombre)

#con estas lineas vemos si EmpleadoArtista es subclase de persona
herencia = issubclass(EmpleadoArtista,Persona)
print(herencia)

#con esta vemos si domador es una instancia

instancia = isinstance(domador,Persona)
print(instancia)