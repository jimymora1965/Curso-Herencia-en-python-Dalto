class Medico:
    def __init__(self,nombre, especialidad, nacionalidad):
        self.nom = nombre
        self.e = especialidad
        self.n = nacionalidad

class Especialista(Medico):
    def __init__(self, nombre, especialidad, nacionalidad , salario, sede):
        super().__init__(nombre, especialidad, nacionalidad)


medico1= Especialista("Felipe","Ginecologo","Colombiano",1000000,"Playa")
medico2 = Especialista("Frank","Anestesia","Venezuela",500000,"Laureles")

print(medico1.e)
print(medico2.n)