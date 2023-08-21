class Medicos:
    def __init__(self, especialidad, universidad, fecha_ingreso):
        self.e = especialidad
        self.u = universidad
        self.f_i = fecha_ingreso       

class Especialistas(Medicos):
    def __init__(self, especialidad, universidad, fecha_ingreso, salario, sede):
        super().__init__(especialidad, universidad, fecha_ingreso)
        self.s = salario
        self.sed = sede

jimy_mora = Especialistas("Anestesiologia\n","Javeriana\n", "26-julio-2023\n","100000\n", "Principal")
frank_gamez = Especialistas("Anestesiologo\n","Venezuela\n", "26-julio-2023\n","1000000\n","Playa")

print(jimy_mora.e, jimy_mora.u,jimy_mora.f_i,jimy_mora.s,jimy_mora.sed)

print()

print(frank_gamez.e,frank_gamez.u,frank_gamez.f_i,frank_gamez.s,frank_gamez.sed)